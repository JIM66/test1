# from collections import deque
# a_list = []
# a_list = deque(maxlen=6)
# for i in range(10):
#     a_list.append(i)
# print(a_list)
# print(type(a_list))
# a1,*a2, a3, a4 = a_list[:6]
# print(a1,a2,a3,a4)
# print(sum(a_list[1:4]))
# line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
# uname, *file, homedir, sh = line.split(':')
# print(uname)
# print(*file)

# 3.4.1怎样从一个集合中获得最大或最小的N个元素列表
import heapq
# a_list = []
# for i in range(10):
#     a_list.append(i)
# print(heapq.nlargest(3, a_list))
# print(heapq.nsmallest(3, a_list))
# # print(dir(heapq.__all__))
# # help(heapq)
# b_list = [-2, 2, -4, -5, 6]
# heapq.heapify(b_list)
# print(b_list)
# c_list = [a_list, b_list]
# print(c_list)
#
# a = heapq.merge(c_list)
# # print(c_list)
# help(heapq.merge)
# # print(type(a))
# b_list = heapq.merge([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [-5, -2, -4, 2, 6])
# # print(list(heapq.merge([1,3,5,7], [0,2,4,8], [5,10,15,20], [], [25])))
# # print(list(heapq.merge(a_list, b_list)))
# # print(set(heapq.merge(a_list, b_list)))
# portfolio = [{'name': 'IBM', 'shares': 100, 'price': 91.1},
# {'name': 'AAPL', 'shares': 50, 'price': 543.22},
# {'name': 'FB', 'shares': 200, 'price': 543.22},
# {'name': 'HPQ', 'shares': 200, 'price': 31.75},
# {'name': 'YHOO', 'shares': 45, 'price': 16.35},
# {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# # print(type(property))
# print(heapq.nsmallest(1, portfolio, key=lambda x: x['price']))
# print(heapq.nlargest(1, portfolio, key=lambda x: (x['shares'], x['price'])))  # 构建元组比较大小
# print(max(x['price'] for x in portfolio))
#
# print((True, False) > (True, True))
# help(heapq)

# 实现一个优先级队列问题，表示没有懂


# class Priority_Queue:
#     def __init__(self):
#         self._queue = []
#         self._index = 0
#
#     def push(self, item, priority):
#         heapq.heappush(self._queue, (-priority, self._index, item))
#         self._index += 1
#
#     def pop(self):
#         return heapq.heappop(self._queue)[-1]
#
#
# class Item:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return 'Item({!r})'.format(self.name)
#
# q = Priority_Queue()
# q.push(Item('foo'), 1)
# q.push(Item('bar'), 5)
# q.push(Item('spam'), 4)
# q.push(Item('grok'), 1)


# class PriorityQueue:
#     def __init__(self):
#         self._queue = []
#         self._index = 0
#
#     def push(self, item, priority):
#         heapq.heappush(self._queue, (-priority, self._index, item))
#         self._index += 1
#
#     def pop(self):
#         return heapq.heappop(self._queue)[-1]
#
#
# class Item:
#     def __int__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return 'Item({!r})'.format(self.name)
#
# q = PriorityQueue()
# q.push(Item('foo'), 1)
# q.push(Item('bar'), 5)
# q.push(Item('spam'), 4)
# q.push(Item('grok'), 1)
# print(q.pop())
# h = []
# a_list = [1, 2, 3, 4, 5]
# heapq.heappush(h, a_list)
# # print(type(heapq.heappop(h)))
# print(heapq.heappop(h))

# 3.16

# from collections import defaultdict
#
# d = defaultdict(list)
# d['a'].append(1)
# d['a'].append(2)
# d['b'].append(3)
# print(d)
#
# d = defaultdict(set)
# d['a'].add(1)
# d['a'].add(2)
# d['b'].add(3)
# print(d)

# prices = {
# 'ACME': 45.23,
# 'AAPL': 612.78,
# 'IBM': 205.55,
# 'HPQ': 37.20,
# 'FB': 10.75
# }
# min_price = min(zip(prices.values(), prices.keys()))
# # print(min_price)
# print(type(min_price))
# print(prices.keys())
# a = {'x' : 1,
# 'y' : 2,
# 'z' : 3
# }
# b = {'w' : 10,
# 'x' : 11,
# 'y' : 2
# }
#
# print(a.keys() & b.keys())
# print(a.keys() - b.keys())
# print(a.items() & b.items())
# print(a.items())

# 3.10怎样在一个序列上面保持元素的同时消除重复的值

# 1、序列上的元素都是hashable类型
# def dedupe(items):
#     seen = set()
#     for item in items:
#         if item not in seen:
#             yield item
#             seen.add(item)
#     return seen
#
a = [1, 5, 2, 1, 5, 2, 1, 9, 10]
# print(dedupe(a))
# print(list(dedupe(a)))

# 2、序列中的元素不可哈希时


# def dedupe(items, key = None):
#     seen = set()
#     for item in items:
#         val = item if key is None else key(item)
#         if val not in seen:
#             yield item
#             seen.add(val)
#     return seen
#
# b = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
# print(list(dedupe(b, key=lambda d: (d['x'],d['y']))))
# print(list(dedupe(b, key=lambda d: d['x'])))
# print(list(dedupe(a)))

# # 3.12找出一个序列中出现次数最多的元素
# from collections import Counter
# words = [
# 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
# 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
# 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
# 'my', 'eyes', "you're", 'under','jim love', 'jim love'
# ]
#
# word_count = Counter(words)
# top_three = word_count.most_common(3)
# print(word_count)
# print(top_three)

# 3.13对字典列表排序，使用operator模块中的itemgetter函数比使用lambda表达式快点
# from operator import itemgetter
# rows = [
# {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
# {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
# {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
# {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
# ]
# rows_by_fname = sorted(rows, key=itemgetter('fname'))
# print(rows_by_fname)
# rows_by_fname = sorted(rows, key=lambda x: x['fname'])
# print(rows_by_fname)


# 3.15根据某个字段比如DATA进行分组迭代访问()
# from operator import itemgetter
# from itertools import groupby
# rows = [
# {'address': '5412 N CLARK', 'date': '07/01/2012'},
# {'address': '5148 N CLARK', 'date': '07/04/2012'},
# {'address': '5800 E 58TH', 'date': '07/02/2012'},
# {'address': '2122 N CLARK', 'date': '07/03/2012'},
# {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
# {'address': '1060 W ADDISON', 'date': '07/02/2012'},
# {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
# {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
# {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}
# ]
#
# rows.sort(key=itemgetter('date'))
# for data, items in groupby(rows, key=itemgetter('date')):
#     print(data)
#     for i in items:
#         print("  ", i)
#
# print(groupby(rows, key=itemgetter('date')))
# print(list(groupby(rows, key=itemgetter('date'))))


# 3.16过滤序列元素

# 4.1使用多个界定符
# import re
# line = 'asdf fjdk; afed, fjek,asdf, foo'
# a = re.split('[;,\s]\s*', line)
# print(a)

# # 5.1数字日期和时间
# a = 2.1
# b = 4.2
# c = a+b
# print(c)
# # c = 6.300000000000001 原因：浮点数的一个普遍问题是它们并不能精确表示十进制数，
# # 并且，即使是最简单的数学运算也会产生小误差
# # 这些错误是由于底层CPU和IEEE754标准通过自己的浮点单位去执行算术时的特征
# # 如果想要更精确（并且能够容忍一定的性能损耗），你可以是使用decimal模块
# import decimal
# from decimal import Decimal
# a = Decimal('4.2')
# b = Decimal('2.1')
# print(a+b)
# #　ａ＋ｂ＝6.3
# print(type(a))
# help(format)

# 第四章  迭代器与生成器
import itertools
# help(itertools)
# help(reversed)
# def frange(start, stop, step=1):
#     x = start
#     while x< stop:
#         yield x
#         x += step
#
# a = frange(1, 5, 0.5)
# print(list(frange(1, 5, 0.5)))
# print(type(frange(1, 5, 0.5)))
# print(a)
# print(next(a))
#
# def frange2(start, stop, step=1):
#     x = start
#     while x < stop:
#         x
#         x += step
# print(frange2(1, 5, 0.5))
# print(type(frange2(1, 5, 0.5)))
# import requests
# from itertools import permutations
# a = ['a', 'b', 'c', 'd']
# for c in permutations(a, 3):
#     print(c, end=' ')
#
# help(print)
# import os
# import sys
# print(sys.getdefaultencoding)
# help(requests.get)
#
#
# def myfun():
#     return 1, 2, 4, 5
#
# a, *b, c = myfun()
# print(b)


import numpy as np

a = np.arange(15).reshape(3, 5)
print(a)






