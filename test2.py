import numpy as np
import pandas as pd
import os
import sys

in_file = sys.argv[1]  # 因为索引0是sys的本身路径，所以开始索引为1
out_file = sys.argv[2]  # 创建输出文件索引
pro = sys.argv[3]  # 创建省份名称索引
data1 = pd.read_table(in_file, sep='\t', header=None)  # 读取数据，将文件导入内存
data = np.array(data1)
file = open(out_file, 'w')
row_province = data.shape[0]  # 获取数据行数
province = data[:, 0]  # 获取第一列
C = []  # 存放类别名称  # 提取省份,存入C数组
for i in province:
    if i not in C:
        C.append(i)
if pro != ".":
    file.writelines(pro)
    M = []  # 存放最终数据
    T = ["\t"]  # 存放换行符
    for i in range(row_province):
        N = []
        if pro == province[i]:
            S = data[i, 1:3:1]
            Q = ' '.join(str(i) for i in S)  # 转换数据类型==>str
            N.append(Q)  # 添加符合省份条件的地区、数字到N
        M = T + N
        file.writelines('\n'.join('%s' % id for id in M))
    print(pro + "的信息" + out_file + "文件的路径为：" + os.path.abspath(out_file))
else:
    sum: int = 0
    P = []
    Pi = []
    for i in range(len(data)):
        if data[i][0] != data[(i + 1) % len(data)][0] and i != 0 or i == len(data) - 1:  # 判断省份是否变换
            P.append([data[i - 1][0], sum])
            for n in range(len(P)):  # 列表中省份的数据排序
                for k in range(0, len(P) - 1):
                    if P[k][1] < P[k + 1][1]:
                        P[k], P[k + 1] = P[k + 1], P[k]
            sum: int = 0
            Pi.append(P)  # 将每个排序好的省份放入新列表
            P = []
        else:
            P.append([data[i][1], data[i][2]])  # 存入市、数据
            sum += data[i][2]
            if data[i][0] != data[(i + 1) % len(data)][0] and i != 0 or i == len(data) - 1:
                P.append([data[i - 1][0], sum])
                for n in range(len(P)):  # 列表中省份的数据排序
                    for k in range(0, len(P) - 1):
                        if P[k][1] < P[k + 1][1]:
                            P[k], P[k + 1] = P[k + 1], P[k]
                sum: int = 0
                Pi.append(P)  # 将每个排序好的省份放入新列表
                P = []
    for j in range(len(Pi)):  # 对省排序
        for o in range(0, len(Pi) - 1):
            if Pi[o][0][1] < Pi[o + 1][0][1]:
                Pi[o], Pi[o + 1] = Pi[o + 1], Pi[o]
    for h in range(len(Pi)):  # 写入最终结果
        for g in range(len(Pi[h])):
            file.writelines([str(Pi[h][g][0]), '\t', str(Pi[h][g][1]), '\n'])
        file.writelines(['\n'])
    file.close()
    print(out_file + "文件的路径为：" + os.path.abspath(out_file))