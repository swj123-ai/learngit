import json
import urllib.request
DINGURL = "https://oapi.dingtalk.com/robot/send?access_token"
TOKEN = "9e5fa1015527bdc3056f02dba792f7c4f6b48a1639d821f8ce950e4346f1cd9a"  #钉钉告警群获取token
DEFAUTMSG = "告警"  #告警关键字
class DingRobot(object):

    def __init__(self, token=TOKEN):
        self.token = token

    def send_text(self, msg=DEFAUTMSG, ats=[]):
        text_msg = {}
        text_msg["msgtype"] = "text"
        text_content = {}
        text_content["content"] = msg
        text_msg["text"] = text_content
        at_info = {"atMobiles": [], "isAtAll": False}
        for item in ats:
            if item == "all":
                at_info["isAtAll"] = True
            elif isinstance(item, int):
                at_info["atMobiles"].append(item)
            else:
                pass
        text_msg["at"] = at_info

        # print(text_msg)
        req = urllib.request.Request("{}={}".format(DINGURL, self.token))
        req.add_header("Content-Type", "application/json")
        res = urllib.request.urlopen(req, json.dumps(text_msg).encode('utf-8'))
        print(res.read())


if __name__ == '__main__':
    robot = DingRobot()
    res = ""
    robot.send_text(res, ats=[])
