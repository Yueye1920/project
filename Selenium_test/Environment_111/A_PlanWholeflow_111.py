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
wd.get('http://10.17.8.111/#')
time.sleep(2)
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
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/button[1]').click()
# 直达元素位置
target = wd.find_element(By.XPATH,
                         '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/span[1]')
# js代码
js = "arguments[0].scrollIntoView()"
# 执行聚焦元素操作
wd.execute_script(js, target)
time.sleep(1)

# 点击用款计划录入（单位）菜单
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/span[1]').click()
time.sleep(3)
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
    '10')
# 填写计划说明
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[2]/div[1]/div/div[3]/div/div/section/aside/div[1]/div[3]/div/div/textarea').send_keys(
    '测试新增')
# 点击保存
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[3]/div/div[2]/div[3]/div/button[2]').click()
time.sleep(3)
# 点击确定
wd.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/button[2]').click()
time.sleep(1)
# 点击额度列表
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[1]/button').click()
time.sleep(2)
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
    '5')
# 填写计划说明
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[2]/div[1]/div/div[3]/div/div/section/aside/div[1]/div[3]/div/div/textarea').send_keys(
    '测试作废')
# 点击保存
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[3]/div/div[2]/div[3]/div/button[2]').click()
time.sleep(3)
# 点击确定
wd.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/button[2]').click()
time.sleep(1)

# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div/span').click()
# 点击作废
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[2]/button').click()
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
# 点击已办事项
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[3]/div/div[1]/span[2]').click()
# 点击已送审
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[3]/div/div[2]/div/div[1]/div[1]/ul/li[1]').click()
time.sleep(1)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div/span').click()
# 点击撤销
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li/button').click()
time.sleep(1)
# 点击待办事项
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[2]/div/div[1]/span[2]').click()
# 点击未送审
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[2]/div/div[2]/div/div[1]/div[1]/ul/li[1]').click()
time.sleep(1)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div/span').click()
# 点击送审
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()

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
                '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/span[4]').click()
time.sleep(2)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div').click()
time.sleep(1)
# 点击退回
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[2]/button').click()
time.sleep(1)

# 菜单栏点击用款计划录入（单位）
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[2]/div/div/div/span').click()
time.sleep(1)

wd.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div/div[3]/div[1]').click()

# 点击待办事项
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[2]/div/div[1]/span[2]').click()
# 点击被退回
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[2]/div/div[2]/div/div[1]/div[1]/ul/li[2]').click()
time.sleep(1)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div/span').click()
# 点击送审
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
time.sleep(2)

# 菜单栏点击用款计划审核（单位）
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[3]/div/div/div/span').click()
time.sleep(1)
# 点击刷新
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[1]/div/div[2]/div[5]/button[1]').click()
time.sleep(2)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div').click()
time.sleep(1)
# 点击审核
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
time.sleep(2)
# 点击已办事项
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[2]/div/div[1]/span[2]').click()
# 点击已审核
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[2]/div/div[2]/div/div[1]/div[1]/ul/li[1]').click()
time.sleep(1)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div').click()
time.sleep(1)
# 点击撤销审核
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li/button').click()
time.sleep(2)
# 点击待办事项
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[1]/div/div[1]/span[2]').click()
# 点击待审核
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[1]/div/div[2]/div/div[1]/div[1]/ul/li[1]').click()
time.sleep(1)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div').click()
time.sleep(1)
# 点击审核
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
time.sleep(2)

# 点击首页
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[1]/div').click()
time.sleep(1)
# 执行聚焦元素操作
wd.execute_script(js, target)
time.sleep(1)

# 点击用款计划审核（部门）菜单
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/span[6]').click()
time.sleep(2)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div').click()
time.sleep(1)
# 点击退回
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[2]/button').click()
time.sleep(1)

# 菜单栏点击用款计划审核（单位）
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[3]/div/div/div/span').click()
time.sleep(1)
# 点击待办事项
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[1]/div/div[1]/span[2]').click()
# 点击被退回
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[1]/div/div[2]/div/div[1]/div[1]/ul/li[2]').click()
time.sleep(1)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div/span').click()
# 点击送审
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
time.sleep(2)

# 菜单栏点击用款计划审核（部门）
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[4]/div/div/div/span').click()
time.sleep(1)
# 点击刷新
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[1]/div/div[2]/div[5]/button[1]').click()
time.sleep(2)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div').click()
time.sleep(1)
# 点击审核
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
time.sleep(2)
# 点击已办事项
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[2]/div/div[1]/span[2]').click()
# 点击已审核
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[2]/div/div[2]/div/div[1]/div[1]/ul/li[1]').click()
time.sleep(1)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div').click()
time.sleep(1)
# 点击撤销审核
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li/button').click()
time.sleep(2)
# 点击待办事项
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[1]/div/div[1]/span[2]').click()
# 点击待审核
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[1]/div/div[2]/div/div[1]/div[1]/ul/li[1]').click()
time.sleep(1)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div').click()
time.sleep(1)
# 点击审核
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
time.sleep(2)

# 点击首页
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[1]/div').click()
time.sleep(1)
# 执行聚焦元素操作
wd.execute_script(js, target)
time.sleep(1)

# 点击用款计划审核（复审）菜单
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/span[7]').click()
time.sleep(2)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[4]/div').click()
time.sleep(1)

# 点击退回
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[2]/button').click()
time.sleep(1)

# 菜单栏点击用款计划审核（部门）
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[4]/div/div/div/span').click()
time.sleep(1)
# 点击待办事项
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[1]/div/div[1]/span[2]').click()
# 点击被退回
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[1]/div/div[2]/div/div[1]/div[1]/ul/li[2]').click()
time.sleep(1)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div/span').click()
# 点击送审
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
time.sleep(2)

# 菜单栏点击用款计划审核（复审）
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[5]/div/div/div/span').click()
time.sleep(1)
# 点击刷新
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[1]/div/div[2]/div[5]/button[1]').click()
time.sleep(2)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[4]/div').click()
time.sleep(1)
# 点击审核
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
time.sleep(2)
# 点击已办事项
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[2]/div/div[1]/span[2]').click()
# 点击已审核
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[2]/div/div[2]/div/div[1]/div[1]/ul/li[1]').click()
time.sleep(1)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[4]/div').click()
time.sleep(1)
# 点击撤销审核
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li/button').click()
time.sleep(2)
# 点击待办事项
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[1]/div/div[1]/span[2]').click()
# 点击待审核
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[1]/div/div[2]/div/div[1]/div[1]/ul/li[1]').click()
time.sleep(1)
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
                '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/span[8]').click()
time.sleep(2)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[4]/div').click()
time.sleep(1)
# 点击退回
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[2]/button').click()
# 文本框输入
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div/div[7]/div/div[2]/div/textarea').send_keys('退回操作')
# 点击确定
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div/div[7]/div/div[3]/span/button[2]').click()
time.sleep(1)

# 菜单栏点击用款计划审核（复审）
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[5]/div/div/div/span').click()
time.sleep(1)
# 点击待办事项
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[1]/div/div[1]/span[2]').click()
# 点击被退回
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[1]/div/div[2]/div/div[1]/div[1]/ul/li[2]').click()
time.sleep(1)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[4]/div').click()
# 点击送审
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
time.sleep(2)

# 菜单栏点击用款计划批复（国库）
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[6]/div/div/div/span').click()
time.sleep(1)
# 点击刷新
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[1]/div/div[2]/div[5]/button[1]').click()
time.sleep(2)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[4]/div').click()
time.sleep(1)
# 点击批复
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
time.sleep(2)
# 点击已批复页签
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[2]/button').click()
time.sleep(1)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[4]/div').click()
time.sleep(1)
# 点击撤销
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li/button').click()
time.sleep(2)
# 点击待批复页签
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[1]/button').click()
time.sleep(1)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[4]/div').click()
time.sleep(1)
# 点击批复
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
time.sleep(1)
print('计划批复成功')


# 退出
wd.quit()
