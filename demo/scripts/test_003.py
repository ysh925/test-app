import allure
import pytest



@allure.step('test_module_01')
@allure.severity(allure.severity_level.CRITICAL)
@allure.testcase('http://baidu.com')
@allure.issue('http://163.com')
def test_01():
    allure.attach('测试','这是一个描述')
    assert 0 == 0

@allure.testcase('http://baidu.com')
@allure.step('test_module_02')
@allure.severity(allure.severity_level.TRIVIAL)
def test_02():
    allure.attach('这是一个描述', '测试')
    assert 0 == 0

