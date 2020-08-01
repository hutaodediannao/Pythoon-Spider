from tkinter import *
import requests
from PIL import Image, ImageTk


def sign():
    # 获取用户输入的名字
    name = entry.get()
    url = 'http://m.uustv.com/'
    header = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'
    }

    data = {
        'word': name,
        'sizes': '60',
        'fonts': 'zql.ttf',
        'fontcolor': '#000000'
    }

    html = requests.post(url, data, headers=header).text
    # print(html)
    reg = r'<img src="tmp/(.*?).gif"/>'
    icons = re.findall(reg, html)
    # print(icons)
    targetImgUrl = '%stmp/%s.gif' % (url, icons[0])
    # print(targetImgUrl)

    # 保存图片
    imgName = '{}.gif'.format(name)
    response = requests.get(targetImgUrl).content
    with open(imgName, 'wb') as f:
        f.write(response)
        f.close()

    # 显示图片
    bm = ImageTk.PhotoImage(file=imgName)
    label2 = Label(root, image=bm)
    label2.bm = bm
    label2.grid(row=2, columnspan=2)


# 创建窗口
root = Tk()

# 窗口大小
root.geometry('535x305+200+200')

# 标题
root.title('签名设计')

# 标签控件
label = Label(root, text='签名', font=('文化行楷', 20), fg='pink')

# 定位
label.grid()

# 输入框
entry = Entry(root, font=('微软雅黑', 20))
entry.grid(row=0, column=1)

# 点击按钮
button = Button(root, text='设计签名', font=('微软雅黑', 20), command=sign)
button.grid(row=1, column=1)

# 显示窗口
root.mainloop()

# 根据用户输入名字
# 爬虫爬取签名网站上的图片
