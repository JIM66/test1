import numpy as np
from pandas import DataFrame,Series
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot

data = pd.read_csv("F:\学习\数据分析\书籍\使用案例\haiti.csv")
# 概览数据
print(data[['INCIDENT DATE', 'LATITUDE', 'LONGITUDE']][:10])
print(data['CATEGORY'][:10])
print(data.describe())
# 过滤错误数据
data = data[(data.LATITUDE > 18) & (data.LATITUDE < 20) & (data.LONGITUDE > -75) & (data.LONGITUDE < -70) & data.CATEGORY.notnull()]


# 获取所有分类的列表
def to_cat_list(catstr):
    stripped = (x.strip() for x in catstr.split(','))
    return [x for x in stripped if x]


# 将各个分类信息拆分为编码和英语名称
def get_all_categories(cat_series):
    cat_sets = (set(to_cat_list(x)) for x in cat_series)
    return sorted(set.union(*cat_sets))


# 获取英文名称
def get_english(cat):
    code, names = cat.split('.')
    if '|' in names:
        names = names.split(' | ')[1]
    return code, names.strip()

# def get_english(cat):
#     code, names = cat.split('.')
#     if '|' in names:
#         names = names.split(' | ')[1]
#     return code, names.strip()

# def to_cat_list(catstr):
#     stripped = (x.strip() for x in catstr.split(','))
#     return [x for x in stripped if x]
#
# def get_all_categories(cat_series):
#     cat_sets = (set(to_cat_list(x)) for x in cat_series)
#     return sorted(set.union(*cat_sets))
#


# 测试函数get_english
# print(get_english('2. Urgences logistiques | Vital Lines'))

all_cats = get_all_categories(data['CATEGORY'])
# all_cats = get_all_categories(data.CATEGORY)
# 生成器表达式
english_mapping = dict(get_english(x) for x in all_cats)
# english_mapping = dict(get_english(x) for x in all_cats)
# 测试输出
# print(english_mapping)
# print(get_english(x))
# print(all_cats)
# print(get_all_categories(all_cats))
# print(type(data.CATEGORY))
# print(type(data['CATEGORY']))
# print(english_mapping['6c'])
# print(len(english_mapping.keys()))
# for i in english_mapping.keys():
#     print(i, english_mapping[i])


# 抽取唯一的分类编码
def get_code(seq):
    return [x.split('.')[0] for x in seq if x]
all_codes = get_code(all_cats)
code_index = pd.Index(np.unique(all_codes))
print(code_index)
print(data.index)
print(len(code_index))
dummy_frame = DataFrame(np.zeros((len(data), len(code_index))), index=data.index, columns=code_index)
# print(dummy_frame)

# 将dummy_frame中适当的行变为1
for row, cat in zip(data.index, data.CATEGORY):
    codes = get_code(to_cat_list(cat))
    # print(codes)
    dummy_frame.ix[row, codes] = 1
# print(dummy_frame.shape)
data = data.join(dummy_frame.add_prefix('category_'))
# print(data.ix[:, 10:15])
# print(data.shape)
# print(data)
# 以上数据清洗完成

# 开始绘制地图
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon








