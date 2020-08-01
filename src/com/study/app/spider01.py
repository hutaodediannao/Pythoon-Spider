import os
import re

import requests
from urllib.request import urlretrieve

def dowload_video():
    url = 'https://www.pearvideo.com/category_8'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/83.0.4103.106 Safari/537.36 '
    }
    html = requests.get(url, headers=header).text
    reg = r'<a href="(.*?)" class="vervideo-lilink actplay">'
    video_ids = re.findall(reg, html)
    # print(str(video_ids))
    video_url = []
    startUrl = 'https://www.pearvideo.com/'
    for vid in video_ids:
        newUrl = startUrl + vid
        video_url.append(newUrl)

    for playUrl in video_url:
        html = requests.get(playUrl, headers=header).text
        reg = r'srcUrl="(.*?)",'
        purl = re.findall(reg, html)

        reg2 = r'<h1 class="video-tt">(.*?)</h1>'
        video_name = re.findall(reg2, html)
        print(video_name[0])
        print("开始下载视频:%s" % video_name[0])
        path = 'video'
        if path not in os.listdir():
            os.mkdir(path)

        filepath = path + '/%s.mp4' % video_name[0]
        # 专门下载的方法封装
        urlretrieve(purl[0], filepath)


dowload_video()
