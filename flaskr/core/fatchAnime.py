#!/usr/bin/python3
# -*- coding: UTF-8 -*-
__Author__ = "Alvin Liu"

'http://www-mipengine-org.mipcdn.com/i/p3.manhuapan.com/2020/12/11211014200587.jpg'
'http://www-mipengine-org.mipcdn.com/i/p3.manhuapan.com/2020/12/11211014200599.jpg'

from requests_html import AsyncHTMLSession
from requests_html import HTMLSession


async_session = AsyncHTMLSession()


async def fetchBaidu():
    """
    抓取百度的数据，测试获取接口字段
    """
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'
    result = await async_session.get('https://manhua.fzdm.com/2/998/index_1.html', headers={'user-agent': ua})
    for i in result.html.find('img'):
        # 展示抓取HTML内容信息
        print(i)


# fetchBaidu()
async_session.run(fetchBaidu)
