# 解析webhtml
from requests_html import HTMLSession


session = HTMLSession()


def fetchBaidu():
    """
    抓取百度的数据，测试获取接口字段
    """
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'
    result = session.get('http://www.xbiquge.la/44/44391/19673679.html', headers={'user-agent': ua})
    for i in result.html.find('div'):
        # 展示抓取HTML内容信息
        print(i.text)


fetchBaidu()
