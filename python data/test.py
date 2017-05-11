from numpy.random import randn
from pandas import DataFrame,Series
import pandas as pd
import numpy as np
from matplotlib.pyplot import plot
import matplotlib.pyplot as plt
from os import path
import matplotlib
# import mpl_toolkits
# help(mpl_toolkits)
# print(matplotlib.)
# a = 'jim    '
# print(a)
# print(a.strip())
# print(np.zeros((3, 4)))
# # print(DataFrame(np.zeros(3, 4)))
# # def to_cat_list(catstr):
# #     stripped = (x.strip() for x in catstr.split(','))
# #     return [x for x in stripped if x]
# #
# # def get_all_categories(cat_series):
# #     cat_sets = (set(to_cat_list(x)) for x in cat_series)
# #     return sorted(set.union(*cat_sets))
# #
# # def get_english(cat):
# #     code, names = cat.split('.')
# #     if '|' in names:
# #         names = names.split(' | ')[1]
# #     return code, names.strip()
#
# help(DataFrame.add_prefix)
# df = DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
#                 'key2': ['one', 'two', 'one', 'two', 'one'],
#                 'data1': np.arange(5),
#                 'data2': np.random.randn(5)})
#
# print(df)
# grouped = df['data1'].groupby(df['key1'])
# print(grouped)
# print(grouped.mean())
# mean = df['data1'].groupby([df['key1'], df['key2']]).mean()
# print(mean)
# print(mean.unstack())
# std = df['data1'].groupby([df['key1'], df['key2']]).std()
# print(std)
# help(DataFrame.add_prefix)
# help(pd.cut)

# 随机采样和排列
# 红桃（red）/黑桃（Spades）/梅花（Clubs）/方片（Diamonds）
# suits = ['H', 'S', 'C', 'D']
# # card_val = (range(2, 11) + [10]*3)*4
# card_val = (range(1, 11) + [10] * 3) * 4
# base_names = ['A'] + range(2, 11) + ['J', 'Q', 'K']
# cards = []
# for suit in suits:
#     cards .extend(str(num) + suit for num in base_names)
# deck = Series(card_val, index=cards)
#
# print(deck)

# suits = ['H', 'S', 'C', 'D']
# card_val = [i for i in range(1, 11)] + [10] * 3 * 4
# base_names = ['A'] + range(2, 11) + ['J', 'K', 'Q']
# cards = []
# for suit in ['H', 'S', 'C', 'D']:
#     cards.extend(str(num) + suit for num in base_names)
#
# # deck = Series(card_val, index=cards)
# close_px = pd.read_csv('F:\学习\数据分析\书籍\使用案例\stock_px.csv', parse_dates=True, index_col=0)
# # print(close_px)
# # print(close_px.describe())
# rets = close_px.pct_change().dropna()
# spx_corr = lambda x: x.corrwith(x['SPX'])
# by_year = rets.groupby(lambda x: x.year)
# print(by_year.apply(spx_corr))
# a_data = by_year.apply(spx_corr)
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.plot(a_data['AAPL'], 'k--', label='SPX_CORR_APPL', color='r')
# ticks = ax.set_xticks([2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011])
# # ticks = ax.set_xticks([0, 250, 500, 750, 1000])
# # print(a_data.index)
# ax.legend(loc='upper left')
# plt.show()

# from dateutil.parser import parse
# a = parse('6/12/2013', dayfirst=True)
# print(a)
#
# datestrs = ['7/6/2016', '8/5/2017']
# b = pd.to_datetime(datestrs,dayfirst=True)
# print(b)
# c = pd.to_datetime(datestrs, dayfirst=False)
# print(c)
# # help(pd.to_datetime)
# d = pd.to_datetime(datestrs)
# print(d)
# from datetime import datetime
# dates = [datetime(2011, 1, 2), datetime(2011, 1, 5), datetime(2011, 1, 7), datetime(2011, 1, 8),
#          datetime(2011, 1, 10), datetime(2011, 1, 12)]
# ts = Series(np.random.randn(6), index=dates)
# # print(ts)
# # print(type(ts))
# # print(ts.index)
# # print(ts + ts[::2])
# # print(ts[::2])
# stamp = ts.index[2]
# # print(stamp)
# # print(ts[stamp])
# longer_ts = Series(np.random.randn(1000), index=pd.date_range('2000/1/1', periods=1000))
# # print(longer_ts)
# print(longer_ts['2001'])
#
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.plot(longer_ts, 'k--', label='ts.series', color='r')
#
# ax.legend(loc='upper left')
# plt.show()
# ts = Series(np.random.randn(4), index=pd.date_range('2000/1/1', periods=4, freq='M'))
# print(ts)
# ts.shift
# data = pd.read_csv("F:\学习\数据分析\书籍\使用案例\P00000001-ALL.csv")
# print(data[['']][:10])
# data = pd.DataFrame(np.range(10), columns=)
# data = pd.read_csv("F:\学习\数据分析\书籍\使用案例\P00000001-AL.csv")
# print(data[data.columns][:10])
# # print(data['contb_receipt_amt'])
# print(data.columns)
# # print(data['contbr_employer'].groupby())
# # help(DataFrame.groupby)
# print(set(data['contbr_employer'].values))
# # print(type(data['contbr_employer']))
#
# # 第十一章 金融和经济数据应用
# stock_price = pd.read_csv('F:\学习\数据分析\书籍\使用案例\stock_px(11).csv', encoding='gbk')
# stock_volume = pd.read_csv('F:\学习\数据分析\书籍\使用案例\交易数量.csv', encoding='gbk')
# # print(stock_price[stock_price.columns][:10])
# # print(stock_price[stock_price.columns][:10])
# prices = stock_price[stock_price.columns][:10]
# volume = stock_price[stock_price.columns][:10]
# print(type(prices))
# print(type(volume))

# vwap = (prices * volume).sum()/volume.sum()
# print(vwap)

# a = 'jiang'
# print(a*3)
# b = list(a)
# print(b)
# b[1] = 2
# print(a[1])
# print(b[1])
# help(str.replace)
# # import string
# # help(string)
# my_set = {1, 2, 3, 4, 5}
# print(my_set)
# for i , j in enumerate(b):
#     print(i, j)
#
# # print(enumerate(b))
# # print(dir(enumerate(b)))
# help(input)
# import math
# a = 1
# if a < 0:
#     raise RuntimeError("you can't input a negative number")
# else:
#     print(math.sqrt(a))
# import time
# a = "1/2"
#
#
# def get_num(num):
#     b = str(a).split("/")
#     # print(b)
#     return b[0]
#
# print(get_num(a))
# print(time.time())
import time


def test1(n):
    start = time.time()
    lst = []
    for i in range(n*10000):
        lst = lst + [i]
    end = time.time()
    return n, end-start


def test2(n):
    start = time.time()
    lst = []
    for i in range(n*10000):
        lst.append(i)
    end = time.time()
    return n, end-start


def test3(n):
    start = time.time()
    lst = [i for i in range(n*10000)]
    end = time.time()
    return n, end-start


def test4(n):
    start = time.time()
    lst = list(range(n*10000))
    end = time.time()
    return n, end-start, start, end

# n_list = [10, 30, 50, 10000]
# for n in n_list:
#     # print('test1', test1(n))
#     print('test2', test2(n))
#     print('test3', test3(n))
#     print('test4', test4(n))
# print(test4(10000))
# print(help(int))



class Rational:

    def __init__(self, num, den=1):
        self.num = num
        self.den = den

    def plus(another):
        den = another.num*another.den
        num = (another.num*another.den + another.den*another.num)
        return Rational(num, den)

    def print(self):
        return str(self.num)+"/"+str(self.den)


# r1 = Rational(3, 5)
# r2 = Rational(4, 6)
# # print(r1.print())
# # print(r1.plus(r2))
# # X = Rational()
# a = 'test1'
# b = 'test2'
# print(','.join(a+b))


# 2.5学校人事管理系统中的类
import datetime


# 定义共同类别
class PersonTypeError(TypeError):
    pass


class PersonValueError(ValueError):
    pass


class Person:
    _num = 0

    def __init__(self, name, sex, birthday, ident):
        if not (isinstance(name, str) and sex in ("女", "男")):
            raise PersonTypeError(name, sex)
        try:
            birth = datetime.date(*birthday)
        except:
            raise PersonValueError("Wrong date:", birthday)
        self._name = name
        self._sex = sex
        self._birthday = birth
        self._id = ident
        Person._num += 1

    def id(self):
        return self._id

    def name(self):
        return self._name

    def sex(self):
        return self._sex

    def birthday(self):
        return self._birthday

    def age(self):
        return (datetime.date.today().year-self._birthday.year)

    def set_name(self, name):
        if not isinstance(name, str):
            raise PersonValueError("set_name", name)
        self._name = name

    def __lt__(self, other):
        if not isinstance(other, Person):
            raise PersonTypeError(other)
        return self._id < other._id

    @classmethod
    def num(cls):
        return Person._num

    def __str__(self):
        return " ".join((self._id, self._name, self._sex, str(self.birthday)))

    def details(self):
        return ",".join(("编号：" + self._id, "姓名：" + self._name, "性别："+self._sex,
                         "出生日期："+str(self._birthday), "年龄"+str(self.age())))


p1 = Person("谢洁雨", "女", (1995, 7, 30), "1201510111")
p2 = Person("汪力强", "男", (1990, 2, 17), "1201380324")
p3 = Person("张子玉", "女", (1974, 10, 16), "0197401032")
plist = [p1, p2, p3]
# for p in plist:
#     print(p.details())
#
# plist.sort()
# for p in plist:
#     print(p.details())


# 定义学生类
class Student(Person):
    _id_num = 0

    @classmethod
    def _id_gen(cls):
        cls._id_num += 1
        year = datetime.date.today().year
        return "1{:04}{:05}".format(year, cls._id_num)

    def __init__(self, name, sex, birthday, department):
        Person.__init__(self, name, sex, birthday, Student._id_gen())
        self._department = department
        self._enroll_date = datetime.date.today()
        self._courses = {}

    def set_course(self, course_name):
        self._courses[course_name] = None

    def set_score(self, course_name, score):
        if course_name not in self._courses:
            raise PersonValueError("NOT this course selected:", course_name)
        self._courses[course_name] = score

    def scores(self):
        return [(cname, self._courses[cname]) for cname in self._courses]

    def details(self):
        return ", ".join(Person.details(self), "入学日期："+str(self._enroll_date), "院系："+self._department,
                         "课程记录："+str(self ._courses))


# 定义教师类
class Staff(Person):
    _id_num = 0

    @classmethod
    def _id_gen(cls, birthday):
        cls._id_num += 1
        birth_year = datetime.date(*birthday).year
        return "0{:04}{:05}".format(birth_year, cls._id_num)

    def __init__(self, name, sex, birthday, entry_date=None):
        super().__init__(name, sex, birthday, Staff._id_gen(birthday))  # 请注意：派生类覆盖了基类的同名方法。如果从self出发调用details, 实际调用的将是本类的details
        # ,要调用基类的同名方法，必须通过基类的名字或super函授
        if entry_date:
            try:
                self._entry_date = datetime.date(*entry_date)
            except:
                raise PersonTypeError("Wrong date:", entry_date)
        else:
            self._entry_date = datetime.date.today()
        self._salary = 1720
        self._department = "未定"
        self._position = "未定"

    def set_salary(self, amount):
        if not type(amount) is int:
            raise TypeError
        self._salary = amount

    def set_position(self, position):
        self._position = position

    def set_department(self, department):
        self._department = department

    def details(self):
        return ",".join((super().details(), "入职日期："+str(self._entry_date), "院系："+str(self._department),
                        ("职位："+self._position), "工资："+str(self._salary)))  # 使用super不需要使用self

p1 = Staff("张子玉", "女", (1974, 10, 16))
p2 = Staff("李国栋", "男", (1962, 5, 24))
# print(p1)
# print(p2)
#
# p1.set_department("数学")
# p1.set_salary(8400)
# p1.set_position("副教授")
#
# print(p1.details())
# print(p2.details())
#
#
# help(list)


# 链接结构

class LinkedListUnderflow(ValueError):
    pass


class LNode:
    def __init__(self, elem, _next=None):
        self.elem = elem
        self.next = _next


class LList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = LNode(elem, self._head)  # LNode没有这个模块

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow
        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last")
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def find(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):   # 这里没有看懂
                return p.elem
            p = p.next

    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end="")
            if p.next is not None:
                print(", ", end="")
            p = p.next
        print("")

    def for_each(self, proc):
        p = self._head
        while p is None:
            proc(p.elem)
            p = p.next

    def elements(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    def find_all(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next

# mlist1 = LList()
# for i in range(0, 100000):
#     mlist1.prepend(i)
# for i in range(11, 20):
#     mlist1.append(i)
# mlist1.printall()
# # print(mlist1.find(20))  # find如何使用


# 定义单链表
# class LList1(LList):
#
#     def __init__(self):
#         LList.__init__(self)
#         self._rear = None
#
#     def prepend(self, elem):
# for num in range(10, 1, -1):
#     print('a',num,sep="b")
#     print('a', num)
#
# help(print)
# a = 'jiang'
# print(a[0:2])
#
# a = [-1]
# print(a*10)

# KMP算法
def matching_kmp(t, p, pnext):
    """kmp串匹配， 主函数"""
    j, i = 0, 0
    n, m = len(t), len(p)
    while j< n and i<m:
        if i == -1 or t[j] == p[i]:
            j, i = j+1, i+1
        else:
            i = pnext[i]
    if i == m:
        return j-1
    return -1


# 构造pnext列表
def gen_pnext(p):
    i, k, m = 0, -1, len(p)
    pnext = [-1]*m
    while i < m-1:
        if k == -1 or p[i] == p[k]:
           i, k = i+1, k+1
           pnext[i] = k
        else:
            k = pnext[k]
    return pnext


def gen_pnext1(p):
    """
    获取pnext列表的改进算法，对于和目标字符串中，如果字符和匹配失败字符相同时，直接对pnext[i]进行赋值
    :param p:
    :return:
    """
    i, k, m = 0, -1, len(p)
    pnext = [-1]*m
    while i < m-1:
        if k == -1 or p[i] == p[k]:
            i, k = i+1, k+1
            if p[i] == p[k]:
                pnext[i] = pnext[k]
            else:
                pnext[i] = k
        else:
            k = pnext[k]
    return pnext

# p = 'abbcabcaabbcaa'
# print(gen_pnext(p))
# print(len(gen_pnext(p)))
# print(gen_pnext1(p))
# print(len(gen_pnext1(p)))




# i, k, m = 0, -1, len(p)
# pnext = [-1] * m
# while i < m - 1:
#     print("i", i)
#     print("k", k)
#     print("p[%i]" % i, p[i])
#     print("k", k, p[k])
#     # print("p[sk]" &str(k), p[k])
#     if k == -1 or p[i] == p[k]:
#         i, k = i + 1, k + 1
#         pnext[i] = k
#
#     else:
#         k = pnext[k]
#     print(pnext)

# 二叉树的list实现

def BinTree(data, left = None, right = None):
    return [data, left, right]


def is_empty_BinTree(bTree):
    return bTree is None


def root(btree):
    return btree[0]


def left(btree):
    return btree[1]


def right(btree):
    return btree[2]


def set_root(btree, data):
    btree[0] = data
    return btree


def set_left(btree, left):
    btree[1] = left
    return btree


def set_right(btree, right):
    btree[2] = right
    return btree


# t1 = BinTree(2, BinTree(4), BinTree(5))
# print(t1)

# 实现优先队列
class PrioQueueError(ValueError):
    pass


class PrioQue:

    def __init__(self, elist = []):
        self._elems = list(elist)
        self._elems.sort(reverse=True)

    def enqueue(self, e):
        i = len(self._elems) -1
        while i >= 0:
            if self._elems[i] <= e:
                i -= 1
            else:
                break
        self._elems.insert(i+1, e)

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError
        return self._elems[-1]

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError
        return self._elems.pop()

# import math
# t = math.log(5,2)
# t1 = math.log(5)
# print(t)
# print(t1)
# print(math.e)
# print(math.e**t1)


class PrioQueue:
    """
    使用堆构造树排序
    """
    def __init__(self, elist = []):
        self._elems = list(elist)
        if elist:
            self.bulidheap()

    def is_empty(self):
        return not self._elems

    def bulidheap(self):
        end = len(self._elems)
        for i in range(end//2, -1, -1):
            self.siftdown(self._elemsp[i], i, end)

    def peek(self):
        if self.is_empty():
            raise PrioQueueError("in peek")
        return self._elems[0]

    def siftup(self, e, last):
        elems, i, j = self._elems, last, (last-1)/2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j-1)/2
        elems[i] = e

    def siftdown(self, e, begin, end):
        elems, i, j, = self._elems, begin, begin*+1
        while j < end:
            if j+1 < end and elems[j+1] <elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, 2*j + 1
        elems[i] = e

    def enqueue(self, e):
        self._elems.append(None)
        self.siftup(e, len(self._elems) - 1)

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError("in dequeue")
        elems = self._elems
        e0 = elems[0]
        e = elems.pop()
        if len(elems) > 0:
            self.siftdown(e, 0, len(elems))
        return e0


# 构建通用模拟器类
from random import randint


#  二叉树的链接实现

class BinTNode:
    def __init__(self, dat, left=None, right=None):
        self.data = dat
        self.left = left
        self.right = right


def count_BinTNodes(t): #  定义结点计数函数
    if t is None:
        return 0
    else:
        return 1+count_BinTNodes(t.left)+count_BinTNodes(t.right)


def sum_BinTNodes(t):
    if t is None:
        return 0
    else:
        return t.dat + sum_BinTNodes(t.left) + sum_BinTNodes(t.right)


t = BinTNode(1, BinTNode(2), BinTNode(3))

# print(t)
# print(count_BinTNodes(t))
# # print(sum_BinTNodes(t))
# w = {1, 2, 3, 4, 5, 6}
# print(max(w))
# print(ord('a'))

import numpy as np
import pylab as pl
import time
from matplotlib import cm
from math import log

escape_radius = 10
iter_num = 20


def draw_mandelbrot2(cx, cy, d, N=600):
    global mandelbrot
    """
    绘制点(cx, cy)附近正负d的范围的Mandelbrot
    """
    x0, x1, y0, y1 = cx - d, cx + d, cy - d, cy + d
    y, x = np.ogrid[y0:y1:N * 1j, x0:x1:N * 1j]
    c = x + y * 1j

    smooth_mand = np.frompyfunc(smooth_iter_point, 1, 1)(c).astype(np.float)
    pl.gca().set_axis_off()
    pl.imshow(smooth_mand, cmap=cm.Blues_r, extent=[x0, x1, y1, y0])
    pl.show()


def smooth_iter_point(c):
    z = c  # 赋初值
    d = 1 + 2j  # 这里，把幂运算的指数，设定成复数1+2j， 就是广义mandelbrot集合， d=2就是标准mandelbrot集，d=3就是三阶的
    for i in range(1, iter_num):
        if abs(z) > escape_radius: break
        z = z ** d + c  # **运算符是幂运算
    # 下面是重新计算迭代次数，可以获取连续的迭代次数（即正规化）
    absz = abs(z)  # 复数的模
    if absz > 2.0:
        mu = i - log(log(abs(z), 2), 2)
    else:
        mu = i
    return mu  # 返回正规化的迭代次数




# 鼠标点击触发执行的函数
def on_press(event):
    global g_size
    print(event)
    print(dir(event))
    newx = event.xdata
    newy = event.ydata
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

    draw_mandelbrot2(newx, newy, g_size)


fig, ax = pl.subplots(1)

g_size = 2.5

# 注册鼠标事件
fig.canvas.mpl_connect('button_press_event', on_press)

# 初始绘制一个图
draw_mandelbrot2(0, 0, g_size)












