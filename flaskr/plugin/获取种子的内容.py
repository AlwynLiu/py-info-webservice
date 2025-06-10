from aria2p import API, Client

def download_from_magnet(magnet_link, download_path):
    # 创建aria2客户端
    client = Client(host="127.0.0.1", port=6800, secret="")
    api = API(client)

    # 添加磁力链接
    download = api.add_magnet(magnet_link, options={"dir": download_path})

    print(f"开始下载：{download.name}")
    print(f"下载路径：{download_path}")

# 示例用法
magnet_link = "magnet:?xt=urn:btih:01a3ba472d25d205e7a460d5341f5eebcb567ead"  # 替换为你的磁力链接
download_path = "D:/磁力下载"  # 替换为你的下载路径
download_from_magnet(magnet_link, download_path)