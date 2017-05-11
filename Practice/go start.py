# 第二课：获取网页源码
# from urllib.request import urlopen
# a = urlopen("https://www.jylc168.com/product/detail/id/ZgFdAeZWNBkrvm1e7MRkLQ")
# # print(a) # 读取对象
# print(a.read()) # 读取源码
#
# # 第三课：（1）POST数据加载
# from urllib.request import urlopen
# from urllib.parse import urlencode
# values = {"usename": "2532489252@qq.com", "password": "XXXXX"} # 构建字典对象values
# data = urlencode(values) # python3中如何把登陆口令转换成URL格式？？？
# # print(data)
# url = "https://www.jylc168.com/access/login" # 囧羊理财登陆界面
# reqonse = urlopen(url, data)
# # (2)get数据加载
# from urllib.request import urlopen
# from urllib.parse import urlencode
# from urllib.request import Request
# host = "https://www.jylc168.com/access/login"
# values = {"usename": "2532489252@qq.com", "password": "xxxxxxx"}
# data = urlencode(values)
# url = host+'?'+data
# # print(url)
# res = Request(url)
# response = urlopen(res)


# 第四课 设置头部
# from urllib.request import urlopen
# from urllib.parse import urlencode
# from urllib.request import Request
# host = "https://www.zhihu.com"
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"}
# values = {"usename": "2532489252@qq.com", "password": "jiang0110486"}
# data = urlencode(values)
# url = host+'?'+data
# print(url)
# # print(url)
# res = Request(url, headers)
# response = urlopen(res)
# print(response)








