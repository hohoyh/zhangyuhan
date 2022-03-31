import numpy as np
import pandas as pd


# 初始化数据
def init(in_file):
    data1 = pd.read_table(in_file, sep='\t', header=None)  # 读取数据，将文件导入内存
    data = np.array(data1)
    return data


# 提取省份
def province_array(data):
    province = data[:, 0]  # 获取第一列
    C = []  # 存放类别名称  # 提取省份,存入C数组
    for i in province:
        if i not in C:
            C.append(i)
    return C

# C = province_array(data)
# print(C)
