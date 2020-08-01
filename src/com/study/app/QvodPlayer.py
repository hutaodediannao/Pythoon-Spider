import re
from tkinter import Tk, LEFT, BOTH
from tkinter import ttk

import requests

# 所有下载对象容器
dowloadElements = []

# 封装下载对象
class DowloadElement:
    def __init__(self, title, dowloadurl):
        self.title = title
        self.dowloadurl = dowloadurl
        pass

    def __str__(self) -> str:
        return '{title=%s, dowloadurl=%s}' % (self.title, self.dowloadurl)


# 开始搜索引擎请求数据
def requestNetData(queryKey):
    url = 'https://www.bpn6.com/shipin/list-%s.html' % queryKey
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/83.0.4103.106 Safari/537.36 '
    }
    html = requests.get(url, headers=header).text
    # print(html)
    reg = r'<a href="(.*?).html" title='
    srcList = re.findall(reg, html)
    # print(srcList)
    videoUrlList = []
    for src in srcList:
        videoUrlList.append('https://www.bpn6.com%s.html' % src)
    # print(videoUrlList)

    # 开始根据电影页面遍历爬取下载地址
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/83.0.4103.106 Safari/537.36 '
    }
    for videoUrl in videoUrlList:
        try:
            html = requests.get(videoUrl, headers=header).content.decode('utf-8')
            # 下载地址
            reg = r'<input type="text" data-clipboard-text="(.*?)" id="lin1k1"'
            dowloadUrl = re.findall(reg, html)[0]
            # 下载title
            reg2 = r'<h2 class="c_pink text-ellipsis">(.*?)</h2>'
            title = re.findall(reg2, html)[0]
            # 开始封装对象
            de = DowloadElement(title, dowloadUrl)
            dowloadElements.append(de)

            for e in dowloadElements:
                print(e)
        except Exception:
            print('出现错误...')
            continue
    # 数据返回来了，开始重新渲染UI
    drowUI()

# 绘制GUI
def drowUI():

    root = Tk()  # 初始框的声明
    root.geometry('1000x700+100+50')
    root.title('宅男神器，你懂的')
    columns = ("姓名", "IP地址")
    treeview = ttk.Treeview(root, height=18, show="headings", columns=columns)  # 表格

    treeview.column("姓名", width=300, anchor='center')  # 表示列,不显示
    treeview.column("IP地址", width=700, anchor='center')

    treeview.heading("姓名", text="姓名")  # 显示表头
    treeview.heading("IP地址", text="IP地址")
    treeview.pack(side=LEFT, fill=BOTH)

    # name = ['日本自摸美女', '服务器', '笔记本']
    # ipcode = ['10.13.71.223', '10.25.61.186', '10.25.11.163']
    for i in range(min(len(dowloadElements), len(dowloadElements))):  # 写入数据
        treeview.insert('', i, values=(dowloadElements[i].title, dowloadElements[i].dowloadurl))

    root.mainloop()
    pass



# 绘制UI
# drowUI()
# 请求数据
requestNetData('经典三级')
