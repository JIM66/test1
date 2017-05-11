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
#
# # 囧羊理财（龙佳)
# import requests
# from bs4 import BeautifulSoup
# import re
# import csv
# host = 'https://www.jylc168.com'
# url = 'http://www.jylc168.com/home/product/ajax_search_lists'
# req = requests.post(url)
# size = req.json()['data']['total_count']
# req = requests.post(url, data={'size': size})
# soup = BeautifulSoup(req.json()['data']['html'], 'html.parser')
# list_n = soup.find_all('div', 'm-pj2 m-pj ui-border mt10 pr')
# max_bid = BeautifulSoup(requests.get(host + list_n[0].find('a').get("href")).text, 'html.parser').find("input").get("value")
# with open("囧羊理财.xml", 'w', newline='') as cs:
#     csv_write = csv.writer(cs, 'excel')
#     csv_write.writerow(['理财频道', '项目名称', '标的金额', '年化利息', '项目期限', '收益方式', '当前进度', '剩余可投金额', '状态', '标的链接'])
#     for n in list_n:
#         ar = [row for row in re.sub('\r| |.*: |￥|元', '', n.get_text()).split('\n') if len(row) > 0]
#         ar.append('{}{}'.format(host, n.find("a").get("herf")))
#         csv_write.writerow(ar)










