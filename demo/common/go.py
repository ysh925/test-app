from demo.page.setting_serche import A


class start_go():
    def __init__(self,driver):
        self.driver = driver

    def re_Settings_serche(self):
        return A(self.driver)

