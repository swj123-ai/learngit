#coding = UTF-8
#Author:zhangxi
# Data:2021/1/27
import requests
import json
import dingrobot
class Test_login():
    @staticmethod
    def test_getapptoken(): # 获取app系统token
        host = "http://app.narwaltech.com"
        endpoint = "/user/login/pw"  # 接口
        url = host + endpoint
        data = {
            "mobile":"17352698215",
            "password":"17352698215",
            "area_code": "86"
        }
        headers = {
            "Connection": "keep-alive",
            "Content-Type": "application/json"
        }
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        #print(res.text)
        if "token" in res.text:
            global access_token
            respbody = json.loads(res.text)
            access_token = respbody.get("result",{}).get("token")#获取token
            access_uuid = respbody.get("result",{}).get("uuid") #获取uuid
            print(access_token)
            return access_token,access_uuid
        else:
            robot = dingrobot.DingRobot()
            res = "APP获取token失败告警"
            robot.send_text(res, ats=[])  # 发送告警信息
            return
if __name__ == '__main__':
      Test_login().test_getapptoken()
