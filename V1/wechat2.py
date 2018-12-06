import itchat
from itchat.content import *
# itchat.content包含所有的消息类型参数，这样处理的好处是代码中引用时不需要写前缀，比如文本类型不需写itchat.content.TEXT，只需写TEXT

# 通过装饰符将函数text_reply()注册为处理消息的函数，对收到的文本TEXT、地图MAP、名片CARD、通知NOTE、分享SHARING作出回应
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])  # 装饰器
def text_reply(msg): # 形参msg接收发来的信息，信息是字典类型
	return "【自动回复】我已收到您的消息，多谢~\n\n【来自WinTerson的Python小机器人】"  # 设定回复信息

# 对发过来的图片/表情PICTURE、语音RECORDING、附件ATTACHMENT和视频VIDEO作出回应
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def receiveFile_reply(msg):
	return "【自动回复】我收到了一个{}文件，多谢~\n\n【来自WinTerson的Python小机器人】".format(msg['Type'])

itchat.auto_login(True)
# 扫码登陆。也可以写成itchat.auto_login(hotReload=True)，参数为True的作用是存储登陆，这样即使程序关闭，一定时间内重新开启也可以不用重新扫码。itchat.auto_login()不具备存储登陆的功能

itchat.run()  # 等待新消息
