import pandas as pd
import sys
import os
print(sys.argv)
file = sys.argv[1]   # 因为索引0是sys的本身路径，所以开始索引为1
fi = open(file, mode="r+")
data = pd.read_table(fi, sep='\t', header=None).values  # 读取数据
filename = 'yq_out.txt'
row_province = data.shape[0]  # 获取数据行数
province = data[:, 0]  # 获取第一列
C = []  # 存放类别名称  # 提取省份,存入C数组
for i in province:
    if i not in C:
        C.append(i)
M = []  # 存放最终数据
T = ["\n"]  # 存放换行符
for j in range(len(C)):
    N = []  # 存放地区、数字
    for i in range(row_province):
        if C[j] == province[i]:
            S = data[i, 1:3:1]
            Q = ' '.join(str(i) for i in S)  # 转换数据类型==>str
            N.append(Q)  # 添加符合省份条件的地区、数字到N
    M = M + [C[j]] + N + T
with open(filename, "w", encoding='utf-8') as f:  # 写入文件
    f.write('\n'.join('%s' % id for id in M))
print("yq_out.txt的路径为："+os.path.abspath(filename))
