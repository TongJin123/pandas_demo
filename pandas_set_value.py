import numpy as np
import pandas as pd

dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
print(df)

df.iloc[2,2] = 1111  # 以位置的方式 把行和列的索引为2的值设置为1111  索引从0开始
print(df)

df.loc['20130101','B'] = 2222  # 以标签的方式来设置值
print(df)

# df[df.A>4] = 0  # df中A大于4的数据，整个df中A大于4的都被赋值为0
df.A[df.A>4] = 0 # 只对A这一列来说，把A大于4的数据赋值为0
print(df)

df['F'] = np.nan  # 定义一个新的列，并赋值为nan，为空，方便以后修改数据
df['E'] = pd.Series([1,2,3,4,5,6],index=pd.date_range('20130101',periods=6))
# 定义一个123456的列，为了和原先的数据对齐，必须和原数据的行的序号一样
print(df)

