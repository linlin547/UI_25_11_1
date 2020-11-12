import allure
from selenium import webdriver


class Test001:
    def setup_class(self):
        # 声明firefox的driver
        self.driver = webdriver.Firefox()
        # 访问百度
        self.driver.get("http://www.baidu.com")

    @allure.step("登录")  # 添加步骤名称 到报告
    def test_001(self):
        print("\n test_001")
        # 添加一个截图到报告
        allure.attach(self.driver.get_screenshot_as_png(), "截图演示",
                      allure.attachment_type.PNG)

    def teardown_class(self):
        self.driver.quit()
