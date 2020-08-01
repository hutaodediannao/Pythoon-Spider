# 有道词典
import json
from tkinter import Label, Entry, Button, Tk

import requests


def search(word, callback):
    url = 'https://fanyi.baidu.com/sug'
    keyword = word
    header = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36'
    }
    data = {'kw': keyword}
    jsonResult = requests.post(url, data, headers=header).text.encode('utf-8')
    # print(jsonResult)
    pyjo = json.loads(jsonResult)
    result = str(pyjo['data'][0]['v'])
    print(result)
    callback(result)


def initUI():
    # 创建窗口
    root = Tk()
    # 窗口大小
    root.geometry('800x200+200+200')
    # 标题
    root.title('有道词典')
    # 标签控件
    label = Label(root, text='词典', font=('文化行楷', 10), fg='pink')
    # 定位
    label.grid()
    # 输入框
    entry = Entry(root, font=('微软雅黑', 10))
    entry.grid(row=0, column=1)

    result = ''

    def callback(re):
        print('re ========> %s' % re)
        nonlocal result
        result = re
        # labelResult.text = result

        labelResult = Label(root, text=result, font=('文化行楷', 10), fg='red')
        labelResult.grid()
        pass

    def hand():
        searchKey = entry.get()
        print(searchKey)
        search(searchKey, callback)
        pass

    # 点击按钮
    button = Button(root, text='开始翻译', font=('微软雅黑', 10), command=hand)
    button.grid(row=1, column=1)

    # 显示窗口
    root.mainloop()
    pass


initUI()
