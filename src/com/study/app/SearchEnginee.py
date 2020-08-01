from flask import Flask
from flask import render_template
from flask import request

from src.com.study.app.searchSpider import query

app = Flask(__name__)

@app.route('/baidu')
def index():
    return render_template('index.html')

@app.route('/s')
def search():
    keyword = request.args.get('wd')
    html = query(keyword)
    return html

if __name__ == '__main__':
    app.run(debug=True)