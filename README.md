# Youth_Study_Script

## 这个脚本已经挂了。各显神通吧。

青年大学习批量学习脚本(广东）

# 这是什么？

Youth_Study_Script是一个基于Python开发的脚本，这个Python脚本通过利用特定的API和标头自动记录青年学习平台的学习历史过程，从而**免去**团支书催促青年大学习烦恼。

# 如何使用？

## 先决条件

 1. 安装**Python 3.X**以上的版本，本人是基于3.11.4的版本运行的。
 2. 确保安装了必要的第三方库**requests**库

## 指南

1. 下载Github仓库里的**main.py**脚本或者是Package文件夹里面的**main.exe**到本地计算机。 
2. 确保安装了必要的Python库（`requests`）。
3. 将下载的脚本放置在一个空文件夹下，第一次运行会生成一个mid.txt文件，用姓名替换 `姓名`（仅方便团支书标记mid对应哪位团员），用相应的数字代码替换 `mid数字代码`。如需添加更多mid只需参照格式往下添加即可。举个例子：
```
# 姓名1
Mid1
# 姓名2
Mid2
# 姓名3
Mid3
以此类推
```
4. 在Python环境中执行脚本。 
5. 按照提示继续操作。

# 如何获取团员们对应的Mid？

 1. 前往**广东智慧团建系统**，生成**电子团员证**，然后通过微信转发给功能获取该团员的电子团员证**链接**。
![申请电子团员证](https://picdl.sunbangyan.cn/2023/12/23/1565a902fb61a1cd10bfde600fe1638c.jpeg)

2.获取到的链接一般有如下两种：
> https://tuan.12355.net/wechat/view/information/member_certification_photo.html?mid=xxxxxx

> https://tuan.12355.net/wechat/view/information/member_certification_generated.html?memberId=xxxxxx&showMemberAdditionNames=&showMemberRewa

两种链接中的xxxxxx部分即是该团员的mid代码，将其按照格式要求填到mid.txt里面即可使用脚本代完成最新一期的青年大学习。

# 开源协议
本仓库代码基于MIT协议开源。
