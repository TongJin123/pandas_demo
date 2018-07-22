import pandas as pd
import numpy as np

dates = pd.date_range('20180101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
print(df)
print(df['A'],df.A)  # 选择columns中A的内容
print(df[0:3],df['20180102':'20180104'])  # 选择索引，可以通过切片，直接选择索引范围
print(df.loc['20180103'])  # 直接选择标签，可以更具体的查找
print(df.loc[:,['A','B']])  # 选择所有行和AB列的数据
print(df.loc['20180104',['A','B']])  # 查找具体行具体列的数据
print(df.iloc[3:5,1:3])  # 查找位置，可以具体查找行列的数据，可以不用切片，中间用逗号隔开
print(df.ix[3:5,['A','D']])  # g综合标签选择和位置选择，既可以选择标签，也可以选择索引
print(df[df.A>8])  # 根据比较判断来选择数据









