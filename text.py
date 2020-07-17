# -*- coding: utf-8 -*-
# @Time    : 2020/7/16 23:30
# @Author  : Qiang
# @File    : text.py
# @Software: PyCharm


import allure, pytest


class Test_allure:
    def setup(self):
        pass

    def teardown(self):
        pass

    @pytest.mark.parametrize("a",[1,2,3])
    @allure.step('我是测试步骤001')
    def test_al(self, a):
        assert a != 2

    @pytest.issue('http://www.163.com')
    @pytest.allure.testcase('http://www.baidu.com/test_001')
    @allure.allure.severity(pytest.allure.severity_leverl.TRIVIAL)
    def test_al01(self):
        allure.attach('我是一个描述')
        assert 0