from login_test import Test_testlogin
#from utils.operationexcel import operactionexcle
import json
import ast
import utils.operationexcel
import xlrd

book = xlrd.open_workbook("/home/swj/auto-master/Data/data.xlsx")

headers = {'Content-Type': 'application/json'}
login_test = Test_testlogin(headers)
res = utils.operationexcel.operactionexcle()
res_excel = res[0] #获取用例数据
print(res_excel)

for case in res_excel:
    response = Test_testlogin.user_login(url=case['url'],data=ast.literal_eval(case['data']))
    result_back = {'code':response['code'],'msg':response['msg']} #返回结果信息
    print(result_back)


