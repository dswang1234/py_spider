# 因变量：租金价格
# 变量：户型、面积、朝向、楼层比例、距离地铁站步行距离、区域内三甲医院、商超数量

import time


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

from time import sleep

import os,time
from tqdm import *
import csv

# option = webdriver.ChromeOptions()
# option.add_argument('--headless')
# driver = webdriver.Chrome(chrome_options=option)
# driver.get('http://sh.ziroom.com/z/z1-p2/')
# # driver.get('http://sh.ziroom.com/x/787286905.html')
# # print(driver.get_cookies())
# cookie = {'domain': '.ziroom.com',
#            'httpOnly': False,
#            'name': 'Hm_lpvt_4f083817a81bcb8eed537963fc1bbf10',
#            'path': '/',
#            'secure': False,
#            'value': '1570022163'}
#
# driver.add_cookie(cookie)
#
# print(driver.find_element_by_xpath('/html/body/section/div[3]/div[2]/div[1]/div[2]/h5/a').get_attribute('href'))
# print(driver.find_element_by_xpath('/html/body/section/div[3]/div[2]/div[]/div[2]/h5/a'))
#
# url_pool = []
#
# out = open('ziroom.csv','a',newline='')
# csv_write = csv.writer(out,dialect='excel')
#
# for i in trange(1,30):
#     # cookie = {'domain': '.ziroom.com',
#     #            'httpOnly': False,
#     #            'name': 'Hm_lpvt_4f083817a81bcb8eed537963fc1bbf10',
#     #            'path': '/',
#     #            'secure': False,
#     #            'value': '1570022163'}
#
#     url = 'http://sh.ziroom.com/z/z1-p'+str(i)+'/'
#     # print(url)
#     option = webdriver.ChromeOptions()
#     option.add_argument('--headless')
#     driver = webdriver.Chrome(chrome_options=option)
#     # driver.add_cookie(cookie)
#     driver.get(url)
#     for i in range(1,51):
#         if len(url_pool)<501:
#             sleep(2)
#             xpa = '/html/body/section/div[3]/div[2]/div[' + str(i) + ']/div[2]/h5/a'
#             try:
#                 url_part = str(driver.find_element_by_xpath(xpa).get_attribute('href'))
#                 url_name = str(driver.find_element_by_xpath(xpa).text)
#                 if url_name == '':
#                     continue
#                 else:
#                     print(url_part, url_name)
#                     url_pool.append(url_part)
#             except NoSuchElementException:
#                 continue
#         else:
#             break
# print('获取网址完毕....')
# print(url_pool)

# for i in url_pool:
#     option = webdriver.ChromeOptions()
#     option.add_argument('--headless')
#     driver = webdriver.Chrome(chrome_options=option)
#     driver.get(i)

option2 = webdriver.ChromeOptions()
option2.add_argument('--headless')
driver2 = webdriver.Chrome(chrome_options=option2)
driver2.get('http://sh.ziroom.com/x/791814865.html')
print(driver2.find_element_by_xpath('/html/body/section/aside/div[3]/div[1]/dl[1]/dd').text)
print(driver2.find_element_by_xpath('/html/body/section/aside/div[3]/div[1]/dl[2]/dd').text)
print(driver2.find_element_by_xpath('/html/body/section/aside/div[3]/ul/li[2]/span[2]').text)
print(driver2.find_element_by_xpath('/html/body/section/aside/div[3]/div[1]/dl[3]/dd').text)

