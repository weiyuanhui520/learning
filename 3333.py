from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "127.0.0.1:7555  device"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = "com.xueqiu.android.main.view.MainActivity"
# 不清空缓存启动app
caps["noReset"] = "true"
# 设置等待页面空闲状态的时间为0s
caps['settings[waitForIdleTimeout]'] = 0
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
# 显式等待10s
driver.implicitly_wait(10)

driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
driver.find_element_by_id("com.xueqiu.android:id/search_input_text").sendkeys("alibaba")
driver.quit()
