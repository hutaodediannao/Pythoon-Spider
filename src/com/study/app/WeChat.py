from wxpy import *
turing = Tuling(api_key='4a0488cdce684468b95591a641f0971d')
bot = Bot()
#只跟某一个好友聊天
nc=input("输入好友昵称：")
xianding = bot.friends().search(nc)
@bot.register(chats=xianding)
def communite(msg):
    turing.do_reply(msg)
embed()


