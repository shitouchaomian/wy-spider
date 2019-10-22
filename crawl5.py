from self_use.s_pickle import from_pickle,to_pickle
import pandas as pd
a = ['个护清洁.pkl', '全球特色.pkl', '居家生活.pkl', '数码家电.pkl', '服饰鞋包.pkl', '母婴亲子.pkl', '美食酒水.pkl', '运动旅行.pkl']
pandas = from_pickle('./pickle1/crawl3.pkl')
for each in a:
    for_pandas = each.split('.')[0]
    pandas_each = pandas[for_pandas]
    data_frame = from_pickle('./pickle1/crawl4/%s'%each)
    pandas_row = pd.DataFrame(data_frame)
    pandas_each['评价数']= pandas_row[[1]]
'爬的东西差不多了，做个可视化叭'
to_pickle(pandas,'./pickle1/crawl5.pkl')
