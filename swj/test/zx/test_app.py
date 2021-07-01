#coding = UTF-8
#Author:zhangxi
# Data:2021/3/3
import requests
import json
import dingrobot
import login_test_app
import pytest
import time
from pytest import assume
class Test_app():
    # 公共变量
    host = "http://kun.test.client.narwaltech.com"
    uuid,access_token=login_test_app.Test_login().test_getappauthentication()  #获取鉴权需要数据
    if access_token != "":
        print("获取到access_token,值为", access_token)
        time.sleep(2)
    if uuid != "":
        print("uuid,值为", uuid)
        time.sleep(2)
    headers = {
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Auth-Token":access_token,
        "UUID":uuid
    }
    # 断言及告警
    # Author:zhangxi
    # Data:2021/3/5
    @staticmethod
    def result_assession(resp, error_text):
        respbody = json.loads(resp.text)  # 还原数据为json格式
        nickname = respbody.get("result", {}).get("nickname")
        pytest.assume(nickname=="13417458760")  # 断言结果回写报告
        # result = "\"nickname\":\"1341745876" in resp.text  # 判断修改数据是否和预期符合
        # print(resp.text)
        # print(result)
        if(nickname!="13417458760"):
        # if (not result):
            robot = dingrobot.DingRobot()
            robot.send_text(error_text, ats=[])  # 发送告警信息
        return

    # Author:zhangxi
    # Data:2021/3/4
    def test_app_userinformation_modify(self):  # 修改用户信息
        endpoint = "/user/info"  # 接口
        url = self.host + endpoint
        print("url=", url)
        data = {"nickname": 13417458760, "sex": 1}
        print("headers=", self.headers)
        res = requests.post(url=url, data=json.dumps(data), headers=self.headers)
        print("res=", res)
        Test_app.result_assession(res, "App修改用户信息失败告警")
        time.sleep(5)
        return


if __name__ == '__main__':
    test_app = Test_app()
    test_app.test_app_userinformation_modify()
    time.sleep(5)
