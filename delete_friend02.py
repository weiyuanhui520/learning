from appium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
import time

desired_caps = {
    "platformName": "Android",  # 系统
    "platformVersion": "6.0",  # 系统版本号
    "deviceName": "3782a8457d94",  # 设备名
    "appPackage": "com.tencent.mm",  # 包名
    "appActivity": "com.tencent.mm.ui.LauncherUI",  # app 启动时主 Activity
    'unicodeKeyboard': True,  # 使用自带输入法
    'noReset': True  # 保留 session 信息，可以避免重新登录
}


# driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

def is_element_exist(driver, value):
    try:
        driver.find_element(by=By.ID, value=value)
    except Exception as e:
        return False
    else:
        return True


def getsize(driver):
    x = driver.get_windows_zise()['width']
    y = driver.get_windows_zise()['height']
    return (x, y)


def getelementsaze(element):
    ele_size = element.size
    # 元素的宽
    width = ele_size['width']
    # 元素的高
    height = ele_size['height']
    return (width, height)


def getlocation(element):
    ele_coordinate = element.location
    # 元素左上角横坐标
    x = ele_coordinate['x']
    # 元素左上角纵坐标
    y = ele_coordinate['y']
    return (x, y)


def swipego(driver, x1, y1, x2, y2, time):
    width1 = getsize(driver)[0].x1
    height1 = getsize(driver)[1].y1
    width2 = getsize(driver)[0].x2
    height2 = getsize(driver)[1].y2
    driver.swipe(width1, height1, width2, height2, time)


if __name__ == '__main__':
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    driver.implicitly_wait(10)
    print(111111)
    wait = WebDriverWait(driver, 3000)
    time.sleep(30)
    friends = driver.find_elements_by_id('com.tencent.mm:id/dtf')
    print(friends)
    friends[1].click()
    time.sleep(2)
    print(222)
    while True:
        # friends=wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/dtx")))
        # print(friends)


        fristfriend = driver.find_elements_by_id('com.tencent.mm:id/ft6')
        #     fristfriend = wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/ft6")))
        print(fristfriend)
        print(fristfriend[0])
        # getelementsaze(driver, fristfriend[0])
        element = fristfriend[0]
        print(element.get_attribute('name'))
        time.sleep(1)
        print(driver)
        value = getelementsaze(element)
        # getlocation(driver, fristfriend[0])
        value2 = getlocation(element)
        print('value is %s', (value))
        print('value2 is %s', (value2))
        x1 = (float(value2[0]) + float(value[0])) / 2
        y1 = (float(value2[1]) + float(value[1])) / 2
        x2 = (float(value2[0]) + float(value[0])) / 2
        y2 = float(value2[1]) + float(value[1]) * 1.5
        y3 = y1 - y2
        driver.swipe(x1, y2, x2, y1, 500)
        # swipego(driver, x1, y2, x2, y1, time)
        print(x1)
        print(y1)
        print(x2)
        print(y2)
        print(y3)
        driver.tap([(x1, y2)])
        time.sleep(1)
