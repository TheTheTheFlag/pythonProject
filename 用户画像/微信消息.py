import win32clipboard as w
import win32con
import win32api
import win32gui
import time
import random


# 把文字放入剪贴板
def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()


# 模拟ctrl+V
def ctrlV():
    win32api.keybd_event(17, 0, 0, 0)  # ctrl
    win32api.keybd_event(86, 0, 0, 0)  # V
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)


# 模拟alt+s
def altS():
    win32api.keybd_event(18, 0, 0, 0)
    win32api.keybd_event(83, 0, 0, 0)
    win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)


# 模拟enter
def enter():
    win32api.keybd_event(13, 0, 0, 0)
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)


# 模拟单击
def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


# 移动鼠标的位置
def movePos(x, y):
    win32api.SetCursorPos((x, y))


# list = ['王超',
#         '一日看尽',
#         '牛中',
#         '超杰',
#         '韩艳',
#         '马万',
#         '陶敬',
#         '秋霜',
#         '大表姐',
#         '张辉',
#         '辛明利']
list = ['文件传输助手',
        '文件传输助手',
        '文件传输助手',
        '文件传输助手',
        '文件传输助手',
        '文件传输助手',
        '文件传输助手',
        '文件传输助手',
        '文件传输助手',
        '文件传输助手',
        '文件传输助手'
        ]
list2 = ['百炼千锤一根针，一颠一倒布上行。眼晴长在屁股上，只认衣冠不认人',
         '子孙中山狼，得志便猖狂。金闺花柳质，一载赴黄粱。',
         '殿前兵马虽骁雄，纵暴略与羌浑同。闻道杀人汉水上，妇女多在官军中。',
         '人皆养了望聪明，我被聪明误一生。惟愿孩儿愚且鲁，无灾无难到公卿',
         '何处望神州？满眼风光北固楼。千古兴亡多少事？悠悠。不尽长江滚滚流',
         '年少万兜鍪，坐断东南战未休。天下英雄谁敌手？曹刘。生子当如孙仲谋。',
         '尔曹身与名俱灭，不废江河万古流',
         '蚍蜉撼大树，可笑不自量。',
         '塞上纵归他日马，城东不斗少年鸡。',
         '十有九人堪白眼，百无—用是书生',
         '朽木不可雕也，粪土之墙不可杇也！于予与何诛'
         ]
list3 = ['你属什么?不，你属黄瓜的，天生就是欠拍!',
         '你吃错药了吗?还是忘吃药了?',
         '手榴弹看到你都会自曝，猪见到你都会嘲笑，你咋还好意思活在世上呢?',
         '你长得可真是野兽抽象派啊。',
         '小姐姐，你的床好繁忙啊，一轮又一轮，人来人往没得歇。',
         '巴黎圣母院一直缺个敲钟的，你再适合不过了。',
         '我真的只想骂人，所以不会骂你。',
         '以后和我联系前能不能先把脑袋按上，总是拿你的无知挑战我下限，我真是怕了你了。',
         '亲亲，您复杂的五官和四肢，完全没办法掩盖您朴素接地气的智商哇!',
         '我真是为你好，别再跑街上乱晃了，随便去动物园应聘某个笼子也好，到时候在街上被警察射杀可就糟了。',
         '问你个问题啊，恶心妈妈抱着恶心一直在哭，这是为啥?因为见到你以后恶心死了!',
         '你看看你长这个德性，就是光着身子追我半个地球我也不会动心，我回一次头都算我输。'
         ]
i = 0
total = 100

for index, \
    n \
        in enumerate(list3):
    if __name__ == "__main__":
        # 获取鼠标当前位置
        # hwnd=win32gui.FindWindow("MozillaWindowClass",None)
        hwnd = win32gui.FindWindow("WeChatMainWndForPC", None)
        win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
        win32gui.MoveWindow(hwnd, 0, 0, 1000, 700, True)
        time.sleep(0.01)
        movePos(28, 147)
        click()
        movePos(140, 28)  # x,y
        click()
        time.sleep(1)
        setText("文件传输助手")  # 接收人的名字
        ctrlV()
        # click()
        time.sleep(1)
        enter()
        time.sleep(1)
        setText(n)
        ctrlV()
        altS()
