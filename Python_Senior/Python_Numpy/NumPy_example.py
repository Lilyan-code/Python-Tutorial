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

# 数学函数
print('Math Function example')
# 三角函数：
print(a)

print(np.sin(a))

# 以自然对数为底的指数函数e^x：
print(np.exp(a))

# 数组的开平方根
print(np.sqrt(a))

# 数组的切片 and 索引
print('Array split & index')

# 一维数组index
a = np.array([1, 2, 3, 4, 5])
print(a[0])
print(a[-3])

# 一维数组split
print(a[0: 2])
print(a[: -1])

# 二维数组index：
a = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(a[0])
print(a[-1])

# 二维数组split：
print(a[:, -1])  # 二维数组切片需要用,区分行列这里是最后一列的意思

# 数组外形操作：
print('Array Shape')

# 查看数组形状：
a = np.random.random((3, 2))
print(a)
print(a.shape)

# 更改数组形状（不改变原始数组的形状）：
print(a.reshape(2, 3))
print(a)
# 更改数组形状（改变原始数组的形状）
print(a.resize(2, 3))
print(a)

# 展平数组 将多维数组转换为一维数组
print(a.ravel())

# 垂直合并数组
a = np.random.randint(10, size = (3, 3))
b = np.random.randint(10, size = (3, 3))
print(a)
print(b)

print(np.vstack((a, b)))

# 水平合并数组：
print(np.hstack((a, b)))

# 沿x轴切分数组：
print(np.vsplit(a, 3)) # 将a切分成三个行向量（一维数组）

# 沿y轴切分数组：
print(np.hsplit(a, 3)) # 将a切分成三个列向量（一维数组）

# 数组排序
a = np.array(([1, 4, 3], [6, 2, 0], [9, 7, 5]))
print(a)

# 返回数组每一列的最大值：
print(np.max(a, axis = 0))

# 返回数组每一行的最小值：
print(np.min(a, axis = 1))

# 返回数组每一列最大元素的index：
print(np.argmax(a, axis = 0))

# 返回数组每一行最小元素的index：
print(np.argmin(a, axis = 1))

# Array Count
print('Array Count')

# 统计数组每一列的中位数
print(np.median(a, axis = 0))

# 统计数组各行的sqrt
print(np.mean(a, axis = 1))

# 统计数组每一列的average：
print(np.average(a, axis = 0))

# 统计数组各行的方差：
print(np.var(a, axis = 1))

# 统计数组每一列的标准偏差：
print(np.std(a, axis = 0))

# 创建一个6x6的二维数组，边界值全为1，Other Value is 0：
Z = np.ones((6, 6))
Z[1: -1, 1: -1] = 0
print(Z)

# 使用数字0将一个全为1的6x6的二维数组包围
Z = np.ones((6, 6))
Z = np.pad(Z, pad_width = 1, mode = 'constant', constant_values = 0)
'''
Examples
    --------
    >>> x = np.arange(9).reshape((3,3))
    >>> x
    array([[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8]])

    >>> np.diag(x)
    array([0, 4, 8])
    >>> np.diag(x, k=1)
    array([1, 5])
    >>> np.diag(x, k=-1)
    array([3, 7])

    >>> np.diag(np.diag(x))
    array([[0, 0, 0],
           [0, 4, 0],
           [0, 0, 8]])

'''
# 创建一个6x6的二维数组，并设置1，2，3，4，5落在对角线下方：
Z = np.diag(1 + np.arange(5), k = -1) # k = 1主对角线 k = -1副对角线
print(Z)

# 创建一个10x10的二维数组，并使得1和0沿对角线间隔放置：
Z = np.zeros((10, 10), dtype = int)
Z[1::2, ::2] = 1
Z[::2, 1::2] = 1
print(Z)

# 创建一个0 - 10的一个一维数组， 并将(1, 9]之间的全部数值转换成负数
Z = np.arange(11)
print(Z)
Z[(1 < Z) & (Z <= 9)] *= -1
print(Z)

# 找出两个一维数组中相同的元素：
Z1 = np.random.randint(0, 10, 10)
Z2 = np.random.randint(0, 10, 10)
print("Z1:", Z1)
print("Z2:", Z2)
print(np.intersect1d(Z1, Z2)) # 找出Z1和Z2中的相同元素

# 使用NumPy打印yesterday， today， tomorrow
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
today = np.datetime64('today', 'D')
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print("yesterday: ", yesterday)
print("today: ", today)
print("tomorrow: ", tomorrow)

# 使用五种不同的方法提取一个随机数组的整数部分
Z = np.random.uniform(0, 10, 10)
print('init:', Z)
print('way 1:', Z - Z % 1)
print('way 2:', np.floor(Z))
print('way 3:', np.ceil(Z) - 1)
print('Way 4:', Z.astype(int))
print('Way 5:', np.trunc(Z))

# 创建一个5x5的矩阵，其中每行的数值范围从1～5：
Z = np.zeros((5, 5))
Z += np.arange(1, 6)
print(Z)

# 创建一个长度为5的等间隔一维数组，其值域（0，1）：
# linspace的功能是返回指定区域间隔的数组，endpoint = True说明右半区间是闭合边界可以取到
Z = np.linspace(0, 1, 6, endpoint = False)[1:]
print(Z)

# 创建一个长度为10的一维数组，并将其按升序排序：
Z = np.random.random(10)
Z.sort()
print(Z)

# 创建一个4x4的二维数组，并按照列进行升序排序
Z = np.array([[7, 4, 3], [3, 1, 2], [4, 2, 6]])
print("original array:\n", Z)
Z.sort(axis = 0)
print(Z)

# 创建一个长度为5的一维数组，并将其中最大值替换为0
Z = np.random.random(5)
print('Original Array:\n', Z)
Z[Z.argmax()] = 0
print(Z)

# 打印每个NumPy标量类型的min and max：
for dtype in [np.int8, np.int32, np.int64]:
    print("The minimum value of {}: ".format(dtype), np.iinfo(dtype).min)
    print("The maximum value of {}: ".format(dtype), np.iinfo(dtype).max)
for dtype in [np.float32, np.float64]:
    print("The minimum value of {}: ".format(dtype), np.finfo(dtype).min)
    print("The maximum value of {}: ".format(dtype), np.finfo(dtype).max)

# 将float32转换为整型：
Z = np.arange(10, dtype = np.float32)
print(Z)

Z = Z.astype(np.int32, copy = False) # copy = False：返回输入数组的副本，否则创建一个新的数组返回
print(Z)

# 将随机二维数组按照第3列从上到下进行升序排序：
Z = np.random.randint(0, 10, (5, 5)) # 返回5x5的二维数组，里面的元素为0~9
print("排序前：\n", Z)
print(Z[Z[:, 2].argsort()]) # 因为按照第三列排序，排序移动的是每一个行向量

# 从随机一维数组中找出距离给定数值（0.5)最近的数：
Z = np.random.uniform(0, 1, 20)
print('random array:\n', Z)
z = 0.5
m = Z.flat[np.abs(Z - z).argmin()]
print(m)

# 将二维数组的前两行进行顺序交换
Z = np.arange(25).reshape(5, 5)
print(Z)
Z[[0, 1]] = Z[[1, 0]]
print(Z)

# 找出随机一维数组中出现频率最高的值
Z = np.random.randint(0, 10, 50)
print('random array：', Z)
print(np.bincount(Z).argmax())

# 找出给定一维数组中非0元素的index：
Z = np.nonzero([1, 1, 1, 1, 0, 0, -1, 0])
print(Z)

# 给定5x5的二维数组，在其内部随机放置p个值为1的数：
p = 3
Z = np.zeros((5, 5))
np.put(Z, np.random.choice(range(5 * 5), p, replace = False), 1)
print(Z)

# 随机的3x3二维数组，减去数组每一行的average：
X = np.random.rand(3, 3)
print(X)

Y = X - X.mean(axis = 1, keepdims = True)
print(Y)

# 获得二维数组点积结果的对角线数组：
X = np.random.uniform(0, 1, (3, 3))
Y = np.random.uniform(0, 1, (3, 3))
print(np.dot(X, Y))
print('speed lower:')
# speed low way:
print(np.diag(np.dot(X, Y)))
# speed quicker way:
print('speed quicker:')
print(np.einsum("ij, ji->i", X, Y))

# 找到随机一维数组前p个最大值
Z = np.random.randint(1, 100, 100)
print(Z)

p = 5
print(Z[np.argsort(Z)[-p: ]])

# 将二维数组中所有元素保留两位小数：
Z = np.random.random((5, 5))
print(Z)

np.set_printoptions(precision = 2)
print(Z)

# 使用科学计数法输出数组：
Z = np.random.random([5, 5])
print(Z)
print(Z / 1e3)

# 使用NumPy找出百分位数：
a = np.arange(15)
print(a)

print(np.percentile(a, q = [25, 50, 75]))

# 找出数组中缺失值的总数以及所在的位置
Z = np.random.rand(10, 10)
print("Z:\n", Z)
Z[np.random.randint(10, size = 5), np.random.randint(10, size = 5)] = np.nan
print(Z)

# 从随机数组中删除包含缺失值的行：
print(np.sum(np.isnan(Z), axis = 1) == 0)

# 统计随机数组中的各元素的数量：
Z = np.random.randint(0, 100, 25).reshape(5, 5)
print(Z)
print(np.unique(Z, return_counts = True))

# 将数组中各元素按指定分类转换为文本值
Z = np.random.randint(1, 4, 10)
print(Z)

label_map = {1: 'car', 2: 'bus', 3:'train'}
print([label_map[x] for x in Z])

# 打印各元素在数组中升序排列的index：
Z = np.random.randint(100, size = 10)
print('Array:', Z)
print(Z.argsort())

# 得到二维随机数组各行的最大值max：
Z = np.random.randint(1, 100, [5, 5])
print(Z)
print(np.amax(Z, axis = 1))

# 得到二维随机数组各行的最小值min：
Z = np.random.randint(1, 100, [5, 5])
print(Z)
print(np.apply_along_axis(np.min, arr = Z, axis = 1))

# 计算两个数组之间的欧氏距离：
X = np.array([1, 2])
Y = np.array([5, 6])
print(np.sqrt(np.power((6 - 2), 2) + np.power((5 - 1), 2)))
print(np.linalg.norm(Y - X)) # NumPy中的计算

# 打印复数的实部和虚部
a = np.array([1 + 2j, 3 + 4j, 5 + 6j])
print('real:', a.real)
print('imag:', a.imag)

# 求解给出矩阵的逆矩阵并验证：
matrix = np.array([[1., 2.], [3., 4.]])
inverse_matrix = np.linalg.inv(matrix)

# 验证原矩阵和逆矩阵想乘是否为单位矩阵E
assert np.allclose(np.dot(matrix, inverse_matrix), np.eye(2))
print(inverse_matrix)

# 使用Z-Score标准化算法对数据进行标准化处理Z = (X - mean(X)) / sd(X)
def zscore(x, axis = None):
    xmean = x.mean(axis, keepdims = True)
    xstd = np.std(x, axis = axis, keepdims = True)
    zscore = (x - xmean) / xstd
    return zscore
Z = np.random.randint(10, size = (5, 5))
print(Z)
print('Z-Score\n')
print(zscore(Z))

# 使用Min-Max标准化算法对数据进行标准化处理：Y = (Z - min(Z)) / max(Z) - min(Z)
def min_max(x, axis = None):
    min = X.min(axis = axis, keepdims = True)
    max = X.max(axis = axis, keepdims = True)
    result = (x - min) / (max - min)
    return result

Z = np.random.randint(10, size = (5, 5))
print('original Z\n')
print(Z)
print(min_max(Z))

# 使用L2范数对数据进行标准化处理L2 = sqrt(pow(x1, 2) + pow(x2, 2) + ....pow(xn,2))
def l2_normalize(v, axis = 1, order = 2):
    l2 = np.linalg.norm(v, ord = order, axis = axis, keepdims = True)
    l2[l2 == 0] = 1
    return v / 12
z = np.random.randint(10, size = (5, 5))
print(z)
print(l2_normalize(z))

# 使用NumPy计算变量直接的相关性系数：
Z = np.array([
    [1, 2, 1, 9, 10, 3, 2, 6, 7], # 特征A
    [2, 1, 8, 3, 7, 5, 10, 7, 2], # 特征B
    [2, 1, 1, 8, 9, 4, 3, 5, 7] # 特征C
])
'''
相关性系数取值从  [−1,1]  变换，靠近  1  则代表正相关性较强， −1  
则代表负相关性较强。
结果如下所示，变量 A 与变量 A 直接的相关性系数为 1，因为是同一个变量。
变量 A 与变量 C 之间的相关性系数为 0.97，说明相关性较强。
'''
print(np.corrcoef(Z))

# 使用NumPy计算矩阵的特征值和特征向量
M = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
w, v = np.linalg.eig(M)
print(w)
print(v)
# 验证
print(v * np.diag(w) * np.linalg.inv(v))

print('===========')
# 使用NumPy计算Ndarray两相邻元素差值：
z = np.random.randint(1, 10, 10)
print(Z)

print(np.diff(Z, n = 1))
print(np.diff(Z, n = 2))
print(np.diff(Z, n = 3))

print('add===============')
# NumPy将Ndarray相邻元素依次累加
Z = np.random.randint(1, 10, 10)
print(Z)
print(np.cumsum(Z))

# 使用NumPy按列连接两个数组：
m1 = np.array([1, 2, 3])
m2 = np.array([4, 5, 6])
print(np.c_[m1, m2])

# 使用NumPy按行连接两个数组：
m1 = np.array([1, 2, 3])
m2 = np.array([4, 5, 6])
print(np.r_[m1, m2])

# 使用NumPy打印9*9乘法表
print(np.fromfunction(lambda x, y: (x + 1) * (y + 1), (9, 9)))

print('image =============')
# 使用NumPy将图片转为Ndarray数组：
from io import BytesIO
from PIL import Image
import pylab
import PIL
import requests

# 通过链接下载图像
URL = 'https://i.loli.net/2020/07/16/9H6Kwo8vifTVS7O.jpg'
response = requests.get(URL)

# 将内容读取为图像
I = Image.open(BytesIO(response.content))
# 将图像转换为 Ndarray
picture = np.asarray(I)
print(picture)

# 将转换后的 Ndarray 重新绘制成图像
from matplotlib import pyplot as plt

plt.imshow(picture)
pylab.show()