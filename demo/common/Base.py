from selenium.webdriver.support.wait import WebDriverWait

class Base(object):

    def __init__(self,driver):

        self.driver = driver

    def find_elements(self,loc,time=5,poo=0.5):

        return WebDriverWait(self.driver, time, poo) \
            .until(lambda x: x.find_elements(*loc))


    def find_element(self,loc,time=5,poo=0.5):

        """
        :param location: 定位方法
            (By.XPATH,"元素路径")
        :return:可以操作的元素
        """
        return WebDriverWait(self.driver,time,poo)\
            .until(lambda x:x.find_element(*loc))

    def click_element(self,loc):
        """
        :param location: 定位方法
        :param location_value: 元素路径
        :return:
        """
        self.find_element(loc).click()

    def input_text(self,loc,text):
        '''
        :param location: 定位方法
        :param location_value: 元素路径
        :param text: 输入的内容
        :return:
        '''
        self.find_element(loc).send_keys(text)
