import requests


def requestData(url):
    result = requests.get(url, )
    print(result.text)


url = 'https://www.youtube.com/results?search_query=%E5%8E%86%E5%8F%B2'
requestData(url)
