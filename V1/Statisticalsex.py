import itchat

itchat.auto_login(True)    # 扫码登录

female, male, other = [], [], []
# 初始化列表，一条语句替代了三条语句：female = []
#                                male = []
#                                other = []

friendList = itchat.get_friends(update=True)[1:]
# itchat.get_friends()获得微信好友列表，第一个成员（索引为0）是自己。[1:]是众好友

for friend in friendList:       # 遍历好友列表

    gender = friend["Sex"]      # 取出微信好友的性别，放进变量gender里
    if gender == 1:             # gender值为1是男性
       male.append(friend['DisplayName']or friend['NickName'])
       # 将你自己给好友设置的备注名friend['DisplayName']或好友自己起的微信称呼friend['NickName']添加到男性朋友列表male中
    elif gender == 2:           # 女性，添加进列表female
       female.append(friend['DisplayName']or friend['NickName'])
    else:                      # 没标注性别的放进other列表
       other.append(friend['DisplayName']or friend['NickName'])

print('男性朋友{}位，他们是：{}'.format(len(male), male))
print('女性朋友{}位，她们是：{}'.format(len(female), female))
print('没写性别朋友{}位：{}'.format(len(other), other))
# 输出每个列表的人数和成员