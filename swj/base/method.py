import requests
from utils.operationExcel import OperationExcel
from utils.operationjson import Operationjson
from utils.excel_dara import *

class Method:
    def __init__(self):
        self.opjson=Operationjson()
        self.excel=OperationExcel()
    def post(self,row):
        try:
            r = requests.post(
                url=self.excel.get_URL(row=row),
                data=self.opjson.getRequestsData(row=row),
                headers = getHeadersValue()

            )
            return r
        except Exception as e:
            raise RuntimeError("异常")
