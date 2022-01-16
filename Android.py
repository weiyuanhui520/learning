# coding=utf-8
from appium import webdriver
import pytest


class Test_demo1():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '3782a8457d94'
        # com.android.settings/com.android.settings.Settings
        desired_caps['appPackage'] = 'com.tencent.mm'
        desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
        desired_caps['noreset'] = 'true'
        desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        # self.driver.back()
        self.driver.quit()
        print("退出")

    def test_cli22(self):
        self.driver.find_element_by_xpath('//*[@id="com.tencent.mm:id/fzg" and @test="象州运江水晶微帮互动群"]').click()
        # self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")

        # el5 = self.driver.find_element_by_id("android:id/button2")
        # el5.click()
        # el6 = self.driver.find_element_by_accessibility_id("向上导航")
        # el6.click()

        print("启动【设置】应用")

        # if __name__=='__main__':
        #     pytest.main()
        #       pytest.main(['testcases/test_seting_avatar.py', '--alluredir', './report'])
