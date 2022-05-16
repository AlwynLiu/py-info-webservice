import requests
from requests_html import HTMLSession


def requestData(url):
    session = HTMLSession()
    result = session.get(url)
    ul_elements = result.html.find('span.title')
    for i in ul_elements:
        print(i.links)
    # print(result.html.find('div#videoCategory').text)



def popular_women():
    session = HTMLSession()
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'
    url = 'https://www.youtube.com/'
    result = session.get(url, headers={'user-agent': ua})
    print(result.text)
    video_items = result.html.find('a')
    for i in video_items:
        print('视频名称：', i.text)
        print("链接地址：", i.links)


# def download_video():
#     # session = HTMLSession()
#     for i in range(10):
#         url = ''''''.format(i)
#         f = open('./1.ts', 'wb')
#         result = requests.get(url)
#         print(result.content)
#         f.write(result.content)
#         f.close()


# url = ''
# requestData(url)

url = 'https://www.youtube.com/results?search_query=%E5%8E%86%E5%8F%B2'
requestData(url)
