import urllib.request as req  #爬虫常用的包，用于访问网页并获得其中内容
import re  #正则表达式的使用包，用于实现正则表达式书写
import datetime  #关于时间的包，通常用于获取时间相关的内容

# import io
# import sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb2312')
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

url_ytb_s = 'https://www.youtube.com/feed/subscriptions'

cookie_youtube = 'APISID=08pQtyBJUwqu7asv/A1YdKNnP4c-LzIglG;' \
                 'CONSENT=YES+CN.zh-CN+20170813-09-1;' \
                 'HSID=ArNjTDZ4DW3-duwpD;' \
                 'LOGIN_INFO=AFmmF2swRQIgYtrv-ph4o3QnULfpTUetmqOCC-WEOT6a3GR-r4jFUycCIQDJ-4fpb6g6Iqrv9cPKgLmbIz8K3rR3vooN2TNXCMHZHA:QUQ3MjNmekVoMVhFVW5YWGpOeEJFejIxYjByQ2xqMFRSVGthREJ6LVVoQjBNT2FUVng2cV96VUhwd0g0VlNSZFU0aHpTdHA2bUd4Q1JST0pwMkZYcklEUWJWYlRXaWduRGlneTNOX0h6c2dEU29pMDFqcHZvZHZXUDRURHZmb0NsOE1ZckdkbGR2UlVVRmJrUHBzbTFXdk9RYi01YXdLRXFiTHlFR1dhNHNQbEluN3ExUUlqbThZ;' \
                 'PREF=f1=50000000&al=zh-CN;' \
                 'SAPISID=4g9YstiqqkcAtARd/A2kSQFDk6sCJ_N4dk;' \
                 'SID=SgZ3TrvX0tuz1IgxhrY3EgD5KanguFlz5_fzzK7GTNmzM0uoxIcyp2xX4wpW5RnUarknUA.;' \
                 'SSID=A6G-g9j6cnQUBNLJd;' \
                 'ST-1tzw2b8=itct=CCQQtSwYAiITCLKktsOAwtwCFQsOKgodVxML2TIKZy1wZXJzb25hbA%3D%3D&csn=Z31cW8ecJtqioQPHx6uADg;' \
                 'VISITOR_INFO1_LIVE=xBfJyY4sUN0;' \
                 'YSC=zpD1N6BAjx4;'
header = {'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
          'Connection': ' keep-alive',
          'Cookie':cookie_youtube}

request_ytb = req.Request(url=url_ytb_s,headers=header)
response_ytb = req.urlopen(request_ytb)

html = response_ytb.read().decode('utf8')

# print(html)

ytb_name_pattern = re.compile(r'},\"title\":{\"accessibility\":{\"accessibilityData\":{"label\":\"(.*?)来自')
ytb_address_patter = re.compile(r'\"url\":\"/watch\?v=(.*?)\",\"webPageType\":\"WEB_PAGE_TYPE_WATCH\"}},\"watchEndpoint\":{\"videoId\":\"')

result_name = re.findall(ytb_name_pattern,html)
result_address = re.findall(ytb_address_patter,html)

today = datetime.datetime.now()
file_name = str(today.year)+'-'+str(today.month)+'-'+str(today.day)
print(file_name)

# for name in result_name:
#     print(name)
# print(len(result_address))
# for adr in result_address:
#     print(adr)

file_adr = 'F:\\work_log\\'+file_name+'.txt'

log_point = 0

fr = open(file_adr,'w')
while log_point<len(result_name):
    # fr.writelines('https://www.youtube.com/watch?v='+result_address[log_point])
    # fr.writelines('#北京搬运#'+result_name[log_point])
    # fr.writelines('#北京搬运#' + result_name[log_point].encode('utf-8'))

    print('https://www.youtube.com/watch?v='+result_address[log_point])
    print('#北京搬运#' + result_name[log_point], '\n',log_point+1,'\n')
    # print(log_point)
    log_point += 1

fr.close()