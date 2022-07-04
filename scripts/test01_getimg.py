"""
获取图片验证码
"""
# 导包
import logging
import unittest
import requests
from API.loginAPI import LoginAPI
import random
# 定义类
class TestGetimage(unittest.TestCase):
    # 前置操作
    def setUp(self):
        # 函数实例化
        self.login_api = LoginAPI()
        self.session = requests.Session()
    # 后置操作
    def tearDown(self):
        self.session.close()
    # 执行传入参数为随机小数
    def test01_get_img_code_random_float(self):
        # 定义需要传入的随机小数
        r = random.random()
        # 发起请求
        response = self.login_api.getImgCode(self.session,r)
        print(response)
        # 断言
        self.assertEqual(200,response.status_code)
    # 执行传入参数为随机整数
    def test02_get_img_code_random_int(self):
        # 定义需要传入的随机整数
        r = random.randint(10000000,90000000)
        # 发起请求
        response = self.login_api.getImgCode(self.session,r)
        print(response)
        # 断言
        self.assertEqual(200,response.status_code)
    # 传入的参数为空
    def test03_get_img_code_param_is_null(self):
        # 定义需要传入的随机整数
        r = ""
        # 发起请求
        response = self.login_api.getImgCode(self.session,r)
        print(response)
        # 断言
        self.assertEqual(404,response.status_code)

    # 传入为随机的字符串
    def test04_get_img_code_random_char(self):
        # 定义需要传入的参数
        r = random.sample("abcdefghijklmn",8)
        rand = "".join(r)
        logging.info(rand)

        response = self.login_api.getImgCode(self.session,rand)
        print(response)
        # 断言
        self.assertEqual(400,response.status_code)
