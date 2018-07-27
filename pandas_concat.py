import numpy as np
import pandas as pd

# concatenating
df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
res = pd.concat([df1,df2,df3],axis=0,ignore_index=True)
# 全部合并按照行的形式,ignore_index=True是把index重新排序,如果不加就是每个表的index,
print(res)

# join，['inner','outer]
df4 = pd.DataFrame(np.ones((3,4))*4,columns=['a','b','c','d'],index=[1,2,3])
df5 = pd.DataFrame(np.ones((3,4))*5,columns=['b','c','d','e'],index=[2,3,4])
# 如果只是使用concat合并，就会把没有的值设置为nan
res1 = pd.concat([df4,df5],join='inner',ignore_index=True)
# 如果加上join='inner'，就只是把两个表相同的地方合并在一起
print(res1)
res2 = pd.concat([df4,df5],axis=1,join_axes=[df4.index])
# 如果两个表的index不相同，在左右合并的时候，没有索引就用nan代替
print(res2)

# append
df6 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df7 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df8 = pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])
res3 =df6.append(df7,ignore_index=True)
res4 =df6.append([df7,df8]) # append追加数据，追加到表格下面，上下合并，如果没有对应的索引，就会添加nan

s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
res5 = df6.append(s1,ignore_index=True)  # 可以先生成一行数据，添加一行数据
print(res3,res4,res5)
