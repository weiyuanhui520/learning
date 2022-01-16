# coding=utf-8
from appium import webdriver
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
import time

nr = r'你不是收款方好友，对方添加你为好友后才能发起转账'
nr2 = r'对方微信号已被限制登录，为保障你的资金安全，暂时无法完成交易。'
desired_caps = {
    "platformName": "Android",  # 系统
    "platformVersion": "6.0",  # 系统版本号
    "deviceName": "3782a8457d94",  # 设备名
    "appPackage": "com.tencent.mm",  # 包名
    "appActivity": "com.tencent.mm.ui.LauncherUI",  # app 启动时主 Activity
    "unicodeKeyboard": True,  # 使用自带输入法
    "noReset": True,  # 保留 session 信息，可以避免重新登录
    "fullReset": False,  # 重启appium不会清空登录数据
    # "skipDeviceInitialization" : True,
    "automationName": "UiAutomator1"  # 不会重复安装setting
}
ll = ['微信号:  a75559058', '微信号:  chenyu349134578', '微信号:  zhu1314277', '微信号:  wxid_u14iculfxf6j22',
      '微信号:  wxid_p3gnzuku06o722', '微信号:  hao1981319', '微信号:  lus1819', '微信号:  lwh396925999',
      '微信号:  wxid_7tc05e8obi0021', '微信号:  wxid_vobbwehmbu9321', '微信号:  xP_0128', '微信号:  am879701633',
      '微信号:  w594721591', '微信号:  xlmlyc1027', '微信号:  lms20141128', '微信号:  CQY1002559385', '微信号:  xinyi071030',
      '微信号:  XIN5_1', '微信号:  wiX_rgstnoih6axb21', '微信号:  wjdxj843941744', '微信号:  JungHuang1996', '微信号:  baozhilin6789',
      '微信号:  sp401957112', '微信号:  HTH861', '微信号:  w635333971', '微信号:  huimouyixiao5520', '微信号:  xiamiya-',
      '微信号:  zh1634865852', '微信号:  wxid_0wdnyog2a52i22', '微信号:  wxid_rrk8k3u51nkq22', '微信号:  qhj17876656745',
      '微信号:  chunyanz1127', '微信号:  abc291887441', '微信号:  wxid_8dyvg2szs4qj22', '微信号:  YB50JY8', '微信号:  hzy6-6',
      '微信号:  wxid_ns9gyk1k2qyd22', '微信号:  Nuo77c', '微信号:  Caijianming201758', '微信号:  ainiyisi_001',
      '微信号:  wxid_vyu64ig05xxe21', '微信号:  zs15224626211', '微信号:  mjcy1314com', '微信号:  hygfs12345678',
      '微信号:  A15220332697', '微信号:  wxid_4s8c25flcao422', '微信号:  yesweitinglin', '微信号:  wxid_om1k1yii3utn22',
      '微信号:  W996442281', '微信号:  DJ15766562755', '微信号:  W134999999', '微信号:  hyj2392651463', '微信号:  A18377355183',
      '微信号:  chun791777195', '微信号:  AA1550940501', '微信号:  wxid_tdyj2pr5rp3u22', '微信号:  HMc13424228080',
      '微信号:  zhj703007739', '微信号:  wxid_y3htn44zery022', '微信号:  a15676565238', '微信号:  wxid_vbi0q8i1kgjk22',
      '微信号:  HMD10085', '微信号:  wxid_ceujtqqtfah222', '微信号:  wxid_9bp5vlxp89j422', '微信号:  lzhui52168', '微信号:  rvc668',
      '微信号:  yaocai12', '微信号:  wxid_myc8s8zzfyq222', '微信号:  wxg13420080209', '微信号:  wxid_1egdr8snu0cz22',
      '微信号:  q296496345', '微信号:  qq18078276807', '微信号:  luo1141404975', '微信号:  T96866558', '微信号:  xf19980507',
      '微信号:  wei623757432', '微信号:  wxid_kdrmn1fbqrxe22', '微信号:  lxx19978313889', '微信号:  wxid_8wrwfmwnya7z22',
      '微信号:  a13480996516', '微信号:  liminx93p11', '微信号:  zhi168866', '微信号:  qwe15878290791', '微信号:  vs644311324',
      '微信号:  zhuzhuxia20190717', '微信号:  ly464031711', '微信号:  wxid_5l4s3sksd4gt22', '微信号:  wxid_3e4op8jmxivf22',
      '微信号:  aa13667722906', '微信号:  H15977250087', '微信号:  jiaqi_00323', '微信号:  wxid_at4kfrv5zz9022',
      '微信号:  zhouyong_466350531', '微信号:  Yul-789', '微信号:  wxid_wh8te7g1s8ju22', '微信号:  A9sv888',
      '微信号:  wxid_ewkyrbo6xs4x22', '微信号:  wxid_mwhlxp9sxuxr22', '微信号:  wxid_yo66nnhzlm7s22', '微信号:  fei18878297940',
      '微信号:  mm18778204248', '微信号:  tyhbjijiubnook', '微信号:  w18378207968', '微信号:  Syoo88168', '微信号:  QF1273688177',
      '微信号:  x131188900', '微信号:  yjhd201117', '微信号:  wxid_nbzyjnuttazg22', '微信号:  BTC20200607', '微信号:  ruii925017',
      '微信号:  wxid_l6iuqa8i56a022', '微信号:  lianying116688', '微信号:  Tommy2016', '微信号:  pan1102296432',
      '微信号:  Oyj18278224101', '微信号:  wangxiaoli911230', '微信号:  Amn98oo', '微信号:  wdj768', '微信号:  aaa13667800788']
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
wait = WebDriverWait(driver, 3000)
for yy in range(len(ll)):
    ss = ll[yy]
    num = re.findall('[0-9a-zA-Z_]+', ss)
    print(num)
    wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/he6"))).click()
    time.sleep(1.5)
    print('sendkeys')
    wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/bxz"))).click()
    print('click')
    wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/bxz"))).send_keys(num)
    print('sendover')
    # driver.find_element_by_id("com.tencent.mm:id/bxz").send_keys(num)
    wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/bn6"))).click()
    wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/au0"))).click()
    time.sleep(1)
    driver.find_elements_by_id('com.tencent.mm:id/rs')[5].click()
    # hb=driver.find_element_by_id('com.tencent.mm:id/rs')[5].get_attribute('name')
    # print(hb)
    time.sleep(1.5)
    driver.find_element_by_id('com.tencent.mm:id/jf4').send_keys('0.01')
    time.sleep(0.5)
    wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/e6c"))).click()  # 点击转账
    name1 = wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/ffh"))).get_attribute('name')
    time.sleep(0.5)
    if name1 == nr or name1 == nr2:
        wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/ffp"))).click()  # 点击知道了
        wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/ei"))).click()  # 点击返回按钮
        wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/d8"))).click()  # 点击右上角 ...
        time.sleep(0.5)
        wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/h8t"))).click()  # 点击头像
        wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/d8"))).click()  # 点击右上角 ...
        wait.until(EC.element_to_be_clickable((By.ID, "com.tencent.mm:id/ijq"))).click()  # 点击删除
        time.sleep(1)
        driver.find_elements_by_id('com.tencent.mm:id/ffp')[1].click()  # 点击确定删除
        time.sleep(1)
    elif name1 == nr:
        pass

print(len(ll))
