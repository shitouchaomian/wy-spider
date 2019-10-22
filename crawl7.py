from self_use.s_pickle import from_pickle,to_pickle

from matplotlib import pyplot as plt

import pandas as pd

import seaborn as sns

'价格分布直方图'
pandas_1 = from_pickle('./pickle1/crawl5.pkl')



#测试部分
'抽调一组数据（），抽调price,替换price的缺失值，改变price的dtype'
def test_clean(pandas_1,num):
    table1 = pandas_1[list(pandas_1)[num]]
    price = table1[['price']]
    price.replace({'..':0})
    price = pd.DataFrame(price,dtype = 'float')
    return price
price = test_clean(pandas_1,6)



'seaborn不适合这种制图，不是非常的严谨，虽然好看'
###弃用

###直方图测试

def hist_m(data):
    fig, ax = plt.subplots()
    max_d = float(data.mean()[0]*5)
    data = data[data.price<max_d]
    ax.hist(data.price,80000//len(data.price),density=1,color = 'r')
    ax.set_xticks([each for each in range(0,int(max_d),int(max_d//20))])
    ax.set_xlim((0,max_d))
    plt.show()
hist_m(price)

#比较满意的图
