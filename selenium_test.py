# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time

brower = webdriver.Chrome()
print(brower)
brower.get('https://www.baidu.com')
print(brower.current_url)

wait = WebDriverWait(brower, 10)
input = wait.until(lambda x: x.find_element_by_id('kw'))
input.send_keys('selenium')
butten = WebDriverWait(brower, 50).until(lambda x: x.find_element_by_id('su')).click()
time.sleep(3)
# se=WebDriverWait(brower,5000).until(lambda x:x.find_element_by_class('c-title-text')).click()
# se=brower.find_element_by_css_selector('.title_1KPOI').click()
se = brower.find_element_by_partial_link_text('安装教程 - 相关博客 - 开发者搜索').click()
print(type(se))
# se.click()
