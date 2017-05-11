import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError
import json
import random
import csv
import time
import re


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


def page_max(invest_product_url):  # 获取投资产品最大页
    try:
        req = requests.get(invest_product_url, headers=Header)
    except (HTTPError, URLError) as e:
        return None
    try:
        soup = BeautifulSoup(req.text, 'html.parser')
        page_list = soup.find_all('li', 'disabled')
        page_max = page_list[0].get_text()[-5:-1]
    except AttributeError as e:
        return None
    page_max = page_list[0].get_text()[-5:-1]
    return page_max


def get_req(url, page_num):  # 获取标准url的返回
    try:
        req = requests.get(url % str(page_num), headers=Header)
    except(HTTPError, URLError) as e:
        return None
    return req


def clean_content(content):  # 定义正则清洗函数
    content = re.sub(" ", '', content)
    content = re.sub("\t+", "", content)
    content = re.sub("\n+", "\n", content)
    return content


def get_product_list(page_max):  # 获取最开始产品信息列表
    f = open('F:\学习\新新贷\产品_test.csv', 'a+')
    result = []
    try:
        csv_write = csv.writer(f, 'excel')
        csv_write.writerow(['产品名称', '投标额', '投资人数', '收益', '期限', '状态', '操作',  '标的链接'])
        url = 'http://www.xinxindai.com/xplan/search/list-0-%s.html'
        for i in range(1, int(page_max)+1):
            req = get_req(url=url, page_num=i)
            if req is None:
                print('page is %d ,it is happen error' % i)
                time.sleep(100)  # 如果发生错误，等待100秒重新连接
                next(i)
            else:
                print('now download page num is %d' % i)
                soup = BeautifulSoup(req.text, 'html.parser')
                product_list = soup.find(id='planList')
                a_list = product_list.find_all('tr')
                for a in a_list:
                    ar = [row for row in clean_content(a.get_text()).split('\n')][1:-1]
                    if ar[5] == '锁定期' or ar[5] == '退出':
                        ar.append(a.find('a').get('href'))
                        csv_write.writerow(ar)
                        result.append(ar)
            time.sleep(random.uniform(1, 3))
    finally:
        f.close
    return result
# 测试成功
# page_max = 2
# a_list = get_product_list(2)
# for a in a_list:
#     print(a)
url = 'http://www.xinxindai.com/xplan/search/list.html'
page_max = page_max(url)
get_product_list(page_max)


def had_already_max_product(path):  # 定义获取已有的产品ID
    try:
        f = open(path, 'r')
        have_product_list = []
        product_list = csv.reader(f)
        header = next(product_list)
        for i in product_list:
            have_product_list.append(i[7][14:27])
        have_max_product_id = max(have_product_list)
    finally:
        f.close()
    return have_max_product_id


def update_product_list(page_max, had_already_max_product):  # 更新产品列表，传入最大页面和已有的最大产品ID
    f = open('F:\学习\新新贷\产品.csv', 'a+')
    k = 0
    try:
        csv_write = csv.writer(f, 'excel')
        url = 'http://www.xinxindai.com/xplan/search/list-0-%s.html'
        result = []
        for i in range(1, int(page_max) + 1):
            req = get_req(url=url, page_num=i)
            if req is None:
                print('page is %d ,it is happen error' % i)
                time.sleep(100)  # 如果发生错误，等待100秒重新连接
                next(i)
            elif k == 1:
                break
            else:
                print('now download page num is %d' % i)
                soup = BeautifulSoup(req.text, 'html.parser')
                product_list = soup.find(id='planList')
                a_list = product_list.find_all('tr')
                for a in a_list:
                    ar = [row for row in clean_content(a.get_text()).split('\n')][1:-1]
                    if ar[5] == '锁定期':
                        if ar[7][14:27] == had_already_max_product:
                            k = 1
                            break
                        else:
                            ar.append(a.find('a').get('href'))
                            csv_write.writerow(ar)
                            result.append(ar)
            time.sleep(random.uniform(1, 3))
    finally:
        f.close()


def get_invest_list(product_link_list):  # 传入空的invest_list和product_link_list
    invest_list = []
    for i in product_link_list:
        product_id = i[7][14:27]
        print('now download product id is %s' % product_id)
        url = 'http://www.xinxindai.com/xplan/userSchemeList.html?schemeId=%s&currentPage=1&queryType=join&pageSize=1000' % product_id
        try:
            req = requests.get(url, headers=Header)
            JsonObject = json.loads(req.text)
            for j in range(0, len(JsonObject.get('resultList'))):
                invest_list.append(JsonObject.get('resultList')[j])
        except(HTTPError, URLError) as e:
            print('this %s happen error' % product_id)
            return None
        time.sleep(random.uniform(1, 2))
    return invest_list


def get_new_product_id(product_list_path, inverst_list_path):  # 通过读取两个文件，去除已经爬取的投资信息，获取新增产品列表
    b = []
    a = []
    f_product = open(product_list_path, 'r')
    f_inverst = open(inverst_list_path, 'r')
    try:
        product_list = csv.reader(f_product)
        inversr_list = csv.reader(f_inverst)
        heard_product = next(product_list)
        heard_inverst = next(inversr_list)
        for i in product_list:
            if i:
                b.append(i[7][14:27])
                # print(i[7][14:27])

        for j in inversr_list:
            if j:
                c = re.sub('\'', '"', j[0])
                jsObject = json.loads(c)
                # print(jsObject['SCHEMEID'])
                a.append(jsObject['SCHEMEID'])
        c = list(set(a))
        for j in c:  # 从b中移除c
            b.remove(j)
    finally:
        f_product.close()
        f_inverst.close()
    return b

# product_list_path = 'F:\学习\新新贷\产品_test.csv'
# inverst_list_path = 'F:\学习\新新贷\inverst_list2（已经处理完成的）.csv'
# b = get_new_product_id(product_list_path, inverst_list_path)
# for j in b:
#     print(j)
# # print(b)


def get_add_invest_list(new_product_link_list):  # 获取新增产品列表，并把新增产品列表写入文件
    invest_list = []
    f = open('F:\学习\新新贷\inverst_list2（已经处理完成的）.csv', 'a+')
    csv_writer = csv.writer(f, 'excel')
    try:
        for i in new_product_link_list:
            print('now download product id is %s' % i)
            url = 'http://www.xinxindai.com/xplan/userSchemeList.html?schemeId=%s&currentPage=1&queryType=join&pageSize=1000' % i
            try:
                req = requests.get(url, headers=Header)
                JsonObject = json.loads(req.text)
                for j in range(0, len(JsonObject.get('resultList'))):
                    invest_list.append(JsonObject.get('resultList')[j])
                    csv_writer.writerow([JsonObject.get('resultList')[j]])
            except(HTTPError, URLError) as e:
                print('this %s happen error' % i)
                return None
            time.sleep(random.uniform(1, 2))
    finally:
        f.close()
    return invest_list


# # 测试语句，测试成功
# get_new_product_id = ['OS20170123280', 'OS20170122279']
# print(get_add_invest_list(new_product_link_list=get_new_product_id))


# 对下载下来的投资数据进行解析
# f = open('F:\学习\新新贷\inverst_list2（已经处理完成的）.csv', 'r')
# f2 = open("F:\学习\新新贷\inverst(处理数据).csv", 'w')
# headers_list = ['ADDIP', 'EXPECTEDINTEREST',  'ACCOUNT',  'CHANNEL',  'USERNAME', 'NICKNAME',
#                 'SCHEMEID',  'ADDTIME',  'COLLECTIONTYPE',  'OPENDATE']
# pattern = re.compile("\D*1{1}\d{10}\w*")
# try:
#     inverst_list = csv.reader(f)
#     headers = next(inverst_list)
#     csv_writer = csv.writer(f2, 'excel')
#     csv_writer.writerow(['IP', '收益', '金额', '渠道', '用户名', '打码用户名', '产品ID',
#                         '添加时间', '收集类型', '打开时间', '联系方式'])
#     # print(type(inverst_list))
#
#     j = 1
#     for i in inverst_list:
#         a = re.sub('\'', '\"', i[0])
#         b = json.loads(a)
#         # print(a)
#         # print(type(a))
#         result = re.match(pattern, b.get(headers_list[4]))
#         c_list = []
#         if result:
#             d = re.sub('\D', "", b.get(headers_list[4]))
#             print(d)
#             # j = 1
#             for h in range(0, len(headers_list)):
#                 # print(h)
#                 # print(b.get(headers_list[h]))
#                 c_list.append(b.get(headers_list[h]))
#
#             c_list.append(d)
#             csv_writer.writerow(c_list)
#             # print(c_list)
#             # print('now deal with:%d' % j)
#             # j += 1
#             # if j == 10:
#             #     exit()
#         # c_list = [b.get(headers_list[0], b.get(headers_list[1]), b.get())]
#
# finally:
#     f.close()
#     f2.close()





