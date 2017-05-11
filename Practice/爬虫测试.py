# from urllib.request import urlopen
# html = urlopen("http://pythonscraping.com/pages/page1.html")
# print(html.read())


# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen("http://www.pythonscraping.com/pages/page1.html")
# bsObj = BeautifulSoup(html.read(), "html.parser")  # 为什么需要加上“html.parser”的文本
# print(bsObj.h1)
# print(html.read())

# 避免获取html出现错误的写法
# from urllib.request import urlopen
# from urllib.error import HTTPError, URLError
# from bs4 import BeautifulSoup
# def getTitle(url): # 定义getTitle函数
#     try:
#         html = urlopen(url)
#     except (HTTPError, URLError) as e:
#         return None
#     try:
#         bsObj = BeautifulSoup(html.read(), "html.parser")
#         title = bsObj.body.hl
#     except AttributeError as e:
#         return None
#     return title
# title = getTitle("http://www.pythonscraping.com/pages/warandpeace.html")
# if title == None:
#     print("Title could not be fond")
# else:
#     print(title)
#
# # # # 第一个爬虫(返回网站规定的特定内容)
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
# bsObj = BeautifulSoup(html, "html.parser")
# bsObj2 = BeautifulSoup(html.read(), "html.parser")
# nameList = bsObj.findAll("span", {"class": {"green", "red"}})
# # title = bsObj2.h1 # 没有返回预期值
# # print(html.read()) # 为什么没有返回串的东西
# for name in nameList:
#     print(name.get_text())


# 课本的例子
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
# bsObj = BeautifulSoup(html, "html.parser")
# nameList = bsObj.findAll("span", {"class":"green"})
# for name in nameList:
#     print(name.get_text())
#
# # this is my fist script
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# # html = urlopen("http://www.pythonscraping.com/pages/page1.html")
# # html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
# # html = urlopen("https://www.jylc168.com/product/detail/id/ADAjAkYd-0u1OrhCirrg1A.html")
# html = urlopen("http://w3school.com.cn/html/index.asp.html")
# bsObj = BeautifulSoup(html, "html.parser")
# content = bsObj.findAll("div", id="tpn")
# # for cot in content:content
# #     print(cot.get_text())
# # print(bsObj)
# # for cot in content:
# #     print(cot.get_text())
# print(content)

# # 导航树
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen("http://www.pythonscraping.com/pages/page3.html")
# bsObj = BeautifulSoup(html.read(), "html.parser")
# # a = bsObj.tag.subTag.anotherSubTag # 导航树语法,这个问题没有解决
# # print(a)
# print(html.read())

# # 打印子标签
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen("http://www.pythonscraping.com/pages/page3.html")
# bsObj = BeautifulSoup(html, "html.parser")
# for child in bsObj.find("table", {"id": "giftList"}).children: # children打印子标签descendants打印后代标签
#     print(child) # 为什么.get_text()函数没有用

# # 打开CVS格式数据(写入数据)
# import csv
# csvFile = open("F:学习/python/test.xlwt", 'w')
# try:
#      writer = csv.writer(csvFile)
#     writer.writerow(('number', 'number plus 2', 'number times 2'))
#     for i in range(10):
#        writer.writerow((i, i+2, i*2))
# finally:
#     csvFile.close()

# # # 把html上的表格写入xlwt中
# import csv
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen("https://en.wikipedia.org/wiki/Comparison_of_text_editors")
# bsObj = BeautifulSoup(html, "html.parser")
# table = bsObj.findAll("table", {"class": "wikitable"})[0] # [0]表示wikiable列表利的第一个，如果是格式一样，就可以试用wikitablelist
# rows = table.findAll("tr")
# csvFile = open("F:/学习/python/wikitable editors1.xlmt", 'wt', newline='', encoding='utf-8')
# writer = csv.writer(csvFile)
# try:
#     for row in rows: # 这里还有点小问题，这个for循环写出来是阶梯形式
#         csvRow = []
#         for cell in row.findAll(['td', 'th']):
#            csvRow.append(cell.get_text())
#            writer.writerow(csvRow)
# finally:
#     csvFile.close()
#
# # 加载nltk函数
# import nltk
# nltk.download()

# # 如何处理
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen("http://www.pythonscraping.com/pages/page3.html")
# # html = urlopen('https://www.jylc168.com//home/product/ajax_invest_list.html')
# bsObj = BeautifulSoup(html, "html.parser")
# price = bsObj.findall("$")
# print(price)









