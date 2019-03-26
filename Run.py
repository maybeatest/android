# 执行文件
import testcase.Package_Allowance
from util import BSTestRunner
import os,unittest,time
import testcase.Package_Allowance

'''
testcase_class_file:测试用例文件目录.类名.方法名
'''
if __name__ == '__main__':
    suite = unittest.TestSuite()
    # 顺序执行测试用例
    now = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime(time.time()))
    # 获取当前时间
    basedir = os.path.abspath(os.path.dirname(__file__))
    # 读取文件
    file_dir = os.path.join(basedir, 'testresult')
    # 读取文件路径
    file=os.path.join(file_dir,(now+'.html'))
    # 读取文件格式
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(testcase.Package_Allowance.Package_Allowance))
    # 读取测试用例
    re_open = open(file, 'wb')
    # 打开文件
    runner = BSTestRunner.BSTestRunner(stream=re_open, title='测试报告', description='测试结果')
    # 测试报告名称、结果
    runner.run(suite)
    # 关联测试用例，生成测试报告

