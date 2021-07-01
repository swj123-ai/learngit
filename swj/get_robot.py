#Author:swj
#Data:2021/05/12
import requests
import json
import dingrobot
class Test_robot():
    @staticmethod
    def test_getrobot(): #获取所有绑定机器人的robot_id
        url = "http://app.narwaltech.com/robot"
        headers = {
            'uuid': '6116e24ea513411530513ff2c744bfaeaeb0e8c3', #APP登录接口返回
            'device-id': '',
            'auth-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1dWlkIjoiNjExNmUyNGVhNTEzNDExNTMwNTEzZmYyYzc0NGJmYWVhZWIwZThjMyIsImRldmljZV9pZCI6IiIsImlhdCI6MTYyMTIyMzYzNn0.cG-6lEGSINscM1Aa13oe2eTs0YJKrwKBAM7ijxXXloU'

        }
        response = requests.get(url=url,headers=headers)
        if "result" in response.text:
            respbody = json.loads(response.text)
            access_result = respbody.get("result",{})
            access_token = []
            for index,item in enumerate(access_result):
                access_token.append(item['robot_id'])
            #print('robot_id =',access_token)
            return access_token[0] #返回获取到的其中一个robot_id
        else:
            robot = dingrobot.DingRobot()
            res = "[告警]获取robot_id失败"
            robot.send_text(res,ats=[]) #发送告警信息
            return




if __name__ == '__main__':
    Test_robot().test_getrobot()