from demo.common.Base import Base
import demo.page


class A(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def click_serche(self):
        self.click_element(demo.page.Settings_search_box)
        self.click_element(demo.page.search_box)

        # a = get_yaml('data')
        # self.input_text(demo.page.search_box,a.get('input'))
        # self.click_element(demo.page.return_keys)