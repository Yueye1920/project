import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pyautogui import click
from pyautogui import typewrite

# 指定驱动路径
# wd=webdriver.Chrome(service=Service(r'E:\pypro\driver\chromedriver.exe'))

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
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/button[1]').click()

# 直达元素位置
target = wd.find_element(By.XPATH,
                         '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/span[2]')
# js代码
js = "arguments[0].scrollIntoView()"
# 执行聚焦元素操作
wd.execute_script(js, target)
time.sleep(1)

# sys.exit()

# 点击支付申请录入（单位）菜单
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/span[2]').click()
time.sleep(2)

# 选择数据 !!!
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[2]/div[2]/table/tbody/tr/td[4]/div').click()
# 点击新增
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
time.sleep(2)
# 输入收款人信息
wd.find_element(By.XPATH, '//*[@id="payee_acct_name"]/div[1]/input').send_keys('影九')
wd.find_element(By.XPATH, '//*[@id="payee_acct_no"]/div[1]/input').send_keys('6228987833692258')
wd.find_element(By.XPATH, '//*[@id="payee_acct_bank_name"]/div[1]/input').send_keys('烽火银行')

# 点击结算方式
wd.find_element(By.ID, 'set_mode').click()
time.sleep(1)
# 双击选择结算方式                      /html/body/div[4]/div[1]/div[1]/ul/li/div[1]/div[1]/div
set_modes = wd.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li/div[1]/div[1]/div/span[2]')
ActionChains(wd).double_click(set_modes).perform()
# sys.exit()
# 点击单位内部机构
wd.find_element(By.ID, 'internal_dep').click()
time.sleep(1)
# 双击单位内部机构
internal_deps = wd.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li/div[1]/div[1]/div/span[2]')
ActionChains(wd).double_click(internal_deps).perform()
# 填写资金用途

# 直达元素位置
targets = wd.find_element(By.XPATH,
                          '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[2]/div[1]/div[1]/div[4]/div/div/div/div[2]/div[2]/div')
# js代码
jss = "arguments[0].scrollIntoView()"
# 执行聚焦元素操作
wd.execute_script(jss, targets)
time.sleep(1)

wd.find_element(By.XPATH, '//*[@id="use"]/div[1]/div/div[1]/input').send_keys('测试国库集中支付')
# 点击资金往来对象
wd.find_element(By.ID, 'fund_traobj_type').click()
time.sleep(1)
# 点击顶级
wd.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[1]/ul/li/div[1]/div[1]/div[1]').click()
time.sleep(1)
# 双击底级
fund_traobj_typeS = wd.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[1]/ul/li/div[1]/div[1]/div[2]/div[1]/div')
ActionChains(wd).double_click(fund_traobj_typeS).perform()
# 填写金额
wd.find_element(By.XPATH, '//*[@id="pay_app_amt"]/div[1]/input').send_keys('3')
# 点击保存
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[3]/div/div[2]/div[2]/button[2]').click()
time.sleep(2)
# 点击确定
wd.find_element(By.XPATH, '/html/body/div[7]/div/div[3]/button[2]').click()
time.sleep(6)
# 点击确定，进行跳转
wd.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/button[2]').click()
time.sleep(1)

# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[7]/div/span').click()
time.sleep(1)
# 点击送审
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[3]/button').click()
time.sleep(2)

# 点击首页
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[1]/div/div/div/span').click()
# 执行聚焦元素操作
wd.execute_script(js, target)
time.sleep(1)

# 点击支付申请审核（单位）菜单
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/span[3]').click()
time.sleep(2)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[5]/div').click()
time.sleep(1)
# 点击审核
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()

# 点击首页 !!!
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[1]/div/div/div/span').click()
# 执行聚焦元素操作
wd.execute_script(js, target)
time.sleep(1)

# 点击支付凭证生成（单位）菜单
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/span[4]').click()
time.sleep(2)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div').click()
time.sleep(1)
# 点击生成
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li/button').click()
time.sleep(1)

# 点击首页
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[1]/div/div/div/span').click()
# 执行聚焦元素操作
wd.execute_script(js, target)
time.sleep(1)

# 点击支付凭证签名
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/span[6]').click()
time.sleep(2)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[5]/div').click()
time.sleep(1)
# 点击签名
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[2]/button').click()
time.sleep(3)

# 获取坐标
# x,y = position()
# print(x,y)

# 输入密码
click(623, 384)
typewrite('111111')
click(601, 422, button='left')
time.sleep(1)

# 点击首页
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[1]/div/div/div/span').click()
# 执行聚焦元素操作
wd.execute_script(js, target)
time.sleep(1)

# 点击支付凭证签章
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/span[8]').click()
time.sleep(2)
# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[4]/div').click()
time.sleep(1)
# 点击签章
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[2]/button').click()
time.sleep(3)

# 选择印章
click(483, 252, button='left')
time.sleep(1)
click(620, 506, button='left')
time.sleep(1)
# 输入密码
click(593, 387)
typewrite('111111')
time.sleep(2)
click(601, 422, button='left')
time.sleep(1)

# 点击首页
wd.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[1]/div/div/div/span').click()
# 执行聚焦元素操作
wd.execute_script(js, target)
time.sleep(1)

# 点击支付凭证发送
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div/span[9]').click()
time.sleep(2)

# 选择数据
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[2]/div[2]/table/tbody/tr/td[5]/div').click()
time.sleep(1)
# 点击发送
wd.find_element(By.XPATH,
                '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
time.sleep(2)




wd.quit()
