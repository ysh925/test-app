from time import sleep

from demo.common.init_driver1 import init_driver
from demo.common.go import start_go
from demo.common.get_yaml import get_yaml
import demo.page,pytest

def get_data():
    mylist = []
    a = get_yaml('data1').get('info')
    for i in a.keys():
        mylist.append((i,a.get(i).get('name'),a.get(i).get('tel')))
    return (mylist)

class Test_a:

    def setup_class(self):
        self.driver = init_driver()
        self.po = start_go(self.driver).re_Settings_serche()

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture()
    def start_one(self):
        self.po.click_element(demo.page.add)

    @pytest.mark.parametrize('num,name,tel',get_data())
    def test_001(self,num,name,tel):
        self.po.click_element(demo.page.add)
        self.po.input_text(demo.page.name,name)
        self.po.input_text(demo.page.tel,tel)
        print('姓名：%s，电话：%s' % (name,tel))
        self.po.click_element(demo.page.c_return_keys)
        sleep(2)
        self.driver.get_screenshot_as_file('../%s.png' % num)
        sleep(2)
        self.driver.keyevent(4)
