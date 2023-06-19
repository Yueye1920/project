import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# 将驱动放入python安装路径.\python\Scripts中，无需指定驱动路径
wd = webdriver.Chrome()
# 最大化窗口
wd.maximize_window()
wd.get('chrome://settings/')
wd.execute_script('chrome.settingsPrivate.setDefaultZoom(0.8);')
wd.get('http://10.17.8.228/#')
time.sleep(2)
action = ActionChains(wd)
# 点击class文字
wd.find_element(By.CLASS_NAME, 'grayTitle').click()
# element=wd.find_element(By.CLASS_NAME,'grayTitle')
# print(element.text)
wd.find_element(By.ID, 'username').send_keys('W420000010')
wd.find_element(By.ID, 'password').send_keys('Aa123456')
wd.find_element(By.ID, 'btnlogin').click()
print("登录成功")
time.sleep(2)

# wd.find_element(By.CSS_SELECTOR,'#menhu > section > div.page_l > div:nth-child(9)').click()
wd.find_element(By.XPATH, '//*[@id="menhu"]/section/div[1]/div[2]').click()
time.sleep(4)
# //*[@id="app"]/div/div[3]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/button[1]
# 获取窗口列表
list_windows = wd.window_handles
# 切换窗口
wd.switch_to.window(list_windows[1])
time.sleep(1)
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[1]/div[3]/div[2]/button[1]').click()
# //*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[1]/div[3]/div[2]/button[1]
# 直达元素位置
target = wd.find_element(By.XPATH,
                         '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/span[2]')
# js代码
js = "arguments[0].scrollIntoView()"
# 执行聚焦元素操作
wd.execute_script(js, target)
time.sleep(1)

# 点击指标录入菜单
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/span[2]').click()
time.sleep(1)
# 点击新增
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
time.sleep(1)
# 点击模板管理
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div[1]/div/div[2]/div[1]/div/div[1]/div/button[1]').click()
time.sleep(1)
# 选择模板
wd.find_element(By.XPATH,'//*[@id="theme-default"]/div[3]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[1]/div/span/span[2]').click()
# 点击调用模板
wd.find_element(By.XPATH,'//*[@id="theme-default"]/div[3]/div/div[2]/div[1]/div/div/div[1]/div[2]/button[2]').click()
# 点击金额
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/fieldset[2]/div/form/div[17]/div/div[2]/div/input').send_keys(1000000)
time.sleep(1)
# 点击保存
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div[1]/div/div[2]/div[1]/div/div[1]/div/button[4]').click()
time.sleep(3)

# 选择数据
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[1]/div/span/span[2]').click()
# 点击送审
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[3]/button').click()
time.sleep(1)

# 点击首页
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[1]/div/div/div/span').click()
# 执行聚焦元素操作
wd.execute_script(js, target)
time.sleep(1)

# 点击业务处室审核
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/span[3]').click()
time.sleep(1)
# 选择数据
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[1]/div/span/span[2]').click()
# 点击审核
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
time.sleep(1)

# 点击首页
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[1]/div/div/div/span').click()
# 执行聚焦元素操作
wd.execute_script(js, target)
time.sleep(1)

# 点击指标审核
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/span[4]').click()
time.sleep(1)
# 选择数据
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[1]/div/span/span[2]').click()
# 点击审核
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
time.sleep(1)

# 点击首页
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[1]/div/div/div/span').click()
# 执行聚焦元素操作
wd.execute_script(js, target)
time.sleep(1)

# 点击指标下达
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/span[5]').click()
time.sleep(1)
# 选择数据
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[1]/div/span/span[2]').click()
# 点击下达
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
time.sleep(3)


wd.quit()

