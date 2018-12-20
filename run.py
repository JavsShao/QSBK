import requests
from urllib.parse import urlencode
from pyquery import PyQuery


url = 'http://www.qiushibaike.com/8hr/page/1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.8'}


def parse_page(res_html):
    print('我在解析源码！')


def get_page():
    '''
    获取源码
    :return:
    '''
    try:
        response = requests.get(url, headers=headers)
        res_html = response.text
        if response.status_code == 200:
            parse_page(res_html)
    except Exception as e:
        print(e.args)

if __name__ == '__main__':
    get_page()