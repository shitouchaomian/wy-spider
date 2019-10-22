'做一个商品价格和评价的回归'

from self_use.s_pickle import from_pickle,to_pickle

from matplotlib import pyplot as plt

import pandas as pd

pandas = from_pickle('./pickle1/crawl5.pkl')

'散点图'

'先对一组爬虫数据进行挖掘'
pandas_1 = pandas['居家生活']

#想对price 和 评价数做一个回归模型
x = pandas_1['price']

y = pandas_1['评价数']

#爬虫失败或者xpath失败的时候数据被录入为'..'，大多是网站没有评价，替换为0

y = y.replace({'..': 0})
#x,y必须要转换成有序的int和float
x = pd.DataFrame(x,dtype = 'float')

y = pd.DataFrame(y,dtype='int')

#散点图观察
def scatter(x,y):
    fig, axes = plt.subplots(figsize=(16, 9), dpi=50)
    axes.scatter(x,y)
    plt.show()

#scatter(x,y)

#观察数据，应该是反比例函数

#进行机器学习的多项式拟合

#女朋友问我那个商品最好，那我就找出最高评价，有价值的是，网易严选没有对评价数进行索引



from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np

#直接使用机器学习的模块进行数据训练

def ploy_learn(x,y,n):
    poly_features = PolynomialFeatures(degree=n, include_bias=False)
    poly_x = poly_features.fit_transform(x)
    model = LinearRegression()
    model.fit(poly_x, y)
    x_temp = np.linspace(0, 10000, 10000000)
    x_temp = np.array(x_temp).reshape(len(x_temp), 1)
    poly_x_temp = poly_features.fit_transform(x_temp)
    plt.plot(x_temp, model.predict(poly_x_temp), 'r')
    plt.scatter(x, y)
    plt.show()

#ploy_learn(x,y,4)

#结果奇怪，准备对数据进行删除
def treatxy(x,y):
    x['saying'] = y
    xy = x
    xy = xy[x.price <6000]
    xy = xy[x.saying < 30000]
    x = xy[['price']]
    y = xy[['saying']]
    return x ,y
#x1,y1 = treatxy(x,y)
#ploy_learn(x1,y1,24)
def set_fig(x,y):
    fig, axes = plt.subplots()
    axes.scatter(x,y)
    axes.set_title('价格和评价数的关系')
    plt.show()
#总结：这个思路有问题，先做些简单的图叭


