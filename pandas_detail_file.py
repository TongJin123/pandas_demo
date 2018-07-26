import numpy as np
import pandas as pd

data = pd.read_csv('student.csv')  # 从文件中获取数据,还有很多格式能够提取数据

data.to_pickle('students.pickle')  # 到处数据到什么格式的文件中，直接在当前目录下面生成文件

print(data)