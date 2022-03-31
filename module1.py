import os
import input


# 筛选
def yq_select(in_file, out_file, pro):
    data = input.init(in_file)  # 初始化数据
    file = open(out_file, 'w')
    province = data[:, 0]  # 获取第一列
    file.writelines(pro)
    row_province = data.shape[0]  # 获取数据行数
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
    return out_file
# yq_select('yq_in.txt','yq_out.txt','浙江省')
