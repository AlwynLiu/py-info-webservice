import requests

def fetch():
    url = 'https://ecp-test.bgyfw.com:8030/ecp/api/meterex/getMeterByProId?AccessToken=48D9182498E2208BD1C8A42A393DF1E1'
    data = requests.post(url).json()
    print(data)

fetch()
