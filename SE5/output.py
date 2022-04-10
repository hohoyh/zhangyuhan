# 写文件
def write(Pi, file):
    for h in range(len(Pi)):  # 写入最终结果
        for g in range(len(Pi[h])):
            file.writelines([str(Pi[h][g][0]), '\t', str(Pi[h][g][1]), '\n'])
        file.writelines(['\n'])


# 对省排序
def seq(Pi):
    for j in range(len(Pi)):  # 对省排序
        for o in range(0, len(Pi) - 1):
            if Pi[o][0][1] < Pi[o + 1][0][1]:
                Pi[o], Pi[o + 1] = Pi[o + 1], Pi[o]
