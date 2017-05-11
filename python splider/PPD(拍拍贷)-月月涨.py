import requests
import random
import csv
from bs4 import BeautifulSoup
from heapq import merge
import time
import re
import csv
import json
from urllib.error import HTTPError, URLError

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]

Header = {
    'User-Agent': random.choice(USER_AGENTS),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate',
}

# 定义获取标准url


def get_req(url):  # 获取标准url的返回
    try:
        req = requests.get(url, headers=Header, timeout=10)
    except requests.Timeout as Timeerror:
        # print('time out error')
        return None
    except requests.RequestException as othererror:
        # print('other erroe happens')
        return None
    return req


# # 获取数据
# with open('F:\P2P行业企业分析\拍拍贷\月月涨.csv', 'r') as f:
#     csv_writer = csv.writer(f, 'excel')
#     csv_writer.writerow(['序号', '用户名', '投资额', '投资时间'])
#     for product_id in range(1, 41):
#         k = 0
#         for page in range(1, 800):
#             if k == 1:
#                 break
#             else:
#                 values = (page, product_id)
#                 print('now download is %i,%s' % values)
#                 url = 'http://rise.invest.ppdai.com/Product/InvestListPartial?page=%i&productID=%s' % values
#                 req = get_req(url)
#                 if req:
#                     bsobj = BeautifulSoup(req.text, 'html.parser')
#                     n_list = bsobj.find_all('tr')
#                     b_list = []
#                     for n in n_list:
#                         if n.get_text() == '暂无购买信息':
#                             k = 1
#                             break
#                         else:
#                             ar = [i for i in n.get_text().split('\n')[1:-1]]
#                             csv_writer.writerow(ar)
#                 else:
#                     csv_writer.writerow(['this error %i, %s' % values])
#                 time.sleep(random.uniform(1, 3))

# 提取和重新下载上次发生错误的数据
# with open('F:\P2P行业企业分析\拍拍贷\月月涨.csv', 'r') as f:
#     inverest_list = csv.reader(f)
#     error_list = []
#     for i in inverest_list:
#         # print(i)
#         if i.count("") == 3:
#
#             # print(i)
#             # print(i[0][:4])
#             if i[0][:4] == 'this':
#                 error_list.append(i[0][10:])
#     print(error_list, len(error_list))

error_list = [' 63, 5', ' 118, 5', ' 186, 5', ' 7, 6', ' 12, 6', ' 19, 6', ' 40, 6', ' 179, 6', ' 188, 6', ' 191, 6', ' 236, 6', ' 237, 6', ' 254, 6', ' 268, 6', ' 269, 6', ' 270, 6', ' 280, 6', ' 76, 7', ' 90, 7', ' 157, 7', ' 169, 7', ' 186, 7', ' 235, 7', ' 236, 7', ' 243, 7', ' 264, 7', ' 279, 7', ' 290, 7', ' 291, 7', ' 292, 7', ' 293, 7', ' 297, 7', ' 300, 7', ' 301, 7', ' 302, 7', ' 5, 8', ' 54, 8', ' 147, 8', ' 148, 8', ' 152, 8', ' 153, 8', ' 186, 8', ' 188, 8', ' 232, 8', ' 309, 8', ' 25, 9', ' 107, 9', ' 116, 9', ' 161, 9', ' 193, 9', ' 295, 9', ' 296, 9', ' 297, 9', ' 1, 10', ' 13, 10', ' 42, 10', ' 89, 10', ' 108, 10', ' 112, 10', ' 117, 10', ' 142, 10', ' 166, 10', ' 180, 10', ' 181, 10', ' 182, 10', ' 183, 10', ' 185, 10', ' 186, 10', ' 187, 10', ' 56, 11', ' 57, 11', ' 58, 11', ' 59, 11', ' 61, 11', ' 75, 11', ' 138, 11', ' 165, 11', ' 257, 11', ' 258, 11', ' 259, 11', ' 1, 12', ' 2, 12', ' 3, 12', ' 4, 12', ' 42, 12', ' 43, 12', ' 44, 12', ' 45, 12', ' 115, 12', ' 116, 12', ' 117, 12', ' 184, 12', ' 207, 12', ' 71, 13', ' 92, 13', ' 111, 13', ' 113, 13', ' 115, 13', ' 126, 13', ' 127, 13', ' 128, 13', ' 129, 13', ' 138, 13', ' 140, 13', ' 152, 13', ' 153, 13', ' 154, 13', ' 155, 13', ' 175, 13', ' 176, 13', ' 68, 14', ' 70, 14', ' 84, 14', ' 103, 14', ' 44, 15', ' 45, 15', ' 46, 15', ' 89, 15', ' 90, 15', ' 91, 15', ' 144, 15', ' 193, 15', ' 30, 16', ' 72, 16', ' 117, 16', ' 124, 16', ' 5, 17', ' 6, 17', ' 7, 17', ' 8, 17', ' 85, 17', ' 99, 17', ' 121, 17', ' 164, 17', ' 48, 18', ' 112, 18', ' 113, 18', ' 140, 18', ' 141, 18', ' 142, 18', ' 22, 19', ' 26, 19', ' 60, 19', ' 73, 19', ' 114, 19', ' 15, 20', ' 16, 20', ' 84, 20', ' 88, 20', ' 106, 20', ' 116, 20', ' 13, 21', ' 16, 21', ' 17, 21', ' 18, 21', ' 19, 21', ' 28, 21', ' 45, 21', ' 50, 21', ' 67, 21', ' 68, 21', ' 69, 21', ' 70, 21', ' 150, 21', ' 165, 21', ' 185, 21', ' 186, 21', ' 187, 21', ' 1, 22', ' 2, 22', ' 3, 22', ' 4, 22', ' 5, 22', ' 17, 22', ' 18, 22', ' 19, 22', ' 20, 22', ' 32, 22', ' 40, 22', ' 62, 22', ' 64, 22', ' 86, 22', ' 98, 22', ' 100, 22', ' 163, 22', ' 164, 22', ' 165, 22', ' 166, 22', ' 167, 22', ' 67, 23', ' 42, 24', ' 103, 24', ' 74, 25', ' 75, 25', ' 76, 25', ' 77, 25', ' 185, 25', ' 5, 26', ' 110, 26', ' 114, 26', ' 126, 27', ' 246, 27', ' 59, 28', ' 217, 28', ' 20, 29', ' 173, 29', ' 49, 30', ' 68, 31', ' 199, 31', ' 200, 31', ' 201, 31', ' 212, 31', ' 213, 31', ' 218, 31', ' 331, 33', ' 373, 33']
with open('F:\P2P行业企业分析\拍拍贷\月月涨_error.csv', 'w') as f:
    csv_writer = csv.writer(f, 'excel')
    csv_writer.writerow(['序号', '用户名', '投资额', '投资时间'])
    for values in error_list:
        values = (str.strip(values[:values.find(',')]), str.strip(values[values.find(',') + 1:]))

        url = 'http://rise.invest.ppdai.com/Product/InvestListPartial?page=%s&productID=%s' % values
        print('now download is %s,%s' % values)
        req = get_req(url)
        if req:
            bsobj = BeautifulSoup(req.text, 'html.parser')
            n_list = bsobj.find_all('tr')
            b_list = []
            for n in n_list:
                if n.get_text() == '暂无购买信息':
                    k = 1
                    break
                else:
                    ar = [i for i in n.get_text().split('\n')[1:-1]]
                    ar.append(values)
                    csv_writer.writerow(ar)
        else:
            csv_writer.writerow(['this error %s, %s' % values])
        time.sleep(random.uniform(1, 3))


# 更新数据

