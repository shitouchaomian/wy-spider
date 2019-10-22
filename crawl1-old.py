from selenium import webdriver
import pandas as pd
import pickle
'2-1.输入url,xpath1,xpath2,获取pandas对象'
def get_items_price(url,xpath1,xpath2):
    ff = webdriver.Firefox()
    ff.get(url)

    items = ff.find_elements_by_xpath(xpath1)
    items_list=[]
    for each in items:
        items_list.append(each.text)

    price = ff.find_elements_by_xpath(xpath2)
    price_list=[]
    for each in price:
        price_list.append(each.text)
    list1 = [items_list,price_list]
    ff.quit()
    df = pd.DataFrame(list1)
    df = df.T
    df = df.rename(columns = {0:'items',1:'price'})
    return df
'1.传入需要打开的pkl,返回load结果'
def open_pickle(filename):
    with open(filename,'rb') as f:
        load_result = pickle.load(f)
    return load_result
'2.传入name_dict,处理后返回爬虫后的pandas'
def host_sp(name_dict):
    name_list = list(name_dict)
    pandas_list = []
    '利用迭代依次爬虫，存入字典'
    for each in range(len(name_list)):
        pandasob = get_items_price(name_dict[name_list[each]],xpath1,xpath2)
        pandas_list.append([name_list[each],pandasob])
        pandas_dict = dict(pandas_list)
    return pandas_dict
'3.输入sheetname的表单，文件的储存名，进行to_excel'                        
def mulsheet_excel(list1,filename):
    '[[sheetname,pandas]]'
    writer = pd.ExcelWriter(filename)
    for each in list1:
        each[1].to_excel(writer,each[0])
    writer.save()
    print(filename)
    return filename

'4.输入pandas_list,扩充类型'
def extend_pandas(pandas_dict):
    for each in pandas_dict:
        pandas_dict[each]['类型'] = pd.DataFrame([each]*len(pandas_dict[each]))
    return pandas_dict


'5.pickle.dump:传入object,命名'
def pickle_dump(obj,adress):
    with open(adress,'wb') as f:
        pickle.dump(obj,f)
    return '完成dump'

name_dict = open_pickle('./pickle1/topic_dict_url.pkl')
print('name_dict 完成')
xpath1 = '//li/div/div[2]/h4/a/span[3]'
xpath2 = '//li/div/div[2]/p/span[2]/span[2]'
print('host_sp begin')
pandas_dict = host_sp(name_dict)
print('host_sp finish')
pandas_dict_ex = extend_pandas(pandas_dict)
pickle_dump(pandas_dict_ex,'./pickle1/crawl1.pkl')


