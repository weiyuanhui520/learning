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

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)


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


def swipego(driver, x1, y1, x2, y2, time):
    width1 = getsize(driver)[0].x1
    height1 = getsize(driver)[1].y1
    width2 = getsize(driver)[0].x2
    height2 = getsize(driver)[1].y2
    driver.swipe(width1, height1, width2, height2, time)


# 获取通讯录列表
def get_address_list():
    driver.find_elements_by_id('com.tencent.mm:id/dtf')[1].click()
    # 获取昵称（备注）
    address_list = driver.find_elements_by_id('com.tencent.mm:id/ft6')
    remarks = []
    for address in address_list:
        remark = address.get_attribute("text")
        # 排除自己和微信官方号
        if remark != "自己的微信名" and remark not in remarks:
            remarks.append(remark)
    swipego(driver, 0.5, 0.8, 0.5, 0.2, time)
    return remarks


# 判断是否被删
def is_delete(driver, remark, count):
    if count == "1":
        time.sleep(2)
        print('点击微信搜索框')
        driver.find_element_by_id('com.tencent.mm:id/cn1').click()
    time.sleep(2)
    print('在搜索框输入搜索信息')
    driver.find_element_by_id('com.tencent.mm:id/bhn').send_keys(remark)
    time.sleep(2)
    print('点击搜索到的好友')
    driver.find_element_by_id('com.tencent.mm:id/tm').click()
    time.sleep(2)
    # 转账
    driver.find_element_by_id('com.tencent.mm:id/aks').click()
    time.sleep(2)
    driver.find_elements_by_id('com.tencent.mm:id/pa')[5].click()
    time.sleep(2)
    driver.find_element_by_id('com.tencent.mm:id/cx_').click()
    time.sleep(2)
    driver.find_element_by_id('com.tencent.mm:id/cxi').click()
    time.sleep(5)
    # 判断是否被删
    is_exist = is_element_exist(driver, 'com.tencent.mm:id/jh')
    if is_exist is True:
        return remark
    else:
        return False


# 删除把自己删除的人
def del_person(nicks):
    for inx, val in enumerate(nicks):
        time.sleep(2)
        if inx == 0:
            print('在搜索框输入搜索信息')
            driver.find_element_by_id('com.tencent.mm:id/bhn').send_keys(val)
        else:
            time.sleep(2)
            print('点击微信搜索框')
            driver.find_element_by_id('com.tencent.mm:id/cn1').click()
            print('在搜索框输入搜索信息')
            time.sleep(1)
            driver.find_element_by_id('com.tencent.mm:id/bhn').send_keys(val)
        time.sleep(2)
        print('点击搜索到的人')
        driver.find_element_by_id('com.tencent.mm:id/tm').click()
        time.sleep(2)
        print('点击聊天对话框右上角...')
        driver.find_element_by_id('com.tencent.mm:id/cj').click()
        time.sleep(2)
        print('点击头像')
        driver.find_element_by_id('com.tencent.mm:id/f3y').click()
        time.sleep(2)
        print('点击联系人右上角...')
        driver.find_element_by_id('com.tencent.mm:id/cj').click()
        time.sleep(2)
        print('点击删除按钮')
        driver.find_element_by_id('com.tencent.mm:id/g6f').click()
        time.sleep(2)
        print('点击弹出框中的删除')
        driver.find_element_by_id('com.tencent.mm:id/doz').click()
