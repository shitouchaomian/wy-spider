from self_use.s_pickle import from_pickle
from self_use.s_pickle import to_pickle
from selenium import webdriver
import pandas as pd

'恢复crawl的dict'
ff = webdriver.Firefox()
pandas_dict = from_pickle('./pickle1/crawl1.pkl')
xpath1 = '//li/div/div[2]/h4/a/span[3]'
topic_to_url = from_pickle('./pickle1/topic_dict_url.pkl')

'计划从xpath回查更细节的分类，需要找回crawl1中的xpath1 element 对象'
##测试部分

##
'输入url和xpath1,返回所有对象'
def get_type(url,xpath1,turning = False):
    
    ff.get(url)

    items = ff.find_elements_by_xpath(xpath1)
    '迭代法对每个item回找并把text塞入列表进行返回'
    if turning:
        return items
    result_list = []
    for each in items:
        text = each.find_element_by_xpath('../../../../../../../div/p').text
        result_list.append(text)
    
    return result_list




'更改crawl1中的host_sp'
def host_sp(topic_to_url,pandas_dict,xpath1):
    '传入名称网址对应列表，传入pandas,在迭代法中进行patch'
    '利用迭代依次爬虫，处理pandas'
    for each in topic_to_url:
        result_list = get_type(topic_to_url[each],xpath1)
        pandas_dict[each]['undertype'] = pd.DataFrame(result_list)
        
    return pandas_dict
pandas_dict = host_sp(topic_to_url,pandas_dict,xpath1)

to_pickle(pandas_dict,'./pickle1/crawl2.pkl')
ff.quit()
'传入dict,规整全局数据'

'至此数据20191018'




























   


