import os

class runTest():

    # def __init__(self):
    #     self.token=[]

    # 跑脚本的方法
    # def runbaidu(self):
    #     os.system("python3 Test_baidu.py")

    # 跑脚本并生成allure报告
    def screport(self):
        # os.system("cd E:\\baidu_test\\case\\")
        os.system("cd E:\\baidu_test\\case")
        # os.system("python3 Test_baidu.py")
        os.system("pytest Test_baidu.py -s -q --alluredir=E:\\baidu_test\\result\\ ")
        os.system("allure generate E:\\baidu_test\\result\\ -c -o E:\\baidu_test\\report\\")
        # os.system("allure serve E:\\baidu_test\\result\\")


if __name__ == '__main__':
    runTest().screport()