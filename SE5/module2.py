import os
import input
import output


# 排序
def yq_seq(in_file, out_file):
    data = input.init(in_file)  # 初始化数据
    file = open(out_file, 'w')
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
    output.seq(Pi)
    output.write(Pi, file)
    file.close()
    print(out_file + "文件的路径为：" + os.path.abspath(out_file))
    return out_file


# yq_seq('yq_in.txt', 'yq_out.txt')
