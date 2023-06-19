import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 指定驱动路径
# wd=webdriver.Chrome(service=Service(r'E:\pypro\driver\chromedriver.exe'))

# 将驱动放入python安装路径.\python\Scripts中，无需指定驱动路径
wd = webdriver.Chrome()
# 最大化窗口
wd.maximize_window()
wd.get('chrome://settings/')
wd.execute_script('chrome.settingsPrivate.setDefaultZoom(0.8);')
wd.get('http://10.17.8.228/#')
time.sleep(3)
# 点击class文字
wd.find_element(By.CLASS_NAME, 'grayTitle').click()
# element=wd.find_element(By.CLASS_NAME,'grayTitle')
# print(element.text)
wd.find_element(By.ID, 'username').send_keys('W420000005')
wd.find_element(By.ID, 'password').send_keys('Aa123456')
wd.find_element(By.ID, 'btnlogin').click()
print("登录成功")
time.sleep(1)

# wd.find_element(By.CSS_SELECTOR,'#menhu > section > div.page_l > div:nth-child(9)').click()
wd.find_element(By.XPATH, '//*[@id="menhu"]/section/div[1]/div[9]').click()
time.sleep(4)
# //*[@id="app"]/div/div[3]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/button[1]
# 获取窗口列表
list_windwos = wd.window_handles
# 切换窗口
wd.switch_to.window(list_windwos[1])
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/button[1]').click()
# 直达元素位置
target = wd.find_element(By.XPATH,
                         '//*[@id="app"]/div/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/span[2]')
# js代码
js = "arguments[0].scrollIntoView()"
# 执行聚焦元素操作
wd.execute_script(js, target)
time.sleep(1)

# 点击用款计划录入（单位）菜单
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/span[2]').click()
time.sleep(4)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[4]/div').click()
time.sleep(1)
# 点击新增
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
# 填写金额
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[2]/div[1]/div/div[3]/div/div/section/aside/div[1]/div[1]/div[2]/div/input').send_keys(
    '500')
# 填写计划说明
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[2]/div[1]/div/div[3]/div/div/section/aside/div[1]/div[3]/div/div/textarea').send_keys(
    'CS')
# 点击保存
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[3]/div/div[2]/div[3]/div/button[2]').click()
time.sleep(2)
# 点击确定
wd.find_element(By.XPATH, '/html/body/div[4]/div/div[3]/button[2]').click()
time.sleep(1)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div/span').click()
# 点击送审
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
time.sleep(1)
# 点击首页
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[1]/div').click()
time.sleep(1)
# 直达元素位置
# target = wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/span[2]')
# js代码
# js = "arguments[0].scrollIntoView()"
# 执行聚焦元素操作
wd.execute_script(js, target)
time.sleep(1)

# 点击用款计划审核（单位）菜单
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/span[5]').click()
time.sleep(3)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div').click()
time.sleep(1)
# 点击审核
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
# 点击首页
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[1]/div').click()
time.sleep(1)
# 执行聚焦元素操作
wd.execute_script(js, target)
time.sleep(1)

# 点击用款计划审核（部门）菜单
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/span[7]').click()
time.sleep(3)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div').click()
time.sleep(1)
# 点击审核
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
# 点击首页
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[1]/div').click()
time.sleep(1)
# 执行聚焦元素操作
wd.execute_script(js, target)
time.sleep(1)

# 点击用款计划审核（复审）菜单
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/span[9]').click()
time.sleep(3)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[4]/div').click()
time.sleep(1)
# 点击审核
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
# 点击首页
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[1]/div').click()
time.sleep(1)
# 执行聚焦元素操作
wd.execute_script(js, target)
time.sleep(1)

# 点击用款计划批复（国库）菜单
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/span[10]').click()
time.sleep(3)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[4]/div').click()
time.sleep(1)
# 点击批复
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
print('计划批复成功')
# 点击首页
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[1]/div').click()
time.sleep(1)
# 执行聚焦元素操作
wd.execute_script(js, target)
time.sleep(3)

# 退出
wd.quit()
