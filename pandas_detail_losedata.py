import numpy as np
import pandas as pd

dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
print(df)

print(df.dropna(axis=0,how='any'))
# 如果这个行有nan数据，就会把这行数据丢掉 how='any'表示只要有任意一个nan就会丢掉 ，how='all'只有行全部都是nan时候才会丢掉

print(df.fillna(value=0))
#  把值为nan的值全部替换成0

print(df.isnull())
# 如果缺失数据就会打印出True

print(np.any(df.isnull()) ==True)
# 如果数据特别多，表格特别大的时候，就会采用这种方式，如果有缺失，直接返回True