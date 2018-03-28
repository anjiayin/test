
'''from PIL import Image
import matplotlib.pyplot as plt

img=Image.open('E:\\车车检测\\QQ微信询报价工具\\wxbot\\QR.png')
plt.figure("dog")
plt.imshow(img)
plt.show()
'''
import itchat
from itchat.content import TEXT

@itchat.msg_register(TEXT, isFriendChat=True, isGroupChat=True, isMpChat=True)
def simple_reply(msg):
    return 'I received: %s' % msg.text

itchat.auto_login(True)
itchat.run()
