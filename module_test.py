# import yq_test.module1
#
# yq_test.module1.yq_select("yq_in.txt", "yq_out.txt", "浙江省")

# 单元测试
import sys
import module1
import module2
import unittest


if len(sys.argv) == 4:
    module1.yq_select(sys.argv[1], sys.argv[2], sys.argv[3])
if len(sys.argv) == 3:
    module2.yq_seq(sys.argv[1], sys.argv[2])

# class Module1_Test(unittest.TestCase):
#     def setup(self)->None:
#         '''
#         测试之前的准备工作
#         :return:
#         '''
#         # self.clac = module1.yq_select('yq_in.txt','yq_out.txt','浙江省')
#
#     def tearDown(self) -> None:
#         '''
#         测试之后的收尾
#         如关闭数据库
#         :return:
#         '''
#         pass
#     def test_add(self):
#         ret=self.clac.yq_select()
#         self.assertEqual()
