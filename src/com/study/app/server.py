
# 负责启动WSGI服务器函数，加载application函数
from wsgiref.simple_server import make_server

from src.com.study.app.WSGI import application

httpd = make_server('', 8889, application)
print('Serving HTTP on port 8889...')
httpd.serve_forever()
