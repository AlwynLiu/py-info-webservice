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
#         url = '''https://e1v-h.phncdn.com/hls/videos/202004/14/303677802/,201211_1807_1080P_4000K,201211_1807_720P_4000K,201211_1807_480P_2000K,240P_400K,_303677802.mp4.urlset/seg-{}-f2-v1-a1.ts?validfrom=1617876085&validto=1617883285&ip=47.241.56.235&hdl=-1&hash=aGYAQ%2B1%2BP1TQM%2By4h0cwsJZ%2B03A%3D'''.format(i)
#         f = open('./1.ts', 'wb')
#         result = requests.get(url)
#         print(result.content)
#         f.write(result.content)
#         f.close()


# url = 'https://www.pornhub.com/video?o=ht'
# requestData(url)

popular_women()
# download_video()