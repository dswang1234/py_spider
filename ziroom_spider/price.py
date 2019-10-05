import requests
from bs4 import BeautifulSoup
import image_test
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

li = ['-0','-21.4','-42.8','-64.2','-85.6','-107','-128.4','-149.8','-171.2','-192.6']
#
def gethtml(url):
    r = requests.get(url,headers=headers)
    r.raise_for_status()
    r.encoding = 'utf-8'
    return r.text
#
def get_price(url_now):
    print('访问延迟1秒')
    time.sleep(1)
    res2 = gethtml(url_now)
    soup2 = BeautifulSoup(res2, "lxml")

    # 获取图片地址
    url = soup2.find('div', attrs={"class": "info-box"}).find('span', attrs={"class": "num"})
    # 每一页的图片地址
    img_url = 'http:' + str(url).split('(')[1].split(')')[0]


    if image_test.load_img(img_url) == False:
    # 判断图片识别是否有效，无效则返回False
        return False
    else:
        print('http:' + str(url).split('(')[1].split(')')[0])

        # 当前页面的所有租房价格
        all_price = soup2.find_all('div', attrs={"class": "info-box"})

        real_all_price = []
        text = image_test.load_img(img_url)

        for i in all_price:
            stry = i.find_all('span', attrs={"class": "num"})
            p_e = ''
            for j in stry:
                num = str(j).split('position: ')[1].split('px')[0]
                p_e += str(text[li.index(num)])

            real_all_price.append(p_e)

        return real_all_price

# print(get_price('http://sh.ziroom.com/z/z1-p2/'))