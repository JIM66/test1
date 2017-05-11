import numpy as np
import pandas as pd
import matplotlib as mat


# data = [1, 2, 3, 4]
# array1 = np.array([1, 2])
# a = np.array([1, 2, 3, 4])
# b = np.array((5, 6, 7, 8))
# c = np.array([[1, 2, 3, 4], [0.14, 5, 6, 7], [7, 8, 9, 10]], dtype=np.int64)
# print(c)
# print(a)
# print(b)
# print(c)
# print(type(c))
# print(c.shape)
# print(a.shape)
# c.shape = 4, 3
# print(c)
# d = a.reshape(2, 2)
# print(d)
# a[1] = 100
# print(d)
# print(np.arange(0, 1, 0.1))
# e = np .arange(0, 1, 0.1)
# print(len(e))
# e.shape = 2, 5
# print(e)
# a = np.arange(10)
# print(a)
# print(a[5])
# b = np.arange(56)
# print(b)
# b.shape = 7, -1
# # print(b)
# print(b)
# a = np.array([[1, 2, 3., 4], [1, 2, 3, 4]])
# print(a)
# print(a*a)
# print(a*10)
# # print(a.dtype)
# import time
# import math
# import numpy as np
# x = [i*0.001 for i in range(100000)]
# start = time.clock()
# for i, t in enumerate(x):
#     x[i] = math.sin(t)
# print('math.sin', time.clock()-start)
#
# x = [i*0.001 for i in range(100000)]
# x = np.array(x)
# start = time.clock()
# np.sin(x, x)
# print('np.sin', time.clock()-start)
# x1 = np.arange(0, 4)
# x2 = np.arange(4, 8)
# print(x1, x2)
# print('x1+x2', np.add(x1, x2))
# print('x1-x2', np.subtract(x1, x2))
# print('x1*x2', np.multiply(x1, x2))
# print('x1/x2', np.divide(x1, x2))
# print('x1//x2', np.floor_divide(x1, x2))
# print('non', np.floor(x1))
# print('x1%/x2', np.remainder(x1, x2), np.mod(x1, x2))
# a = np.arange(0, 60, 10).reshape(-1, 1)
# print(a, a.shape)
# b = np.arange(0, 5)
# print(b, b.shape)
# c = a+b
# print(c)
# print(c.shape)
# 读取文件
# help(np.size)
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(np.size(a, 1))
# help(np.dot)
# x1 = np.arange(1, 5).reshape(2, 2)
# x2 = np.arange(1, 7).reshape(2, 3)
# a = np.dot(x1, x2)
# print(a)
# x1.dot(x2)
# print(type(a))
# # help(np.linalg)
# # help(np.linalg.inv)
# samples = np.random.normal(size=(4, 4))
# print(np.round(samples, 3))
# print(np.linalg.inv(samples))
# nsteps = 1000
# draws = np.random.randint(0, 2, size=nsteps)
# # print('draws', draws)
# steps = np.where(draws > 0, 1, -1)
# # print('steps', steps)
# walk = steps.cumsum()
# # print('walk', walk)
# print('max:', walk.max(), '\n', 'min', walk.min())
# # print(len(walk))
# # print(walk)
# print((np.abs(walk) >= 10).argmax())
# a = (np.abs(walk) >= 10)
# print(a.argmax())
# print(a)
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.interpolate import interp1d
# x = np.linspace(0, 10, 10)
# print('x', x)
# y = np.exp(-x/3.0)
# f = interp1d(x, y)
# f2 = interp1d(x, y, kind='cubic')
# xnew = np.linspace(0, 10, 40)
# print('xnew', xnew)
# plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
# plt.legend(['data', 'linear', 'cubic'], loc='best')
# plt.show()
# x = np.array([[1, 2, 3], [3, 4, 6]])
# print(x)
# help(np.size)
# print(np.size(x, 1))
# total = sum(x)
# print(total)
# print(np.array([100, 0.1, 2], float))
# cashflows = [50, 40, 20, 10, 50]
# print(round(sp.npv(0.1, cashflows), 2))
# a = np.zeros(10)
# print(a)
# b = np.zeros((3, 2), dtype=float)
# print(b)
# e1 = np.identity(4)
# e2 = np.eys(4)
# print(e2)
# y = np.array([[1, 2, 3], [4, 5, 6]])
# print(x*y)
# # help(np.var)
# # help(np.dot)
# # help(np.argmax)
# cashFlows = np.array([-100, 30, 50, 100, 30, 40])
# print(np.argmax(cashFlows))






# pandas 入门
from pandas import Series, DataFrame
import random
import scipy as sp
import pandas as pd
import csv
# obj = Series([4, 7], index=['a', 'b'])
# print(obj)
# obj2 = Series([1, -2, 3])
# print(obj2)
# # print(obj2.index)
# print(obj2[obj2 > 0])
# print(obj2**2)
# sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 1600, 'Utah': 5000}
# obj3 = Series(sdata)
# print(obj3)
# states = ['California', 'Ohio', 'Oregon', 'Texas']
# obj4 = Series(sdata, index=states)
# print(obj4)
# print(pd.isnull(obj4))
# print(obj3+obj4)
# '-------------------------------------'
# obj4.name = 'this is state people'
# obj4.index.name = 'state'
# # obj3.values.name = '人口数量'
# print(obj4)
# f = open('F:\学习\新新贷\网贷之家2.csv', 'r')
# content_list = csv.reader(f)
# # content_list = next(content_list)
# ar = []
# for i in content_list:
#     if i:
#         ar.append(i)
# index = ar[0]
#
# farme = DataFrame(ar[1:], columns=ar[0])
# a = farme['platName']
#
# # print(farme)
# # print(index)
# # print(a)
# f.close()
# fram = DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'b', 'd'], columns=['Ohio', 'Texas', 'Californa'])
# print(fram)
# fram2 = fram.reindex(['a', 'b', 'c', 'd'])
# print(fram2)
# state = ['Ohio', 'Texas', 'Californa', 'Utah']
# fram3 = fram2.reindex(columns=state)
# print(fram3)
# fram4 = fram3.drop('c')
# print(fram4)
# print(type(fram4))
# obj = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
# print(obj)
# print(obj[[1, 2]])
# print(type(obj))
# df1 = DataFrame(np.arange(12.).reshape(3, 4), columns=list('abcd'))
# df2 = DataFrame(np.arange(20.).reshape(4, 5), columns=list('abcde'))
# print('df1', df1)
# print('df2', df2)
# print('df1+df2', df1+df2)
# print('df1/df2', df1/df2)
# print('df1-df2', df1-df2)
# print('df1*df2', df1*df2)
# print(df1.mul(df2, fill_value=0))
import numpy as np
# a = [i for i in range(0, 4)]
# b = [i for i in range(4, 8)]
# data = [a, b]
# print(type(data))
# data = np.array(data)
# print('', data.dtype)
# # help(np.array)
# # help(np.arange)
# data1 = np.arange(0, 4)
#
# print('data1', data1.dtype)
# data2 = np.arange(0, 4), np.arange(4, 8)
# # print('data2', data2.dtype)
# print(type(data2))
# print(data2)
# data3 = np.array(data2,dtype=float)
# print('data3', data3.dtype, data3)
# print('data1', data1.dtype, data3)
# print(data3*10, data3+data1)
# # help(np.ndim)
# print(np.ndim([1]))
# print(np.ndim(1))
# print(data3.shape)
# print(data3.reshape(4, 2))
# data4 = data3.reshape(4, 2)
# # print(data3)
# a = np.zeros((2, 3), dtype=float, order='F')
# print('a', a)
# b = np.ones((2, 3))
# print('b', b)
# # help(np.ones)
# help(np.eye)
# print(np.eye(N=3, k=1))
# a = ['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']
# names = np.array([a])
# a = names == 'Bob'
# print(a)
#
# arr = np.arange(10).reshape(2, 5)
# print(np.sqrt(arr))
# print(np.exp(arr))
# x =np.random.rand(8)
# y =np.random.rand(8)
# print(x)
# print(y)
# print(np.maximum(x, y))
# points = np.arange(-5, 5, 0.01)
# xs, ys = np.meshgrid(points, points)
# print(ys)
# print(xs)
# help(np.meshgrid)
# import matplotlib.pyplot as plt
# z = np.sqrt(xs**2+ys**2)
# print(z)
# plt.imshow(z, cmap=plt.cm.gray);plt.colorbar()
# plt.title("test")
# plt.show()
# arr2 = np.arange(-2, 2, 1).reshape(2, 2)
# print(arr2)
# arr3 = np.where(arr2 > 0, 2, -2)
# print(arr3)
# arr4 = np.random.randn(9)
# print(arr4.mean())
# print(arr4.std())
from pandas import DataFrame, Series
# Data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 'year': [2000, 2001, 2002, 2003, 2004],
#         'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
# frame = DataFrame(Data, columns=('year', 'state', 'pop'))
# print(frame)
# frame2 = DataFrame(Data, columns=('year', 'state', 'pop', 'debt'), index=['one', 'two', 'three', 'four', 'five'])
# print(frame2)
# print(frame2.columns)
# print(frame2['state'], frame2.year)
# frame2.debt = 16.5
# print(frame2)
# frame2['debt'] = np.arange(5,)
# print(frame2)
# val = Series([1, 2, 4], index=['one', 'three', 'four'])
# frame2.debt = val
# print(frame2)
# frame2['eastern'] = frame2.state == 'Ohio'
# print(frame2)
# a = Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# print(a)
# b = a.reindex(['a', 'b', 'c', 'd', 'e', 'f'], fill_value=[0, 1])
# print(b)
# c = a.reindex(['a', 'b', 'c', 'd', 'e', 'f'], fill_value=0)
# print(c)
# obj3 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
# d = obj3.reindex(range(6), method='ffill')
# print('d ', d)
# c = obj3.reindex(range(6), method='bfill')
# print('c ', c)
# 排序和排名
# obj = Series(np.arange(4), index=list('dbca'))
# print(obj.sort_index())
# data = DataFrame(np.arange(8).reshape(2, 4), index=('three', 'one'), columns=list('abcd'))
# print(data.sort_values('a'), flush=True)
# # help(DataFrame.sort_values)
# obj2 = Series([-7, 7, 2, 6, 5, 2])
# print(obj2.rank())
# print(obj2)

# frame = DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]], index=['a', 'b', 'c', 'd'],
#                   columns=['one', 'two'])
# print(frame)
# print(frame.sum())
# print(frame.sum(axis=1))
# print(frame.describe())
# print(frame.describe())
# frame2 = Series(['a', 'a', 'b', 'c']*4)
# # print(frame2)
# # print(frame2.describe())
# # print(type(frame2.describe()))
# a = frame2.describe()
# print(a)
# print(a.index)
# print(a['top'])
# print(frame2.describe()['freq'])
# # print(frame.describe()[''])
# b = frame.describe()
# print(b.index)
# # print(b["min"])
# print(type(b))
# # print(b.ix[''])
# print(b['one'])
# print(b.ix['50%'])
# print(b.ix['mean', 'one'])
# data = Series([1.1, np.nan, 2.3, np.nan, 3.5])
# print(data.dropna())
# print(data[data.notnull()])
# data = DataFrame([[1, 6.5, 3, np.nan], [1, np.nan, np.nan, np.nan], [np.nan, np.nan, np.nan], [np.nan, 6.5, 3, np.nan]])
# print('data', data)
# print('data1', data.dropna())
# print('data2', data.dropna(how='all'))
# print('data3', data.dropna(axis=1, how='all'))
# 层次化索引
# data = Series(np.arange(10), index=[list('aaabbbccdd'), [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
# print(data)
# # print(np.arange(10))
# # print(list('aaabbccdd'))
# print(data.index)
# print(data['b':'d'])
# # print(data)
# print(data.ix[['b', 'd']])
# print(data[:, 2])
# print(data.unstack())
# print(data.unstack().stack())
# frame = DataFrame(np.arange(12).reshape(4, 3), columns=[['ohio', 'ohio', 'colorado'], ['green', 'red', 'green']],
#                   index=[list('aabb'), [1, 1, 2, 2]])
# print(frame)
# frame.index.names = ['key1', 'key2']
# frame.columns.names = ['state', 'color']
# print(frame)
# # print(frame.swaplevel('key1', 'key2'))
# # print(frame.stortlevel(1))
# # print(frame.swaplevel('key1', 'key2').stortlevel(0))
# print(frame.sum(level='key1'))
# print(frame.sum(level='key2'))
# print(frame.sum(level='color', axis=1))
# frame = DataFrame({'a': range(7), 'b': range(7, 0, -1), 'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
#                    'd': [0, 1, 2, 0, 1, 2, 3]})
# print(frame)
# frame2 = frame.set_index(['c', 'd'])
# print(frame2)
# frame3 = frame.set_index(['c', 'd'], drop=False)
# print(frame3)
# print(frame2.reset_index())
# frame1 = DataFrame({'key': list('bbacaab'), 'data1': range(7)})
# frame2 = DataFrame({'key': list('abd'), 'data2': range(3)})
# print(frame1)
# print(frame2)
# print(pd.merge(frame1, frame2, on='key'))
# print(pd.merge(frame2, frame1, on='key'))
# left = DataFrame({'key1': ['foo', 'foo', 'bar'],
#                   'key2': ['one', 'two', 'one'],
#                   'lval': [1, 2, 3]})
# right = DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
#                    'key2': ['one', 'one', 'one', 'two'],
#                    'rval': [4, 5, 6, 7]})
# print(pd.merge(left, right, on=['key1', 'key2'], how='outer'))
# print(pd.merge(left, right, on=['key1', 'key2'], how='left'))
# data1 = DataFrame(np.arange(6).reshape(2, 3), index=['ohio', 'colorado'], columns=['one', 'two', 'three'])
# print(data1)
# data2 = DataFrame(np.arange(6).reshape(2, 3), index=pd.Index(['ohio', 'colorado'], name='state'),
#                  columns=pd.Index(['one', 'two', 'three'], name='number'))
# print(data2)
# print(data2.stack())
# # print(data1.stack())
# print(data2.stack().unstack('number'))
# data = DataFrame({'k1': ['one']*3 + ['two']*4,
#                   'k2': [1, 1, 2, 3, 3, 4, 4]})
# print(data)
# print(data.duplicated())
# print(data.drop_duplicates())

# print(data1)
# test_test = {2: 'B', 5: 'C'}
# data1['test'] = data1['three'].map(test_test)
# print(data1)
# print(type(data1['test']))
# ages = [18, 20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
# print(len(ages))
# bins = [18, 25, 35, 60, 10000]
# cats = pd.cut(ages, bins, right=False)
# print(cats)
# print(pd.value_counts(cats))
# import requests
# import json
# url = "https://raw.githubusercontent.com/wesm/pydata-book/master/ch07/foods-2011-10-03.json"
# req = requests.get(url)
# # print(req)
# text = req.text
# with open("F:\学习\数据分析\书籍\使用案例\第七章data.json", 'w') as f:
#     json.dump(text, f)

# with open("F:\学习\数据分析\书籍\使用案例\第七章data.json", 'r') as f:
#     a = json.load(f)
#
# print(a)
import matplotlib.pyplot as plt
from numpy.random import randn
# print(np.arange(10))
# plt.plot(np.arange(10))
# plt.show()
# plt.close()
# fig = plt.figure()
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# # ax4 = fig.add_subplot(2, 2, 4)
# plt.plot(randn(50).cumsum(), 'g-')
# # _ = ax1.hist(randn(100), bins=20, color='k', alpha=0.3)
# ax1.hist(randn(100), bins=20, color='r', alpha=0.3)
# ax2.scatter(np.arange(30), np.arange(30)+3*randn(30))
# plt.show()
# # fig, axes = plt.subplots(2, 4)
# # plt.show()
# # print(axes)
# plt.plot(randn(30).cumsum(), color='k', linestyle='dashed', marker='o')
# plt.show()
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.plot(randn(1000).cumsum(), 'k', label='one')
# ax.plot(randn(1000).cumsum(), 'k--', label='two')
# ax.plot(randn(1000).cumsum(), 'k.', label='three')
# ax.legend(loc='best')
# ax.text(100, 5, 'test', family='monospace', fontsize=10)
#
# ticks = ax.set_xticks([0, 250, 500, 750, 1000])
# # labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation=30, fontsize=30)
# title = ax.set_title("my first matplotlib plot")
# x_label = ax.set_xlabel('stages')
# plt.show()

# import requests
# import json
# url = 'https://raw.githubusercontent.com/wesm/pydata-book/master/ch09/P00000001-ALL.csv'
# req = requests.get(url)
# a = req.text
# with open("F:\学习\数据分析\书籍\使用案例\竞选数据.json", 'w') as f:
#     json.dump(a, f)

# import numpy as np
#
# a = np.arange(15).reshape(3, 5)
# b = np.arange(15)
# # print(a)
# # print(a.ndim)
# # print(b.ndim)
# # print(b.shape, a.shape)
# # # help(np.size)
# # print(a.data)
# # print(a.size)
# # print(type(a))
# # print(a.itemsize)
# # print(a.dtype.name)
# #
# # # help(np.ones_like)
# # # print(np.linspace())
# # help(np.random.rand)
# # help(np.random.randn)
# b = np.arange(12).reshape(3, 4)
# print(b)
# print(b.sum(axis=0))
# print(b.sum(axis=1))
# # help(np.all)
# # print(np.all(b))
#
# #
# # def f(x, y):
# #     return 10*x+y
# #
# # b = np.fromfunction(f, (5, 4))
# # print(b)
# # print(np.ravel(b))
# # print()
# help(np.eye)


##制作mandlbort set(如何操作鼠标放大缩小)
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl


def mandelbrot(h, w, d, maxit=20):
    '''return a image of mandlbort fractal of size(h,w)'''

    y, x = np.ogrid[-1.4:1.4:h*1j, -2:0.8:w*1j]
    # print(np.ogrid[-1.4:1.4:h*1j, -2:0.8:w*1j])
    c = x+y*1j
    z = c
    divtime = maxit + np.zeros(z.shape, dtype=int)


    for i in range(maxit):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2
        div_now = diverge & (divtime == maxit)
        divtime[div_now] = i
        z[diverge] = 2
    return divtime


def on_press(event):
    global g_size
    print(event)
    print(dir(event))
    newx = event.x
    newy = event.y
    print(newx)
    print(newy)

    # 不合理的鼠标点击，直接返回，不绘制
    if newx == None or newy == None or event.dblclick == True:
        return None
    # 不合理的鼠标点击，直接返回，不绘制
    if event.button == 1:  # button ==1 代表鼠标左键按下， 是放大图像
        g_size /= 2
    elif event.button == 3:  # button == 3 代表鼠标右键按下， 是缩小图像
        g_size *= 2
    else:
        return None
    print(g_size)
    mandelbrot(newx, newy, d= g_size)


# fig, ax = pl.subplots(1)
#
# g_size = 2.5
#
# # 注册鼠标事件
# fig.canvas.mpl_connect('button_press_event', on_press)
#
#
# plt.imshow(mandelbrot(400, 400, d=2))
# plt.show()   # 目前进度，如何通过点击鼠标把on_press中的值传入mandelbrot

# a = np.arange(12).reshape(3,4)
# print(a)
# b1 = np.array([False, True, True])






