import time

from selenium import webdriver
from selenium.webdriver import Keys

from selenium.webdriver.common.by import By


option = webdriver.ChromeOptions()
#屏蔽自动化受控提示 && 开发者提示
option.add_experimental_option("excludeSwitches", ['enable-automation', 'load-extension'])
prefs = {}
prefs["credentials_enable_service"] = False
prefs["profile.password_manager_enabled"] = False
option.add_experimental_option("prefs", prefs) # 屏蔽保存密码提示框
option.add_argument('disable-notifications')    #禁用通知弹出窗口
driver = webdriver.Chrome(options=option)
driver.get('https://www.feishu.cn/')
driver.maximize_window()
driver.find_element(By.XPATH,'//*[@fill="#EFF0F1"]').click()
driver.find_element(By.LINK_TEXT,'登录').click()
time.sleep(3)
#点击账号登录
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div/div/div[1]/div').click()
driver.find_element(By.NAME,'mobile_input').send_keys("18701856125")
driver.find_element(By.CLASS_NAME,"ud__checkbox__input").click()
#点击下一步
driver.find_element(By.XPATH,'//div[@class="step-box__body"]/button').click()
time.sleep(3)
#点击密码登录
driver.find_element(By.XPATH,'//div[@class="base-tab-pane"]/button').click()
time.sleep(2)
#输入密码
driver.find_element(By.XPATH,'//input[@data-test="login-pwd-input"]').send_keys("test123456")
#点击下一步
driver.find_element(By.XPATH,'//button[@data-test="login-pwd-next-btn"]').click()
time.sleep(2)
#点击tester1账号
driver.find_element(By.XPATH,'//div[@class="meta__user-list"]/div[1]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//div[@class="headerExtra_productList"]/div').click()
time.sleep(2)
driver.find_element(By.XPATH,'//div[@class="_pp_grid_list"]/ul/li[1]').click()
window_handles = driver.window_handles
driver.switch_to.window(window_handles[-1])
time.sleep(5)
#点击通讯录
driver.find_element(By.XPATH,'//section[@data-tip="tip-contacts"]').click()
time.sleep(2)
#点击消息
driver.find_element(By.XPATH,'//section[@data-tip="tip-messenger"]').click()
time.sleep(2)
#点击搜索
driver.find_element(By.XPATH,'//div[@class="complexFeed"]/div[1]/div[1]/div/div').click()
time.sleep(2)
#输入tester2
driver.find_element(By.CLASS_NAME,'quickJump_input').send_keys("tester2")
time.sleep(1)
#点击搜索的结果
driver.find_element(By.XPATH,'//div[@class="quickJump_resultContainer"]/div[2]/div').click()
time.sleep(2)
#向tester2发送消息
driver.find_element(By.XPATH,'//div[@class="lark-editor-wrap"]/pre').send_keys("hello",Keys.ENTER)