# from bs4 import BeautifulSoup
# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link2">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
# """
# soup = BeautifulSoup(html_doc, 'html.parser')
# # print(soup.prettify())
# # test1 = soup.find_all("a")
# # for i in test1:
# #     print(i.get('href'))
#
# test2 = soup.find_all(id='link2')
# for j in test2:
#     print(j.get('href'))
#
# tag = soup.p
# print(type(tag))
# print(soup.strings)
#
# # a_list = [1, 2, 4]
# a_list=[]
# a_list.append(3)
# print(a_list)
# # #
# import csv
# csFile = open('F:\学习\新新贷\新元宝_product_url.csv', 'w')
# try:
#     csv_writer = csv.writer(csFile, 'excel')
#     csv_writer.writerow(['新元宝'])
#     a_list = ['jiang', 'shao', 'bing']
#     for i in a_list:
#         print(i)
#         csv_writer.writerow([i])
# finally:
#     csFile.close()

#
# a = '/xplan/detail/OS20170106205.html'
# print(a.find('O'))
# print(a.rfind('/'))

# print(a[14:])
# import csv
# f = open("F:\学习\新新贷\新元宝_product_url.csv", 'r')
# try:
#     product_id_list = csv.reader(f)
#     headers = next(product_id_list)
#     for product_id in product_id_list:
#         print(product_id[0])
#         print(product_id[0][14:27])
# finally:
#     f.close()

# # a = [1, 2, 3]
#
# a = '/xplan/detail/OS20150108017.html'
# print(a.rfind('/'))
# print(a.rfind('.'))
import requests
# import json
# import csv
# # from bs4 import BeautifulSoup
# #
# url1 = 'http://www.phperz.com/special/46.html'
# url2 = 'http://www.xinxindai.com'
# url = 'http://www.xinxindai.com/xplan/userSchemeList.html?schemeId=OS20161217110&currentPage=1&queryType=join&pageSize=1000'
# req = requests.get(url)
# print(req)
# inverst_list = []
# # soup = BeautifulSoup(req.text, 'html.parser')
# jsonObject = json.loads(req.text)
# # print(jsonObject)
# # print(jsonObject.get('resultList'))
# # print(len(jsonObject.get('resultList')))
# for i in range(0, len(jsonObject.get('resultList'))):
#     a = jsonObject.get('resultList')[i]
#     inverst_list.append(a)
# f2 = open('F:\学习\新新贷\csvtest.csv', 'w')
# try:
#     csv_writer = csv.writer(f2, 'excel')
#     csv_writer.writerow([inverst_list])
# finally:
#     f2.close()
# print(req.text)
# print(req.text.find(':'))
# print(req.text[14:])
# print(req.text[14:])
# print(type(req.text))
# print(req.text['resultList'])



# inverst_list = soup.find_all('ACCOUNT')
# for inverst in inverst_list:
#     print(inverst)
# print(dict(soup))
# print(type(soup))
# print()

# import csv
# shutdown = {"yunfeiyang":{"username":"yunfeiyang","binding_house":{0:"1",1:"2"},"register_time":"2018-20"}}
# f = open('F:\学习\新新贷\csvtest.csv', 'w')
# try:
#     csv_writer = csv.writer(f, 'excel')
#     csv_writer.writerow(['username', 'binding_hourse', 'register_time'])
#     list1 = []
#     print(shutdown.values())
#     for i in shutdown.values():
#         s = list(i.values())
#         print(s)
#         print(i)
#         list1.append(s)
#     csv_writer.writerow(list1)
# finally:
#     f.close()


# #  测试使用sqlalchemy
# from sqlalchemy import create_engine
# engine = create_engine('')
#
# import csv
# import json
# import re
#
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
# #
#
#         # print(b)
#         # print(type(a))
#
#
# finally:
#     f.close()
#     f2.close()
# #
# import json
# import re
# text = "{'data':123}"
# text = re.sub('\'', '\"', text)
# a_dict = json.loads(text)
# print(a_dict['data'])

# import re
# s = 'aa13684bb'
# pattern = re.compile("\D")
# c = re.sub(pattern, '', s)
# # print(len(s))
# # print(c)
# # c = filter(s.isdigit, s)
# # print(filter(s.isdigit, s))
# print(c)


#  测试去除空行没有成功，二进制转码问题
# import csv
# f = open('F:\学习\新新贷\新元宝_product_url2.csv', 'w')
# try:
#     csv_writer = csv.writer(f, 'excel')
#     csv_writer.writerow(['test'])
#     # page_max = 2
#     result = ['/xplan/detail/OS20170111226.html', '/xplan/detail/OS20170111225.html', '/xplan/detail/OS20170111224.html', '/xplan/detail/OS20170111223.html', '/xplan/detail/OS20170111222.html', '/xplan/detail/OS20170111221.html', '/xplan/detail/OS20170111220.html', '/xplan/detail/OS20170111219.html', '/xplan/detail/OS20170111218.html', '/xplan/detail/OS20170111217.html', '/xplan/detail/OS20170110216.html', '/xplan/detail/OS20170110215.html', '/xplan/detail/OS20170110214.html', '/xplan/detail/OS20170110213.html', '/xplan/detail/OS20170110212.html', '/xplan/detail/OS20170110211.html']
#     csv_writer.writerow(result)
# finally:
#     f.close()
#
# list = ['OS20170110211', 'OS20170110212']
# for product_id in list:
#     url = 'http://www.xinxindai.com/xplan/userSchemeList.html?schemeId=%s&currentPage=1&queryType=join&pageSize=1000' % product_id
#     print(url)


# # 测试如何跳出多层循环 ,成功
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# b = [1, 2, 3, 4, 5, 6, 7, 8]
# c = []
# for i in range(0, len(a)):
#     d = 0
#     for j in range(0, len(a)):
#         if b[j] == 6:
#             d = 1
#             break
#         else:
#             c.append(b[j])
#     if d == 1:
#         break
# print(c)

# import requests
# url = 'http://www.17jucai.com/a/invest/public/detail/2016092300001.html'
# req = requests.get(url)
# print(req.text)

# import csv
# f = open('F:\学习\新新贷\新元宝_product_url.csv', 'r')
# try:
#     product_list = []
#     a_list = csv.reader(f)
#     headers = next(a_list)
#     for i in a_list:
#         product_list.append(i[0][14:27])
#         # print(i[0][14:27])
#     print(max(product_list))
# finally:
#     f.close()

# test_list = ['OS20160531257', 'OS20160531256', 'OS20160531255', 'OS20160529254', 'OS20160529253', 'OS20160529252',
#              'OS20160528251', 'OS20160528250', 'OS20160528249']
# print(max(test_list))
# print(min(test_list))
# print(test_list.sort())


# 测试获取产品列表

import requests
from bs4 import BeautifulSoup
import re
import csv
# url = 'http://www.xinxindai.com/xplan/search/list-0-2.html'
# req = requests.get(url)
# Soup = BeautifulSoup(req.text, 'html.parser')
# product_list = Soup.find(id='planList')
# print(type(product_list))
# # soup2 = BeautifulSoup(product_list, 'html.parser')
# a_list = product_list.find_all('tr')
# f = open('F:\学习\新新贷\产品.csv', 'w')
# b_list = []
# try:
#     csv_write = csv.writer(f, 'excel')
#     csv_write.writerow(['产品名称', '投标额', '期限', '投资人数', '收益', '锁定期', '状态', '操作'])
#     for a in a_list:
#         # b = re.sub('\t*\s*', "", a.get_text())
#         # print(b)
#         b_list = [i for i in re.sub('\t*\s*', '', a.get_text())]
#         print(b_list)
#     # csv_write.writerow(b_list)
# finally:
#     f.close()


# #
# url = 'http://www.xinxindai.com/xplan/search/list-0-2.html'
# req = requests.get(url)
# Soup = BeautifulSoup(req.text, 'html.parser')
# product_list = Soup.find(id='planList')
# a_list = product_list.find_all('tr')
# f = open('F:\学习\新新贷\jiangshaobing.csv', 'w')
# try:
#     csv_write = csv.writer(f, 'excel')
#     csv_write.writerow(['产品名称', '投标额', '投资人数', '收益', '锁定期', '状态', '操作', '标的链接'])
#     # a_list = re.sub('\t*', '', product_list.get_text()).split('\n')
#     k = 0
#     for a in a_list:
#         # print(type(a))
#         # print(a.find('a').get('href'))
#         # if k == 1:
#         #     break
#         # else:
#         # print(a.get_text())
#         b = re.sub(' ', "", a.get_text())
#         c = re.sub('\t*', "", b)
#         # print(b)
#         # print(c)
#         ar = [row for row in re.sub('\n{2,8}', '\n', c).split('\n')][1:-1]
#         # ar1 = [row for row in a.get_text()][1:-1]
#         # ar1 = [row for row in re.sub('\s |\t', '', a.get_text()).split('\n')]
#         # ar2 = [row for row in re.sub('\s', "", a.get_text()).split('\n')]
#         # ar.remove('\t')
#         ar.append(a.find('a').get('href'))
#         # print(ar[9])
#         # print(ar.remove(''))
#         # b = a.get_text()
#         # c = re.sub(' ', '', b)
#         # replaceBR = re.compile('<br><br>|<br>')
#         # c = re.sub(' ', '', b)
#
#         # c = re.sub(replaceBR, '\n', b)
#         # ar2 = [row for row in c]
#         # print(c)
#         # print(a)
#         print(ar)
#
#         # print(ar1)
#         # print(ar2)
#         k = 1
#         # print(ar2)
#         # print(a.get_text())
#         csv_write.writerow(ar)
#
#     # for row in a_list:
#     #     print(row)
#     #     csv_write.writerow([row])
# #
# finally:
#     f.close()


# # 一堆问题，不太明白，明日在战
# a = 'abcadefg'
# b = re.sub('a', '', a)
# print(a)
# print(b)
#
# test_list = ['a', '', 'b']
# test_list.remove('')
# print(test_list)
# test_list2 = ['新元宝12个月-星期三活动标-12月期01', '1,000,000.00', '20', '11%', '', '', '12个月', '', '锁定期', '', '', '查看详情', '', '']
# test_list2.remove(" ''")
# print(test_list2)

# 获取最大值成功

# import csv
# test_list = []
# f = open('F:\学习\新新贷\产品.csv', 'r')
# product_list = csv.reader(f)
# header = next(product_list)
# for i in product_list:
#     test_list.append(i[15][14:27])
# print(max(test_list))
#     # print(i[15][14:27])

# import requests
# from bs4 import BeautifulSoup
#
#
# def ngrams(content, n):
#     content = content.split(' ')
#     output = []
#
#     # for i in range(len(content)-n+1):
#         # output.append(content[i, i+n])
#     return content
#
# url = 'http://en.wikipedia.org/wiki/Python_(programming_language)'
# req = requests.get(url)
# bsobj = BeautifulSoup(req.text, 'html.parser')
# content = bsobj.find('div', {'id': 'mw-content-text'}).get_text()
# ngram = ngrams(content, 2)
# # print(content)
# print(ngram)
# # # print()
# # print("2-grams count is: "+str(len(ngrams)))

# import requests
# from bs4 import BeautifulSoup
#
#
# def ngrams(input, n):
#     input = input.split(' ')
#     output = []
#     # return type(n)
#     for i in range(len(input)-n+1):
#         output.append(input[i:i+n])
#     return output
# url = 'http://en.wikipedia.org/wiki/Python_(programming_language)'
# req = requests.get(url)
# bsObj = BeautifulSoup(req.text, 'html.parser')
# content = bsObj.find("div", {"id": "mw-content-text"}).get_text()
# print(content)
# ngrams = ngrams(input=content, n=2)
# print(ngrams)
# print("2-grams count is: "+str(len(ngrams)))


# def test(content, n):
#     content = content.split(' ')
#     resutlt = []
#     for i in range(len(content)-n+1):
#         print(content[i:i+n])
#         resutlt.append(content[i:i+n])
#     return resutlt

# a = 'jaing shao bing'
# print(a.split(' '))

#
# a = '\n\n\n字段1\n\n \n\n\n\n\n\n\n\n\n\n\n\n字段2\n\n  \t \t字段3'
# partern = re.compile('\s*')
# a1 = re.sub('[\t ]', "", a)
# a2 = re.sub('\t', "", a)
# a3 = re.sub('\t* | *', "", a)
# print(a3)
# print(a1)
# b = re.sub('\n{2,}', '\n', a1)
# # print(b)
# print(a1)
# ar = [i for i in b.split('\n')]
# print(ar)
# print(ar[1:])
# # print(ar.remove(''))
#
# import requests
# from bs4 import BeautifulSoup
# import re
# import string
#
# #
# def clean_content(contens):
#     contens = re.sub('\n+', " ", contens)
#     contens = re.sub('\[[0-9]*\]', "", contens)
#     contens = re.sub(" +", ' ', contens)
#     result = []
#     contens = contens.split(' ')
#     for item in contens:
#         item = item.strip(string.punctuation)
#         if len(item) > 1 or (item.lower() == 'a' or item.lower == 'i'):
#             result.append(item)
#     return result
#
#
# def ngrams(contens, n):
#     result = []
#     contens = clean_content(contens)
#     for i in range(len(contens)-n+1):
#         result.append(contens[i:i+n])
#     return result
# url = 'http://en.wikipedia.org/wiki/Python_(programming_language)'
# req = requests.get(url)
# bsObj = BeautifulSoup(req.text, 'html.parser')
# content = bsObj.find("div", {"id": "mw-content-text"}).get_text()
# ngrams = ngrams(content, 3)
# # print(ngrams)
# # a_list = ngrams(content, 2)
# # for a in a_list:
# #     print(a)
# # for a in ngrams:
# #     print(a)
# # print("2-grams count is: "+str(len(ngrams)))
#
# a = '作为一名优秀的程序员，你可能会问：“为什么不自动地对输入的信息进行清洗，去掉非'
# print(ngrams(clean_content(a), 2))

# a = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~蒋少兵'
# print(a.strip(string.punctuation))


# import csv
# f = open('F:\学习\新新贷\产品.csv', 'r')
# have_product_list = []
# product_list = csv.reader(f)
# for a in product_list:
#     print(a)
# header = next(product_list)
# for i in product_list:
#     have_product_list.append(i[8][14:27])
# have_max_product_id = max(have_product_list)
# print(have_max_product_id)


# a = ['1', 2, 3]
# b = ['1', 2, 3, 4, 5]
# for i in a:
#     b.remove(i)
# print(b)

# import json
# import csv
# import re
# # f = open('F:\学习\新新贷\inverst_list2（已经处理完成的）.csv', 'r')
# try:
#     f = open('F:\学习\新新贷\产品.csv', 'r')
#     a_list = csv.reader(f)
#     head = next(a_list)
#
#     k = 0
#     b = []
#     for i in a_list:
#         # j = re.sub('\'', '"', i[0])
#         # jsobject = json.loads(j)
#         # # print(jsobject)
#         # a = jsobject['SCHEMEID']
#         print(i[7][14:27])
#
#         b.append(i[7][14:27])
#     print(b)
# finally:
#     f.close()



# import csv
# f = open("F:\学习\新新贷\产品_test.csv", 'r')
# try:
#     product_list = csv.reader(f)
#     heard = next(product_list)
#     for i in product_list:
#         if i:
#             print(i)
# finally:
#     f.close()

# student_tuples = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
# key1 = lambda student: student[2]
# for i in range(3):
#     print(key1(student_tuples[i][2]))
# print(sorted(student_tuples, key=key1))

# a = 'If you don\'t care about the type of the numbers you can simply use'
# a = a.split(" ")
# print(a)
# for i in range(len(a)-2+1):
#     b = " ".join(a[i:i+2])
#     print(b)
#     c = dict()
#     c[b] = 2
# print(c)
#
#
# def getNgrams(input, n):
#
#     output = dict()
#     for i in range(len(input)-n+1):
#         newNGram = " ".join(input[i:i+n])
#         if newNGram in output:
#             output[newNGram] += 1
#         else:
#             output[newNGram] = 1
#     return output

from collections import OrderedDict
import operator
# d = {1: 'z', 2: 'y', 3: 'x'}
# # a = sorted(d.items(), key=lambda x: x[1], reversed=True)
# c = OrderedDict(sorted(d.items(), key=lambda x: x[1], reversed=True))
# print(c)

# data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
# # standard_way = sorted(data, key=operator.itemgetter(1), reverse=True)
# standard_way = sorted(data, key=lambda x: x[1], reverse=True)
# print(standard_way)
# from collections import OrderedDict
# a = {'consider': 2, 'know': 1, 'proceed': 2, 'assure': 1, 'fear': 1, 'must': 1, 'appear': 1, 'have': 5, 'refer': 1, 'now': 1, 'give': 1, 'see': 1, 'shall': 5, 'too': 1, 'possess': 1, 'sincerely': 1, 'had': 1, 'conceive': 3, 'propose': 1, 'believe': 2, 'deem': 1, 'consent': 1, 'trust': 1, 'apprehend': 1, 'am': 1, 'should': 2, 'wish': 1, 'can': 3, 'may': 1}
# # one_key = lambda x: (x[1], x.isupper(), x.islower())
# b = sorted(a.items(), key=lambda x: (x[1]), reverse=True)
# # b = sorted(a.items(), key=one_key)
# c = OrderedDict(b)
#
# print(b)
#
# print(type(b))
# print(c)
# print(type(c))


# import requests
# import random
#
# USER_AGENTS = [
#     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#     "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
#     "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
#     "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
#     "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
#     "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
#     "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
#     "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
#     "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
#     "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
#     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
#     "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
#     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
#     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
#     "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
#     "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
#     "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
#     "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
#     "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
# ]
#
# Header = {
#     'User-Agent': random.choice(USER_AGENTS),
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Language': 'en-US,en;q=0.5',
#     'Connection': 'keep-alive',
#     'Accept-Encoding': 'gzip, deflate',
# }
#
#
# url = 'http://www.wdzj.com/dangan/'
# params = {'username': 'jiang', 'password': 'password'}
# req = requests.get(url, headers=Header)
# print(req)
# print('cookie is set to:')
# print(req.cookies.get_dict())
# print(req.cookies)
#
#
# for i in range(1, 182):
#     url = 'http://www.wdzj.com/front_select-plat?params=&sort=0&currPage=%i' % i
#     req = requests.get(url, headers=Header, cookies=req.cookies)
#     print('-----------')
#     print(req.text)
#
# a = b"\xba\xda\xc1\xfa\xbd\xad\xb9\xfe\xb6\xfb\xb1\xf5"
# print([ord(c) for c in a])
# # b = '上海|浦东'
# b = '\''
# c = b.encode('GBK', 'ignore')
#
# print(c)
# d = b'\xc9\xcf\xba\xa3|\xc6\xd6\xb6\xab'.decode('gbk')
# print(d)
# print(b'\xf0\x9f\x8c\x8e\xf0\x9f\x8c\x8f'.decode())
# print(b'\xc9\xcf\xba\xa3|\xc6\xd6\xb6\xab'.decode())

# def try_encode(string, encoding):
#     try:
#         # print(string.encode(encoding))
#         return string.encode(encoding)
#     except UnicodeEncodeError as err:
#         return err
#
# s = '雨'
# print(try_encode(s, 'utf-8'))
# print(try_encode(s, 'ascii'))
# print(try_encode(s, 'GB2312'))
#
#
# def try_decode(s, decoding):
#     try:
#         return s.decode(decoding)
#     except UnicodeDecodeError as err:
#         return err
#
# b = b'$'
# print(try_decode(b, 'utf-8'))
# print(try_decode(b, 'ascii'))
# print(try_decode(b, 'gbk'))
#
# b = b'\xd3\xea'
# print(try_decode(b, 'utf-8'))
# print(try_decode(b, 'ascii'))
# print(try_decode(b, 'gb2312'))
# print(try_decode(b, 'gbk'))
# print(try_decode(b, 'Big5'))


# import csv
# import re
# import json
# a = ['gjlhhFlag', 'gjlhhFlag', 'withdrawSpeed', 'salaryguard', 'registeredCapital',  'onlineDate', 'platId',
#      'serviceAttitude',  'platEarnings', 'platName', 'zonghezhishu', 'term',  'zonghezhishuRank',  'platNamePin',
#      'tzjPj', 'platNamePin', 'cityName', 'websiteExperience']
# f1 = open('F:\学习\新新贷\网贷之家.csv', 'r')
# f2 = open('F:\学习\新新贷\网贷之家(处理好数据).csv', 'w')
# try:
#     palt_list = csv.reader(f1)
#     header = next(palt_list)
#     # for i in palt_list:
#         # print(i)
#     csv_writer = csv.writer(f2, 'excel')
#     csv_writer.writerow(a)
#     k = 0
#
#     for i in palt_list:
#         if i:
#             # print(i[0])
#             b = re.sub('\'', '"', i[0])
#             # b = re.sub('"','"',b)
#             # b = re.sub("\n", '', b)
#             # b = re.sub("http://|https://", "", b)
#             # b = re.sub(" ","",b)
#             # b = re.sub('itunes.apple.',"",b)
#
#             print(b)
#             print(type(b))
#             jsonobject = json.loads(b)
#             print(jsonobject)
#             print(type(jsonobject))
#         #     k = 1
#         # if k == 1:
#         #     break
#
#
#             # b = re.sub('://', "", b)
#             # b = re.sub('http', "", b)
#             # b = re.sub('/', "", b)
#             # b = re.sub('itunes', "", b)
#             # print(b)
#             # print(type(b))
#             # print(b)
#             # json_object = json.loads(b)
#             # b = re.sub("http\W+| htpps\W+", "", b)
#             # b = re.sub(":", "", b)
#             # print(b)
#             # print(b)
#             # json_object = json.loads(b, strict=False)
#             # print(json_object)
#             # for j in a:
#             #     print(json_object.get(j))
#                 # csv_writer.writerow(ar)
# finally:
#     f1.close()
#     f2.close()
# #
# # # import re
# # # a = "http://openplat.wdzj.com/upload/plats/95/20161230140353s_.jpg"
# # # b = re.sub("http\w+|\W+", "", a)
# # # print(b)
#
# import re
# import json
# # a = [{'gjlhhFlag': '0', 'firstPin': 'X', 'platStatus': 1, 'withdrawSpeed': 3.1379, 'platIconUrl': 'http://www.wdzj.com/wdzj/images/plat/icon/95.jpg', 'salaryguard': 3.8017, 'registeredCapital': 5000, 'onlineDate': '2012-02-21', 'iosUrl': 'http://itunes.apple.com/cn/app/xin-xin-dai/id918745741?mt=8  ', 'platId': 95, 'serviceAttitude': 3.5603, 'wechat': 'http://openplat.wdzj.com/upload/plats/95/20161230140353s_.jpg', 'platEarnings': 8.68, 'platName': '新新贷', 'androidUrl': 'http://m.app.so.com/detail/index?from=qing&id=2394525 ', 'zonghezhishu': 0, 'term': '6-12月标(58.0%)、3月标(27.1%)', 'zonghezhishuRank': 0, 'tzjPj': '', 'platNamePin': 'xxd8', 'cityName': '上海|虹口', 'websiteExperience': 3.5172}]
# a = [{'gjlhhFlag': '0', 'firstPin': 'Z', 'wechat': 'http://openplat.wdzj.com/upload/plats/4535/20160719174612s_.jpg', 'platStatus': 1, 'platEarnings': 6.38, 'platName': '中平金融', 'androidUrl': 'http://o7m3ewr1m.bkt.clouddn.com/zpjr_beta_v1.0.8.apk\xa0', 'zonghezhishu': 0, 'platIconUrl': 'http://openplat.wdzj.com/upload/plats/4535/20160630130926s_.png', 'platId': 4535, 'zonghezhishuRank': 0, 'registeredCapital': 10000, 'onlineDate': '2016-03-17', 'tzjPj': '', 'iosUrl': 'https://itunes.apple.com/cn/app/zhong-ping-jin-rong/id1128612075?mt=8', 'platNamePin': 'zpjr', 'cityName': '河南|郑州', 'term': '3月标(48.1%)、1月标(23.1%)'}]
# # a = [{'gjlhhFlag': '0', 'firstPin': 'W', 'platStatus': 1, 'zonghezhishu': 0, 'platEarnings': 12, 'platName': '稳易金融', 'platId': 4991, 'withdrawSpeed': 3.375, 'platIconUrl': 'http://openplat.wdzj.com/upload/plats/4991/20160907110613s_.jpg', 'websiteExperience': 4.375, 'tzjPj': '', 'zonghezhishuRank': 0, 'registeredCapital': 1000, 'onlineDate': '2015-04-01', 'salaryguard': 4.0, 'platNamePin': 'wyjr0', 'cityName': '江苏|无锡', 'term': '6-12月标(66.0%)、24月以上标(19.0%)', 'serviceAttitude': 4.25}]
# b = re.sub('\'', '"', str(a[0]))
# regex = re.compile(r'\\(?![/u"])')
# b = regex.sub(r"\\\\", b)
# b = re.sub('\\(?![/u"])')
# pattern = re.compile(r'\\(?![/u"])')
# b = re.sub(pattern=pattern, r"\\\\", b)
# print(b)
# print(type(b))
# c = json.loads(b)
# print(c)
# print(type(c))
# # print(c)
# import re
# a = "\\"
# print(a)
# print(re.search('\\\\', a))
# d = re.search(r'\n', a)
# # print(d)
# # print(d.groups())
# b = re.split('[a-f]+', '0abadD32B9000', flags=re.IGNORECASE)
# print(b)
# c = re.sub('x *', "-", "abc")
# d = re.sub('x *', ' - ', 'abc ')
# print(c)
# print(d)
#
# m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
# print(m)
# print(m.group(1, 2))
# print(m.groupdict())
# print(m.groups())
# # payload = {'key1': 'value1', 'key2': 'value2'}
# from urllib.request import urlopen
# import json
# r = requests.post("http://httpbin.org/post")
# print(r.text)
#
# def getCountry(ipAddress):
#       response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
#       responseJson = json.loads(response)
#       return responseJson
# print(getCountry("103.200.30.110"))
# print(getCountry("192.168.2.1"))
# a = 'jiangshaobin'
# print(next(iter(a)))
# items = [1, 2, 3, 4]
# sqp = list(map(lambda x: x**2, items))
# print(sqp)
#
# number_list = range(-5, 5)
# less_than_zero = filter(lambda x: x < 0, number_list)
# print(list(less_than_zero))
# from functools import reduce
# product = reduce((lambda x, y: x*y), [1, 2, 3, 4, 5])
# print(product)
# print(help(set))
# print(dir(set))
# valid = set(['yellow', 'red', 'blue', 'green', 'black'])
# input_set = set(['red', 'brown', 'blue'])
# print(input_set.intersection(valid))
# print(type(input_set.intersection(valid)))
# print(input_set.difference(valid))
# input_set.add('rede')
# print(input_set)
# def add_to(num, target=[]):
#     target.append(num)
#     return target
#
# print(add_to(1))
# print(add_to(2))
# print(add_to(3))
#
#
# def add_to(num, target=None):
#     if target is None:
#         target=[]
#         target.append(num)
#     return target
#
# print(add_to(1))
# print(add_to(2))
# print(add_to(3))
# from collections import Counter
# cnt = Counter()
# word_list = ['red', 'blue', 'red', 'green', 'blue', 'blue']
# for word in word_list:
#     cnt[word] += 1
# print(cnt)
# a_list = [i for i in range(30) if i % 2 is 0]
# print(a_list)
# b_list = [x**2 for x in range(20) if x % 2 is 0]
# print(b_list)
# c_dict = {'j': 1, 'm': 2, 'i': 3}
# d_dict = {k: v for v, k in c_dict.items()}
# print(d_dict)
# print(c_dict.items())
# print(type(c_dict.items()))
# print(set(a_list))
# print({i for i in range(3)})
# a_list.sort(reverse=True)
# print(a_list)
# from pprint import pprint
# my_dict = {'name': 'Yasoob', 'age': 'undefined', 'personality': 'awesome'}
# pprint(my_dict)
# import itertools
# a_list = [[1, 2], [2, 3, 4], [5, 6]]
# print(list(itertools.chain.from_iterable(a_list)))
# print(set(itertools.chain.from_iterable(a_list)))
#
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print( n, 'equals', x, '*', n/x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')

# import timeit
# print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))
# import requests
# import random
# from bs4 import BeautifulSoup
# import json
# USER_AGENTS = [
#     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#     "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
#     "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
#     "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
#     "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
#     "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
#
# ]
#
# Header = {
#     'User-Agent': random.choice(USER_AGENTS),
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Language': 'en-US,en;q=0.5',
#     'Connection': 'keep-alive',
#     'Accept-Encoding': 'gzip, deflate',
# }
# url = 'http://www.wdzj.com/dangan/'
# url2 = 'http://www.wdzj.com/dangan/yrd'
#
# req = requests.get(url2, headers=Header)
# req_text = req.content.decode('utf-8')
# bs_object = BeautifulSoup(req_text, 'html.parser')
# print(type(bs_object))
# # print(bs_object)
# print(bs_object)
# # print(req.text)
# print(type(req.content))
# print(type(req.text))
# print(type(req.text.encode('utf-8')))
# print(type(req.content.decode('utf-8')))

# print(req.content.decode('utf-8'))
# print()
# print(type(req_text))
# a = b"\xc3\xa4\xc2\xb8\xc2\x8a\xc3\xa6\xc2\xb5\xc2\xb7\xc3\xa5\xc2\xb8\xc2\x82\xc3\xa4\xc2\xba\xc2\x92\xc3\xa8\xc2\x81\xc2\x94\xc3\xa7\xc2\xbd\xc2\x91\xc3\xa8\xc2\xbf\xc2\x9d\xc3\xa6\xc2\xb3\xc2\x95\xc3\xa5\xc2\x92\xc2\x8c\xc3\xa4\xc2\xb8\xc2\x8d\xc3\xa8\xc2\x89\xc2\xaf\xc3\xa4\xc2\xbf\xc2\xa1\xc3\xa6\xc2\x81\xc2\xaf\xc3\xa4\xc2\xb8\xc2\xbe\xc3\xa6\xc2\x8a\xc2\xa5\xc3\xa4\xc2\xb8\xc2\xad\xc3\xa5\xc2\xbf\xc2\x83"
# print(a.decode('iso-8859-1', 'ignore'))
# # a = 'ä¸æµ·å¸äºèç½è¿æ³åä¸è¯ä¿¡æ¯ä¸¾æ¥ä¸­å¿'
# # json_object = json.dump(a,fp='', ensure_ascii=False)
# json_object = json.dumps(a, ensure_ascii=False)
# # print(json_object)
# print(json_object)

# print(7/3)
# print(7 % 3)
# print(7//3)
# pv = 100/(1+0.1)**2
# print(pv)
# print(100*pow((1+0.1), 1))
# b = [1, 2]
# a = [2, 3]
# a = a+b
# print(a)
#
# help(round)
# print(dir())
# print(dir(__builtins__))
# print(dir(__package__))
# import math
# print(dir(math))
# help(math.log2)
# print(math.log2(8))
# print('pi=', math.pi)
# print('e=', math.e)
# print(math.log(math.e))
# help(''.capitalize)
# x = (1)
# print('x', type(1))
# help(print)
# Rn = (1+0.05/2)**2-1
# print(Rn, Rn/12)
# help(enumerate)
#
#
# def npv_f(rate, cashflows):
#     total = 0
#     for i, cashflows in enumerate(cashflows):
#         total += cashflows/(1+rate)**i
#     return total
#
# rate = 0.05
# cashflows = [-100, 20, 40, 50, 20, 10]
# print(npv_f(0.05, cashflows))
# print(type(enumerate(cashflows)))
# for i, cashflows in enumerate(cashflows):
#     print(i, cashflows)
#
#
#
# print(100*(1+0.05)**5)
import os
from os import listdir
# print(os.path)
# help(os.path)

# print(listdir("c:"))
# ar = []
# for i in range(10):
#     ar.append(i)
# print(ar)
# ar.append([1, 2, 4])
# print(ar)


# for i in range(10):
#     url_product_id = 'http://invest.ppdai.com/product/info?producttype=ppb&productid=%i' % i
#     print(url_product_id)
#     print('now download is % i' % i)

# with open('F:\P2P行业企业分析\拍拍贷\彩虹计划相关数据.csv', 'w') as f:
#     csv_write = csv.writer(f, 'excel')
#     csv_write.writerow(['利率', '无效数据1', '投资期限', '开放购买时间', '投资到期日', '无效数据2', '投资额度', '无效数据3', '产品id'])

# a = []
# for i in range(10):
#     a.append(i)
# print(a)
# # print(a.pop(1))
# a = 'this page is error,  34'
# print(len(a))
# print(a[21:])
# for product_id in range(1, 2):
#     for page in range(1, 5):
#         values = (page, product_id)
#         url = 'http://rise.invest.ppdai.com/Product/InvestListPartial?page=%i&productID=%s' % values
#         print(url)
# import string
# a_list = [' 63, 5', ' 118, 5', ' 186, 5', ' 7, 6', ' 12, 6', ' 19, 6', ' 40, 6', ' 179, 6', ' 188, 6', ' 191, 6', ' 236, 6', ' 237, 6', ' 254, 6', ' 268, 6', ' 269, 6', ' 270, 6', ' 280, 6', ' 76, 7', ' 90, 7', ' 157, 7', ' 169, 7', ' 186, 7', ' 235, 7', ' 236, 7', ' 243, 7', ' 264, 7', ' 279, 7', ' 290, 7', ' 291, 7', ' 292, 7', ' 293, 7', ' 297, 7', ' 300, 7', ' 301, 7', ' 302, 7', ' 5, 8', ' 54, 8', ' 147, 8']
# for values in a_list:
#     values = (str.strip(values[:values.find(',')]), str.strip(values[values.find(',')+1:]))
#     url = 'http://rise.invest.ppdai.com/Product/InvestListPartial?page=%s&productID=%s' % values
#     # print(values)
#     # print(type(values))
#     print(url)
# # help(str)
#
# values = (1, 2)
# print(values(2))

# class Person:
#
#     def setName(self, name):
#         self.name = name
#
#     def getName(self):
#         return self.name
#
#     def greet(self):
#         print("Hello word ! i'm $s." % self.name)
#
# # help(map)
# #
# # help(issubclass)
# #
# # a = Person()
# # b = Person()
# # print(a)
# # print(b)
# # print(callable(BeautifulSoup))
# # # help(getattr)
# # print(getattr(Person, 'setName'))
# import traceback
# # help(traceback)
#
# # help(AttributeError)
# print(dir())


# 魔法方法
# class Bird:
#     def __int__(self):
#         self.hungry = True
#
#     def eat(self):
#         if self.hungry:
#             print('Aaaah....')
#             self.hungry = False
#         else:
#             print('No thanks!')
#
# b = Bird()
# print(b.eat)
#
#
# class songbird(Bird):
#     def sing(self):
#         self.sound = 'Squawk!'
#         print(self.sound)
#
#
# class songbird_init(Bird):
#     def __init__(self):
#         self.sound = 'Squawk !'
#
#     def sing(self):
#         print(self.sound)


# test1 = songbird()
# test_init = songbird_init()
# b = Bird()
# print(b.eat())
# print('test1', test1.eat())
# print('test1_init', test_init.eat())

import requests
url = 'http://www.analysys.cn/analysis/8/details?articleId=18095'
req = requests.get(url)
print(req.text)



