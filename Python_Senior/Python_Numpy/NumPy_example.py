import numpy as np

# 创建数组：
array1 = np.array([1, 2, 3]) # 创建一个一维数组，只有一个轴，轴的长度为3
print(array1)

# 通过列表创建二维数组：
print(np.array([(1, 2, 3), (4, 5, 6)])) # 2x3的数组

# 创建全为0的二维数组：
print(np.zeros((3, 3))) # 3x3的零矩阵

# 创建全为1的三维矩阵：
print(np.ones((2, 3, 4))) # 2x3x4的元素全为1的矩阵

# 创建一维等差数组：
print(np.arange(10))

# 创建二维等差数组：
print(np.arange(6).reshape(2, 3)) # 创建2x3的等差数组

# 创建单位矩阵（二维数组）：
print(np.eye(3))

# 创建间隔一维数组：
print(np.linspace(1, 10, num = 6))

# 创建二维随机数组
print(np.random.rand(2, 3))

# 创建二维随机整数数组（数值小于5）
print(np.random.randint(5, size = (2, 3)))

# 依据自定义函数创建数组（lambda表达式）：
print(np.fromfunction(lambda x, y: x + y, (3, 3)))

# 生成一维数组a, b后进行数组运算：
a = np.array([10, 20, 30, 40, 50])
b = np.arange(1, 6)
print(a)
print(b)

# add加法运算：
print(a + b)

# sub减法运算：
print(a - b)

# Multiply乘法运算：
print(a * b)

# divide除法运算：
print(a / b)
print('以上操作均在一维数组上进行')

# 生成二维数组A， B进行数组运算：
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A)
print(B)

# add:
print(A + B)

# sub:
print(A - B)

# multiply矩阵元素之间的乘法:
print(A * B)

# 矩阵乘法运算：
print(np.dot(A, B))

# 或者将A， B转为matrix矩阵再直接相乘
print(np.mat(A) * np.mat(B))

# 数乘矩阵：
print(20 * A)

# 矩阵的转置：
print(A.T)

# 矩阵求逆：
print(np.linalg.inv(A))

print('以上操作均在二维数组或矩阵中进行')

