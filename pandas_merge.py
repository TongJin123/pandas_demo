import pandas as pd
import numpy as np

#  通过key/keys合并两个df，可能会用到数据库里面的used

left = pd.DataFrame({'key':['K0','K1','K2','K3'],
                    'A':['A0','A1','A2','A3'],
                    'B':['B0','B1','B2','B3']})
right = pd.DataFrame({'key':['K0','K1','K2','K3'],
                    'C':['C0','C1','C2','C3'],
                    'D':['D0','D1','D2','D3']})
print(left,right)
res = pd.merge(left,right,on='key')  # 基于key将两个DataFrame合并，合并之后只有一个key
# print(res)

# 合并两个key
left1 = pd.DataFrame({'key1':['K0','K1','K2','K3'],
                    'key2':['K0','K1','K0','K1'],
                    'A':['A0','A1','A2','A3'],
                    'B':['B0','B1','B2','B3']},
                     index=['a1','a2','a3','a4'])
right1 = pd.DataFrame({'key1':['K1','K1','K2','K2'],
                    'key2':['K2','K2','K1','K1'],
                    'C':['C0','C1','C2','C3'],
                    'D':['D0','D1','D2','D3']},
                    index = ['a1', 'a2', 'a5', 'a6'])
# print(left1,right1)
# how= ['left','right','inner','outer'] 选的outer不管一不一样都会打印出来，如果没有值就会打印nan
# left 就是把左边的DataFrame整个拿出来跟右边单行的做对比，如果有就打印，没有有打印nan
res1 = pd.merge(left1,right1,on=['key1','key2'],how='inner')
# 默认的inner合并，就是相同的地方合并，所以两个DataFrame的key1和key2要对应相同才会生成数据，
# 否则只会打印出columns 应为没有数据，就没有index，
# 如果一个DataFrame的key和另外DataFrame的两个key相同，则会重复打印少数key与另外一个key合并
# print(res1)

# indicator
df1 = pd.DataFrame({'coll':[0,1],'col_left':['a','b']})
df2 = pd.DataFrame({'coll':[1,2,3],'col_right':[2,2,2]})
res2 = pd.merge(df1,df2,on='coll',how='outer',indicator=True)
res3 = pd.merge(df1,df2,on='coll',how='outer',indicator='indicator_name')
# indicator显示当我合并的时候，只有left有数据或者right有数据或者两个都有数据both,可以直接命名
# print(df1,df2)
# print(res3)
res4 =pd.merge(left1,right1,left_index=True,right_index=True,how='outer')
# 根据两个DataFrame里面的index合并，outer表示不管相不相同都显示，没有数据打印nan
# print(res4)

boys = pd.DataFrame({'k':['K0','K1','K2'],'age':[1,2,3]})
girls = pd.DataFrame({'k':['K0','K0','K3'],'age':[4,5,6]})
print(boys)
print(girls)
res5 = pd.merge(boys,girls,on='k',suffixes=['_boy','_girls'],how='inner')
# suffixes就是把相同的名字内含不同的数据，用suffixes改变名字来区分这两个名字相同内含不同的数据
print(res5)