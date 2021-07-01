#coding = UTF-8
#Author:zhangxi
# Data:2021/3/2
import requests
import json
import dingrobot
import time
class Test_login():
    @staticmethod
    def test_getappauthentication(): # 获取app系统token
        host = "http://kun.test.client.narwaltech.com"  #测试环境app地址
        endpoint = "/user/login/pw"  # 接口
        url = host + endpoint
        data = {
            "mobile": "13417458760",
            "password": "Swanyang-316",
            "area_code": "86"
        }
        headers = {
            "Connection": "keep-alive",
            "Content-Type": "application/json"
        }
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        if "token" in res.text:
            respbody = json.loads(res.text)
            access_token = respbody.get("result",{}).get("token")  #获取token
            print(access_token)
        else:
            robot = dingrobot.DingRobot()
            res = "APP获取token信息失败告警"
            robot.send_text(res, ats=[])  # 发送告警信息
            return
        if "uuid" in res.text:
            uuid = respbody.get("result",{}).get("uuid")  #获取token
            print(uuid)
        else:
            robot = dingrobot.DingRobot()
            res = "APP获取uuid信息失败告警"
            robot.send_text(res, ats=[])  # 发送告警信息
            return
        return uuid,access_token
if __name__ == '__main__':
      Test_login().test_getappauthentication()
      time.sleep(5)