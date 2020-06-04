import pytest,demo.page
from demo.common.init_driver import init_driver
from demo.common.go import start_go
from demo.common.get_yaml import get_yaml
from time import sleep

def yaml_data():
    my_list = []
    data = get_yaml('data').get('Search_Data')
    for i in data.keys():
        my_list.append((i, data.get(i).get("test"),data.get(i).get("expect_data")))
    return my_list


class Test_a:

    def setup_class(self):
        self.driver = init_driver()
        self.po = start_go(self.driver).re_Settings_serche()

    def teardown_class(self):
        self.driver.quit()


    @pytest.mark.parametrize('test_num,text,expect_data',yaml_data())
    def test_001(self,test_num,text,expect_data):
        self.po.click_serche()
        print('测试编号:',test_num)
        self.po.input_text(demo.page.search_box,text)
        self.driver.get_screenshot_as_file('../%s.png' % test_num)
        sleep(1)
        assert expect_data == 456


