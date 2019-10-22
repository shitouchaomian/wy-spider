from self_use.s_pickle import from_pickle
from self_use.s_pickle import to_pickle
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.options import Options
import random
#options = Options()
#num=str(float(random.randint(500,600)))
#options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/{}"," (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/{}".format(num,num))

#prefs = {"profile.managed_default_content_settings.images":2,'permissions.default.stylesheet':2}
#options.add_experimental_option("prefs", prefs)


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
ff.set_page_load_timeout(25)
ff.set_script_timeout(25)
def get_num(url,turning = False):
    '输入url,xpath1,得到商品的好评数'
    count =0
    try:
        ff.get(url)
        a = ff.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/div[1]/div[1]/div/div/div/ul/li[2]/span/span[2]/span[2]')
    except:
        a = '..'
        count += 1
    else:
        a = a.text
        count = 0
    return a

def host_crawl4(pandasurl_dict,count = 0):
    '迭代法遍历所有的商品种类'
    host_list = []
    
    for each1 in pandasurl_dict:
        
        son1_dict = pandasurl_dict[each1]
        item_name_list = son1_dict['items']
        url_list = son1_dict['url']
        result_list = []

        for each in range(len(url_list)):
            url = url_list[each]
            name = item_name_list[each]
            result = get_num(url)
            if result == '..':
                print(url,'有错误')
                count += 1
            else:
                count = 0
            print(name,result)
            result_list.append([name,result])
        print('count',count)
        if count < 50:
            to_pickle(result_list,'%s.pkl'%each1)
        
        '得到result_list 后，添加到host_list中'
        host_list.append([each1,result_list])

    
    return host_list


pandasurl_dict.pop('居家生活')
pandasurl_dict.pop('美食酒水')
pandasurl_dict.pop('服饰鞋包')


host_list = host_crawl4(pandasurl_dict)
    
    


to_pickle(host_list,'host_list.pkl')
