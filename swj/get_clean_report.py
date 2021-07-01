#Author:swj
#Data:2021/05/13
import requests
import json
import pprint
import dingrobot
import pytest
class Test_cleanreport():
    @staticmethod
    def test_getcleanreport(): #获取单个id清洁记录
        data_id = {
            'clean_report_id':'198309'
        }
        headers = {
            'uuid': 'c340b7414b4a43b680a09d58552a87e5',
            'device-id': '',
            'auth-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1dWlkIjoiYzM0MGI3NDE0YjRhNDNiNjgwYTA5ZDU4NTUyYTg3ZTUiLCJkZXZpY2VfaWQiOiIiLCJpYXQiOjE2MjA4MTA3NTd9.H6rDzg9PHFxEmUw3YLDtc4lWBvbmnw-bPAGaPB0vmlU'
        }
        url = "http://kun.test.client.narwaltech.com/robot/clean_report/detail"
        response = requests.get(url=url,params=data_id,headers=headers)
        print(response.text)
        if "result" in response.text:
            respbody = json.loads(response.text)
            access_result = respbody['result'] #获取返回result
            print(access_result)
            return access_result
        else:
            robot = dingrobot.DingRobot()
            res = "[告警]APP获取单个清洁记录失败"
            robot.send_text(res,ats=[]) #发送告警信息
            return


    def test_getcleanreports(self): #获取单台机器全部清洁记录
        datas_id = {
            'machine_id' : '11-01-24-d7'
        }

        headers = {
            'uuid': 'c340b7414b4a43b680a09d58552a87e5',
            'device-id': '',
            'auth-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1dWlkIjoiYzM0MGI3NDE0YjRhNDNiNjgwYTA5ZDU4NTUyYTg3ZTUiLCJkZXZpY2VfaWQiOiIiLCJpYXQiOjE2MjA4MTA3NTd9.H6rDzg9PHFxEmUw3YLDtc4lWBvbmnw-bPAGaPB0vmlU'
        }

        url = 'http://kun.test.client.narwaltech.com/robot/clean_report/all'
        response = requests.get(url=url,params=datas_id,headers=headers)
        if 'result' in response.text:
            respbody = json.loads(response.text)
            access_result = respbody['result']
            print(access_result)
            return access_result
        else:
            robot = dingrobot.DingRobot()
            res = '[告警]APP获取单台机器全部清洁记录失败'
            robot.send_text(res,ats=[]) #发送告警信息
            return

if __name__ == '__main__':
    Test_cleanreport().test_getcleanreport()
    Test_cleanreport().test_getcleanreports()