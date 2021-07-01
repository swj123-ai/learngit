#Author:swj
#Data:2020/05/14
import requests
import json
import dingrobot
import get_robot
import login_app

RES = login_app.Test_login.test_getapptoken()
UUID = RES[1]
TOKEN = RES[0]
ROBOT_ID = get_robot.Test_robot().test_getrobot()


class Test_cleanscheme():
    @staticmethod
    def test_getcleanscheme(): #获取单个机器人清洁方案
        url = 'http://app.narwaltech.com/robot/scheme'
        data = {
            'robot_id': ROBOT_ID
        }

        headers = {
            'uuid':UUID,
            'auth-token':TOKEN
        }
        response = requests.get(url=url,params=data,headers=headers)
        if 'result' in response.text:
            respbody = json.loads(response.text)
            access_msg = respbody.get("msg",{})
            access_result = respbody.get("result",{})
            access_scheme = access_result.get("mop_scheme",{}) #获取拖地计划id
            for index,item in enumerate(access_scheme):
                access_scheme_id=item['scheme_id']
                access_humidity = item['humidity']
            res1 = "获取的单个机器人清洁方案成功"
            print(res1)

            return res1,access_scheme_id,access_humidity
        else:
            robot = dingrobot.DingRobot()
            res = "[告警]获取机器人清洁方案humidity值失败"
            robot.send_text(res, ats=[])  # 发送告警信息
            return


    def test_editcleanscheme(self): #修改机器清洁方案
        url = 'http://app.narwaltech.com/robot/scheme/'
        headers = {
            'Content-Type': 'application/json',
            'uuid':UUID,
            'auth-token':TOKEN
        }

        get_data = Test_cleanscheme().test_getcleanscheme()
        get_scheme_id = get_data[1]
        #get_humidity = get_data[2]

        data = {
            "robot_id":ROBOT_ID,
            "scheme_id": get_scheme_id,
            "humidity": [2]
        }
        response = requests.post(url=url,data=json.dumps(data),headers=headers)
        if 'result' in response.text:
            respbody = json.loads(response.text)
            access_result = respbody.get("result",{})
            res = access_result['humidity']
            if res == '[2]':
                res2 = "修改humidity值成功"
                print(res2)
            else:
                robot = dingrobot.DingRobot()
                res = "[告警]修改清洁计划humidity值失败"
                robot.send_text(res, ats=[])  # 发送告警信息
            return res2

        else:
            robot = dingrobot.DingRobot()
            res = "[告警]修改清洁计划humidity值失败"
            robot.send_text(res, ats=[])  # 发送告警信息
            return


    def test_delcleanreport(self):#删除机器人清洁方案
        robot_id = get_robot.Test_robot().test_getrobot()
        url = "http://app.narwaltech.com/robot/scheme/"
        end_url = url +'?robot_id='+ robot_id
        data = json.dumps({
            "scheme_id": "78a440a1117841ea8138f5bd3e36d132"
        })
        headers = {
            'Content-Type': 'application/json',
            'auth-token':TOKEN
        }
        response = requests.delete(url=end_url, headers=headers ,data=data)
        if 'msg' in response.text :
            respbody = json.loads(response.text)
            if respbody['msg'] == 'ok':
                print('删除机器人清洁方案成功')
                return respbody['msg']
            else:
                robot = dingrobot.DingRobot()
                res = "[告警]删除机器人清洁方案失败"
                robot.send_text(res, ats=[])  # 发送告警信息
                return

if __name__ == '__main__':
    Test_cleanscheme().test_getcleanscheme()
    Test_cleanscheme().test_editcleanscheme()
    Test_cleanscheme().test_delcleanreport()


