import requests


def requestData(url):
    result = requests.get(url, )
    print(result.text)


url = 'http://www.xbiquge.la/44/44391/19673679.html'
requestData(url)