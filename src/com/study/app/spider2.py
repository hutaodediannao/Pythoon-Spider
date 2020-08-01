import os
from urllib.request import urlretrieve


def dowloadVideo(url):
    path = 'orangeVideo'
    if path not in os.listdir():
        os.mkdir(path)
    lastIndex = str(url).rindex('/')
    fileName = 'orange_video'
    filePath = path + '/%s' % fileName
    urlretrieve(url, filePath)
    pass

dowloadVideo('thunder://QUFodHRwczovL3d3dy5zc3h6eGwxLmNvbS95YXpob3UvMjAyMF8wNy8yNy95YXpob3VfNkR1NFF3OGhfd20ubXA0Wlo=')