import pandas as pd
import numpy as np
import openpyxl
# 打印pandas版本
print(pd.__version__)

# 通过列表创建Series
l = [1, 2, 3, 4, 5]
s0 = pd.Series(l)
print('通过列表创建Series')
print(s0)

# 通过NumPy中的ndarray创建Series
nda = np.random.randn(5)
index = ['A', 'B', 'C', 'D', 'E']
s1 = pd.Series(nda, index = index)
print('通过NumPy中的ndarray创建Series')
print(s1)

# 通过dict来创建Series
dic = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5}
s2 = pd.Series(dic)
print('通过dict来创建Series')
print(s2)

# Series基本操作
# 修改Series索引：
print(s0)
s0.index = ['a', 'b', 'c', 'd', 'e']
print(s0)

# Series纵向合并
s3 = s2.append(s0)
print('Series纵向合并')
print(s3)

# Series按指定index delete value
s3 = s3.drop(('A'))
print('Series按指定index delete value')
print(s3)

# Series修改指定索引元素
s3['B'] = 'xxxxx'
print('Series修改指定索引元素')
print(s3)

# Series按指定索引查找元素
print('Series按指定索引查找元素')
print(s3['B'])
s3['B'] = 0

# Series切片
print('Series切片')
print(s3[: 3])

# Series加法
print('Series加法')
print(s3.add(s2))

# Series减法
print('Series减法')
print(s3.sub(s2))

# Series乘法
print('Series乘法')
print(s3.mul(s2))

# Series除法
print('Series除法')
print(s3.div(s2))

# Series计算中位数
print('Series计算中位数')
print(s3.median())

# Series求和sum
print('Series求和sum')
print(s3.sum())

# Series求max
print('Series求max')
print(s3.max())

# Series求min
print('Series求min')
print(s3.min())

print('===============DataFrame=============')
# 通过NumPy的ndarray创建DataFrame
date = pd.date_range('today', periods = 6) # 定义时间序列作为下标index
nparr = np.random.randn(6, 5)
columns = ['a', 'b', 'c', 'd', 'e']
df1 = pd.DataFrame(nparr, index = date, columns = columns)
print('通过NumPy的ndarray创建DataFrame')
print(df1)

# 通过dict创建DataFrame
data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
label = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j']
df2 = pd.DataFrame(data, index = label)
print('通过dict创建DataFrame')
print(df2)
print(df2.dtypes)

# 打印DataFrame数据结构的前3行数据：
# DataFrame.head(n): default n = 5
print('打印DataFrame数据结构的前3行数据')
print(df2.head(3))

# 打印DataFrame数据结构的后5行数据：
print('打印DataFrame数据结构的后5行数据')
print(df2.tail(5))

# 查看DataFrame index
print('查看DataFrame index')
print(df2.index)

# 查看DataFrame column name
print('DataFrame column name')
print(df2.columns)

# 查看DataFrame存储的data
print('查看DataFrame存储的data')
print(df2.values)

# 查看DataFrame 的describe(计数，最大值，最小值等参数）
print('看DataFrame 的describe')
print(df2.describe())

# DataFrmae的转置
print('DataFrmae的转置')
print(df2.T)

# 对DataFrame数据按column排序
print('对DataFrame数据按column排序')
print(df2.sort_values(by = 'visits')) # 按visits升序排列

# 对DataFrame切片
print('对DataFrame切片')
print(df2[1: 5]) # 取1～4行的数据

# 通过label查询DataFrame的每一列数据
print('通过label查询DataFrame的每一列数据')
print(df2['visits'])

# 通过lable查询DataFrame的多列数据
print('通过lable查询DataFrame的多列数据')
print(df2[['animal', 'visits']])

# 使用iloc查询DataFrame的位置
print('使用iloc查询DataFrame的位置')
print(df2.iloc[1: 5]) # 查1～4行

# copy DataFrame的一个副本
df3 = df2.copy()
print('copy DataFrame的一个副本')
print(df3)

# 判断DataFrame中的原始是否为null
print('判断DataFrame中的原始是否为null')
print(df3.isnull())

# 给DataFrame添加一列新的data new columns
print('给DataFrame添加一列新的data new columns')
new_data = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], index = df3.index)
df3['id'] = new_data
print(df3)

# 根据DataFrame的index更改元素值
df3.iat[2, 1] = 1.5
print('根据DataFrame的index更改元素值')
print(df3)

# 求DataFrame的average平均值
print('求DataFrame的average平均值')
print(df3.mean())

# 对DataFrame的任意一列进行sum求和
print('对DataFrame的任意一列进行sum求和')
print(df3['age'].sum())

# 对DataFrame的缺失值进行补充
df4 = df3.copy()
print(df4)
print(df4.fillna(value = 3))

# 删除存在缺失值的行
df5 = df3.copy()
print(df5)
print(df5.dropna(how = 'any')) # 任何存在NaN的行都会被删除

# DataFrame按照指定的列对齐
left = pd.DataFrame({'key': ['foo1', 'foo2'], 'one': [1, 2]})
right = pd.DataFrame({'key': ['foo2', 'foo3'], 'two': [4, 5]})
print(left)
print(right)

print(pd.merge(left, right, on = 'key'))

# CSV文件写入
print('CSV文件写入')
df3.to_csv('animal.csv')
print('create file success')

# CSV文件读取：
df_animal = pd.read_csv('animal.csv')
print('CSV文件读取')
print(df_animal)

# Excel写入, 注意要安装openpyxl & xlrd两个model， 使用pip install或者conda install
print('Excel写入')
df3.to_excel('animal.xlsx', sheet_name = 'Sheet1')
print('create excel file success')

# 读取Excel file
df_excel_animal = pd.read_excel('animal.xlsx', 'Sheet1', index_col = None, na_values = ['NA'])
print('读取Excel file')
print(df_excel_animal)