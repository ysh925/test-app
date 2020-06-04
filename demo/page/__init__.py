from selenium.webdriver.common.by import By


"""
    设置-搜索框
"""
Settings_search_box = (By.ID,"com.android.settings:id/search")
search_box = (By.ID,"android:id/search_src_text")
return_keys = (By.XPATH,"//android.widget.ImageButton[@content-desc='收起']")


"""
    电话本添加
"""

add = (By.ID,'com.android.contacts:id/floating_action_button')
name = (By.XPATH,"//*[contains(@text,'姓名')]")
tel = (By.XPATH,"//*[contains(@text,'电话')]")
c_return_keys = (By.XPATH,"//android.widget.ImageButton[@content-desc='向上导航']")
