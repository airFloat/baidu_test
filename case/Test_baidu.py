import requests
import unittest




class baidu_test(unittest.TestCase):

    def test_setup_class(self):
        r = requests.get("https://www.baidu.com/")
        # assert r.status_code == 200
        if r.status_code == 200:
            print("用例通过")
        else:
            print("用例未通过")

    def test_setup(self):
        print("第二个用例")

    def test_wudi(self):
        r = requests.get("https://www.baidu.com/")
        if r.status_code == 400:
            print("状态码是400")
        else:
            print("状态码不是400")


# if __name__ == '__main__':
#     baidu_test().setup_class()
#     baidu_test().setup()
#     baidu_test().wudi()
