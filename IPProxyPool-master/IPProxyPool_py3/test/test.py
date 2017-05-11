# #coding:utf-8
# import requests
# import json
# r = requests.get('http://127.0.0.1:8000/?types=0&count=5&country=中国')
# ip_ports = json.loads(r.text)
# print(ip_ports)
# ip = ip_ports[0]['ip']
# port = ip_ports[0]['port']
# proxies={
#     'http':'http://%s:%s' % (ip, port),
#     'https':'http://%s:%s'%(ip,port)
# }
# r = requests.get('http://ip.chinaz.com/',proxies=proxies)
# r.encoding='utf-8'
# print(r.text)


# class test:
#     def __init__(self):
#         self.somevar = 42
# f = test()
# print(f.somevar)
#
#
# class test2:
#     def __init__(self, value='value'):
#         self.somevar = value
#
# f = test2("jim love python")
# print(f.somevar)
#
#
# class Bird:
#     def __init__(self):
#         self.hungry = True
#
#     def eat(self):
#         if self.hungry:
#             print('Aaaah....')
#             self.hungry = False
#         else:
#             print("No, thanks!")
#
# b = Bird()
# print(b.eat())
# print(b.eat())

# import json
# f = open('F:\学习\天猫双12商品活动数据.json', 'r', encoding='utf-8')
# print(json.load(f))


import json
# with open('F:\学习\天猫双12数据\天猫双12商品活动数据.json', 'r', encoding='utf-8') as content_file:
#     test_text = content_file.readlines()
#     for i in test_text:
#         if i['商品ID'] == "3219440286807":
#             print(i)
# # # #
#
# content_file.close()
# test_text = content_file.read()   # 为什么么不行，是因为数据太大吗？
# a = json.loads(test_text, encoding='utf-8')
# print(test_text)
# print(a)


# test_list = [{"_id": "https://detail.tmall.com/item.htm?id=520515542998\u0026skuId=3102455949784", "优惠活动": "全天猫实物商品通用", "商品ID": "520515542998", "服务保障": "正品保证;极速退款;七天退换","原价":"143.00","活动开始时间":"2016-12-12 00:00:00","快递费":"快递: 0.00","卖家地址":"浙江金华","会场":"百货会场","现价":"28.80","活动结束时间":"2016-12-12 23:59:59","标题":"16寸新款超大diy相册手工粘贴式皮革情侣家庭宝宝儿童影集拍立得"},
#
# {"_id":"https://detail.tmall.com/item.htm?id=520515542998\u0026skuId=3102455949785", "优惠活动": "全天猫实物商品通用","商品ID":"520515542998","服务保障":"正品保证;极速退款;七天退换","原价":"143.00","活动开始时间":"2016-12-12 00:00:00","快递费":"快递: 0.00","卖家地址":"浙江金华","会场":"百货会场","现价":"28.80","活动结束时间":"2016-12-12 23:59:59","标题":"16寸新款超大diy相册手工粘贴式皮革情侣家庭宝宝儿童影集拍立得"}]
# for i in test_list:
#     if i["商品ID"] == "520515542998":
#         print(i)
# # #

# print(bin(9))
# from json import loads
# from bs4 import BeautifulSoup
# print(callable(BeautifulSoup))
# print(chr(111))
# print(complex('1+2j'))
# print(dir(json))
# print(callable(loads))
# print(divmod(5, 3))
# a = [1, 2, 3, [1, 2, 3]]
# b = {1: 2}
# print(list(enumerate(a)))
# x = 1
# print(eval('x+1'))
# print(hasattr(json, "loads"))
# print(hex(134))
# print(hash(str(a)))
# print(id(a))
# print(id(b))
# print(pow(2, 3, 3))
# print(repr(a))
# print(type(repr(a)))
# print(list(reversed(a)))
# print(6//5)
# print(divmod(3, 5))
# print(type((3, 5)))
# n = [1, 2, 3]
# a = 4
# print(n * a)
# b = 'jim.jiang'
import numpy as np
a = np.arange(15).reshape(5, 3)
print(a)
print(type(a))













