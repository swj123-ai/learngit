#Author:swj
#Data:2021/05/17
import requests
import json
import dingrobot
import pytest
#import pytest_assume
#from pytest_assume.plugin import assume
import clean_scheme

class Test_robot_assume_report():
    #@pytest.mark.run(order=1) #规定执行顺序
    @pytest.mark.flaky(reruns=3 )#reruns_delay=20) #失败后重试3次，每次间隔时间20秒
    def test_assume_cleanreport_get(self):
        rep1 = clean_scheme.Test_cleanscheme.test_getcleanscheme()
        pytest.assume(rep1[0] == "获取的单个机器人清洁方案成功")
        #pytest.assume(rep1[0] == 'ok')

    #@pytest.mark.run(order=2)
    def test_robot_assume_edit(self):
        rep2 = clean_scheme.Test_cleanscheme.test_editcleanscheme(self)
        pytest.assume("成功" in rep2)

    #@pytest.mark.run(order=3)
    def test_robot_assume_del(self):
        rep3 = clean_scheme.Test_cleanscheme.test_delcleanreport(self)
        pytest.assume("ok" == rep3)


if __name__ == '__main__':
    Test_robot_assume_report()




