"""
获取验证码
定义类
"""
# 导包
import app
import requests
import random
class  LoginAPI():
    # 初始化参数
    def __init__(self):
        # 获取图片验证码URL
        self.getimgcode_url = app.BASE_URL + "/common/public/verifycode1/"
        # 获取手机验证码URL
        self.getSmacode_url = app.BASE_URL + "/member/public/sendSms"
    # 获取验证码
    def getImgCode(self,session,r):
        url = self.getimgcode_url + str(r)
        response = session.get(url)
        return response
    # 获取短信验证码
    def getphoneCode(self,session,phone,imgVerifCode):
        # 定义请求参数
        data = {
            "phone":phone,
            "imgVerifCode":imgVerifCode,
            "type":"reg"
        }
        # 发送请求
        response = session.post(self.getSmacode_url,json=data)
        return response
