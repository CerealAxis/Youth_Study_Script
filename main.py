import json
import requests as r
import urllib.parse
import os

apiHeaders = {
    'Host': 'tuanapi.12355.net',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Origin': 'https://tuan.12355.net',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; M2012K11AC Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2691 MMWEBSDK/201101 Mobile Safari/537.36 MMWEBID/8628 MicroMessenger/7.0.21.1783(0x27001543) Process/tools WeChat/arm64 Weixin GPVersion/1 NetType/WIFI Language/zh_CN ABI/arm64',
    'X-Requested-With': 'com.tencent.mm',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://tuan.12355.net/wechat/view/YouthLearning/page.html',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
}

youthstudyHeaders = {
    'Host': 'youthstudy.12355.net',
    'Connection': 'keep-alive',
    'Content-Length': '134',
    'Origin': 'https://youthstudy.12355.net',
    'X-Litemall-Token': '',
    'X-Litemall-IdentiFication': 'young',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; M2012K11AC Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2691 MMWEBSDK/201101 Mobile Safari/537.36 MMWEBID/8628 MicroMessenger/7.0.21.1783(0x27001543) Process/tools WeChat/arm64 Weixin GPVersion/1 NetType/WIFI Language/zh_CN ABI/arm64',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'X-Requested-With': 'com.tencent.mm',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://youthstudy.12355.net/h5/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
}

def get_sign(mid):
    url = f"https://tuanapi.12355.net/questionnaire/getYouthLearningUrl?mid={mid}"
    response = r.get(url, headers=apiHeaders)

    if response.status_code == 200:
        j = response.json()
        sign_url = j.get('youthLearningUrl', '')
        sign = sign_url.split('?')[1][5:]
        return sign
    else:
        raise ConnectionError(f"Failed to fetch sign for {mid}")

def get_token(sign):
    payload = f"sign={urllib.parse.quote(sign)}"
    url = "https://youthstudy.12355.net/apih5/api/user/get"
    response = r.post(url, headers=youthstudyHeaders, data=payload)

    if response.status_code == 200:
        j = response.json()
        token = j["data"]["entity"]["token"]
        return token
    else:
        raise ConnectionError("Failed to fetch token")

def get_chapter_id():
    url = "https://youthstudy.12355.net/apih5/api/young/chapter/new"
    headers = {
        'X-Litemall-IdentiFication': 'young'
    }
    response = r.get(url, headers=headers)

    if response.status_code == 200:
        j = response.json()
        chapter_id = j["data"]["entity"]["id"]
        return chapter_id
    else:
        raise ConnectionError("Failed to fetch chapter ID")

def save_history(token, cid):
    headers = youthstudyHeaders
    headers["X-Litemall-Token"] = token
    url = "https://youthstudy.12355.net/apih5/api/young/course/chapter/saveHistory"
    payload = {'chapterId': str(cid)}
    response = r.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        return response.json()
    else:
        raise ConnectionError("Failed to save history")

if __name__ == "__main__":
    if not os.path.isfile("mid.txt"):
        with open("mid.txt", "w") as file:
            file.write("# 姓名\nmid数字代码\n")
            print("已生成 mid.txt 文件")
    else:
        with open("mid.txt") as file:
            lines = file.readlines()
            pairs = [lines[i:i + 2] for i in range(0, len(lines), 2)]
            for pair in pairs:
                name = pair[0].strip()
                number = pair[1].strip()
                if number and not number.startswith('#'):
                    print(f"姓名: {name}")
                    print("开始：" + number)
                    try:
                        chapter_id = get_chapter_id()
                        sign = get_sign(number)
                        token = get_token(sign)
                        result = save_history(token, chapter_id)
                        if result["errno"] == 0:
                            print("保存观看记录成功")
                        else:
                            print("出错啦")
                            print(result["errmsg"])
                    except Exception as e:
                        print(str(e))
                        print(f"{number} 异常")
                        continue

    input("按任意键继续...")
