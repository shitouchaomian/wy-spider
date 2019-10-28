from self_use.s_pickle import from_pickle,to_pickle
from selenium import webdriver

import pandas as pd

import numpy as np

pandas_1 = from_pickle('./pickle1/crawl5.pkl')
def change_to_pandas_2(pandas_1):
    '置入到整个pandas中而不是用字典储存'
    list_concat = []

    for each in pandas_1:
        list_concat.append(pandas_1[each])

    pandas_2 = pd.concat(list_concat,axis = 0)

    new = list(range(len(pandas_2)))

    new_arr = np.array(new)

    pandas_2['newindex'] = new_arr

    pandas_2 = pandas_2.set_index('newindex')
    return pandas_2


pandas_2 = change_to_pandas_2(pandas_1)

#to_pickle(pandas_2,'./pickle1/pandas_2')

ff = webdriver.Firefox()
ff.set_page_load_timeout(25)
ff.set_script_timeout(25)
list_price= []
list_evaluate = []



for each in pandas_2['url']:
    try:
        ff.get(each)
    except:
        print('get出错')
        list_price.append(0)
        list_evaluate.append(0)
    else:
        try:
            new_price = ff.find_elements_by_xpath("//div[2]/div/div/div/span/span[@class='num']")[0].text
            
        except:
            new_price = 0
            print('出错')
        else:
            print(each,new_price)
        try:
            new_evaluate = ff.find_elements_by_xpath('//div/div/div/div/ul/li[2]/span/span[2]/span[2]')[0].text
            
        except:
            new_evaluate = 0
            print('出错')
        else:
            print(each,new_evaluate)
        list_price.append(new_price)
        list_evaluate.append(new_evaluate)

list_price = np.array(list_price)
list_evaluate = np.array(list_evaluate)

to_pickle(list_price,'list_price')
to_pickle(list_evaluate,'list_evaluate')

pandas_2['price.10.27'] = list_price
pandas_2['evaluate.10.27'] = list_evaluate


