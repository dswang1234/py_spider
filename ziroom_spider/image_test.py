url2 = 'http://static8.ziroom.com/phoenix/pc/images/price/new-list/dff9d441e1fc59f793d5c3b68461b3ea.png'

import tesserocr
import requests
from PIL import Image
import os
import time

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
cookie = "CURRENT_CITY_CODE=310000; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216d8c41c1da261-033babedfa65a2-67e1b3f-2073600-16d8c41c1db34a%22%2C%22%24device_id%22%3A%2216d8c41c1da261-033babedfa65a2-67e1b3f-2073600-16d8c41c1db34a%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; gr_user_id=d56b5694-765d-4a76-b03f-1aab146e85d2; _csrf=8KzW2-TTTdZLLKidrdDGJPhgW8Ruo5uM; Hm_lvt_4f083817a81bcb8eed537963fc1bbf10=1570016183,1570022086; PHPSESSID=eun9q53l1n71ukqp7jk88cdbo4; PHPSESSID=2l19a24ske0maagi6maq3l4jt0; visitHistory=%5B718772701%2C791637840%2C791814865%2C787286905%2C739322636%2C791759866%5D; gr_session_id_8da2730aaedd7628=916ee3c1-b69e-432a-89d2-716249d3e862; gr_session_id_8da2730aaedd7628_916ee3c1-b69e-432a-89d2-716249d3e862=true; passport_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiI4NjQ0NjE4MC0wNWIzLTRkZjQtYjJiOS1kYjU0NmM1MTgzMjIiLCJ0eXBlIjoyLCJsZW5ndGgiOjEyMCwidG9rZW4iOiIwNzIwYjBjMi0xZWUzLTRlZDktYjQ4NC01NDVlMjhlYzBhNmEiLCJjcmVhdGVUaW1lIjoxNTcwMDkyNDY2NzE1fQ.DB0MBM0fZn-x9CmLa76-ajm4zL2gRW3AuVeItQ6cuE4; Hm_lpvt_4f083817a81bcb8eed537963fc1bbf10=1570092467"
accept = "application/json, text/plain, */*"
accept_language = "Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"

headers = {
    'User-Agent':user_agent,
    'Accept':accept,
    'Accept-Language':accept_language,
    'Cookie':cookie
}

def load_img(url):
    print('识别图片延迟1秒')
    time.sleep(1)
    response = requests.get(url,headers=headers)
    # 获取的文本实际上是图片的二进制文本
    img = response.content
    # 将他拷贝到本地文件 w 写  b 二进制  wb代表写入二进制文本
    # 保存路径
    path = 'D:\\pycharm-project\\ziroom_spider\\1.png'
    with open(path, 'wb') as f:
        f.write(img)

    image = Image.open('D:\\pycharm-project\\ziroom_spider\\1.png')  # 识别照片

    result = tesserocr.image_to_text(image)

    if '1' not in result and '2' not in result:
            return False

    else:
        os.remove(path)

        a = list(result)[:-1]

        for i in range(10):
            if str(i) not in a:
                a.insert(0, str(i))

        b = []

        for i in a:
            b.append(int(i))

        return b  # 返回识别的图片内容

# print(load_img(url2))