from self_use.s_pickle import from_pickle
from self_use.s_pickle import to_pickle
from selenium import webdriver
import pandas as pd

pandas_dict = from_pickle('./pickle1/crawl3.pkl')

'对pandas_dict做处理:to_dict'

def each_url(pandas_dict):
    '传入panads_dict,传出each url to prepare spider'
    pandasurl_dict = []
    for each in pandas_dict:
        treatmented = pandas_dict[each]
        treatmented = treatmented[['items','url']]
        treatmented = treatmented.to_dict()
        pandasurl_dict.append([each,treatmented])
    pandasurl_dict = dict(pandasurl_dict)
    return pandasurl_dict

pandasurl_dict = each_url(pandas_dict)

ff = webdriver.Firefox()

def get_num(url,turning = False):
    '输入url,xpath1,得到商品的好评数'
    try:
        ff.get(url)
        a = ff.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[1]/div[1]/div/div/div/ul/li[2]/span/span[2]/span[2]')
    except:
        a = '..'
    else:
        a = a.text
    return a

def host_crawl4(pandasurl_dict):
    '迭代法遍历所有的商品种类'
    host_list = []
    
    son1_dict = pandasurl_dict['服饰鞋包']
    item_name_list = son1_dict['items']
    url_list = son1_dict['url']
    result_list = []
    for each in range(len(url_list)):
        url = url_list[each]
        name = item_name_list[each]
        result = get_num(url)
        if result == '..':
            print(url,'有错误')

        print(name,result)
        result_list.append([name,result])
    '装载到pickle中不怕程序break了，学校的网也是真的不怎么稳定'
    to_pickle(result_list,'服饰鞋包.pkl')
    '得到result_list 后，添加到host_list中'

    return result_list
        
host_list = host_crawl4(pandasurl_dict)
