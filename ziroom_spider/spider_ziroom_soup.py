import requests
from bs4 import BeautifulSoup
from tqdm import *
import csv
from time import sleep
import price

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

def gethtml(url):
    r = requests.get(url,headers=headers)
    r.raise_for_status()
    r.encoding = 'utf-8'
    return r.text

'''-------------------------------------------爬取池提取-------------------------------------------'''

#爬取池url_pool
url_pool = []
url_pool_price = []


for i in trange(1,51):
    print('第'+str(i)+'轮....')
    str_url = "http://sh.ziroom.com/z/z1-p"+str(i)+"/"
    # 获取网页源代码
    res = gethtml(str_url)
    sleep(1)
    # 使用lxml的方式解析
    soup = BeautifulSoup(res,"lxml")
    # 找到所有此页面的具体租房的链接板块
    ziroom_url = soup.find_all(attrs={"class":"info-box"})

    now_all_price = []
    if price.get_price(str_url) == False:
        print('价格图片识别出错...跳过该轮...')
        continue
    else:
        now_all_price = price.get_price(str_url)
        print(now_all_price)
        if now_all_price == False:
            print('出错...跳过该轮...')
            continue
        else:
            # 获取网页租房名称以及链接
            for j in ziroom_url:
                ziroom_one_url = 'http:' + j.find('a').get("href")
                url_pool.append(str(ziroom_one_url))

            for j in now_all_price:
                url_pool_price.append(j)


print(len(url_pool),len(url_pool_price))



'''-------------------------单个页面提取以及相关文件的写入----------------------'''

# 打开csv文件的写入口
out = open('stu.csv', 'a', newline='')
csv_write = csv.writer(out, dialect='excel')

head = ['租房名称','面积','朝向','户型','楼层比例','位置','小区年代','价格']
csv_write.writerow(head)

# 单个页面的提取
for i in trange(len(url_pool)):
    sleep(1)
    single_info = []
    res2 = gethtml(url_pool[i])
    soup2 = BeautifulSoup(res2,"lxml")

    print('租房名称')
    ziroom_one_name = str(soup2.find(attrs={"class":"Z_name"})).split('i>')[1].split('<')[0]
    print(ziroom_one_name)
    single_info.append(ziroom_one_name)

    print('租房信息：面积，朝向，户型')
    ziroom_one_info = soup2.find_all('dd')

    for j in range(1, 4):
        str_i = str(ziroom_one_info[-j])[4:][:-5]
        print(str(ziroom_one_info[-j])[4:][:-5])
        single_info.append(str_i)

    print('楼层比例')
    ziroom_one_info_va = str(soup2.find_all(attrs={"class": "va"})[1])[17:][:-7]
    print(ziroom_one_info_va)
    single_info.append(ziroom_one_info_va)

    print('位置')
    ziroom_one_location = str(soup2.find('span',attrs={"class":"ad"})).split('>')[1].split('<')[0]
    print(ziroom_one_location)
    single_info.append(ziroom_one_location)

    print('小区年代')
    ziroom_one_found = str(soup2.find('span', attrs={"class": "value"})).split('>')[1].split('<')[0]
    print(ziroom_one_found)
    single_info.append(ziroom_one_found)

    print('价格')
    ziroom_one_price = url_pool_price[i]
    print(ziroom_one_price)
    single_info.append(ziroom_one_price)

    csv_write.writerow(single_info)

    print('第'+str(i)+'个信息写入完毕')

out.close()
print('爬取完成')