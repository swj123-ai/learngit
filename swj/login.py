#coding = UTF-8
#Author:zhangxi
# Data:2021/1/21
import requests
import json
import dingrobot
class Test_login():
    @staticmethod
    def test_getpitatoken(): # 获取终端系统token
        host = "http://pita.narwaltech.com"
        endpoint = "/api/aiot-narwal-peng-auth/token/request"  # 接口
        url = host + endpoint
        data = {
            "mobile":"17352698215",
            "password":"17352698215",
            "platId": 0,
            "seven":0
        }
        headers = {
            "Connection": "keep-alive",
            "Host": "pita.narwaltech.com",
            "Content-Type": "application/json"
        }
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)
        result = "\"success\":true" in res.text
        if result:
            respbody=json.loads(res.text)  #还原数据
            access_token=respbody.get("data", {}).get("accessToken")
            print(access_token)
            return access_token
        else:
            robot = dingrobot.DingRobot()
            res = "[告警]管理台获取token失败"
            robot.send_text(res, ats=[])  # 发送告警信息
            return


if __name__ == '__main__':
    Test_login().test_getpitatoken()

