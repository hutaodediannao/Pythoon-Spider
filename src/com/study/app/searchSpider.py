import requests


def query(word):
    url = 'https://www.baidu.com/s?wd=%s' % word
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
    }
    html = requests.get(url, headers=header).text
    return html
