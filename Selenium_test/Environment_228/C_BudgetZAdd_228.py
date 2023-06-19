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
# 输入本级文号
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/fieldset[1]/div/div[1]/div/div/div/div/div[2]/div/input').send_keys('额财科发[2023]99号')
# 输入发文标题
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/fieldset[1]/div/div[2]/form/div[1]/div/div/div/input').send_keys('2023年人才培养计划')
# 输入日期
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/fieldset[1]/div/div[2]/form/div[2]/div/div/div/input').send_keys('2023-03-29')
time.sleep(1)
# 输入摘要
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/fieldset[1]/div/div[2]/form/div[3]/div/div/div/input').send_keys('人才培养补助资金')
# 选择预算单位
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/fieldset[2]/div/form/div[1]/div/div[2]/div/div/div/div/div/div/div/input').click()
time.sleep(1)
# 双击预算单位
agency = wd.find_element(By.XPATH,'//*[@id="theme-default"]/div[4]/div/div[2]/div[1]/div[1]/div')
ActionChains(wd).double_click(agency).perform()
time.sleep(1)
# 选择资金管理处室
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/fieldset[2]/div/form/div[2]/div/div[2]/div/div/div/div/div/div/div/input').click()
time.sleep(1)
# 双击资金管理处室
bgt_mof_dep = wd.find_element(By.XPATH,'//*[@id="theme-default"]/div[5]/div/div[2]/div[1]/div[1]/div')
ActionChains(wd).double_click(bgt_mof_dep).perform()
time.sleep(1)
# 选择预算级次
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/fieldset[2]/div/form/div[3]/div/div[2]/div/div/div/div/div[1]/div/div/input').click()
time.sleep(1)
# 双击预算级次
budgetlevel = wd.find_element(By.XPATH,'//*[@id="theme-default"]/div[6]/div/div[2]/div[1]/div[1]/div')
ActionChains(wd).double_click(budgetlevel).perform()
time.sleep(1)
# 选择项目类别
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/fieldset[2]/div/form/div[4]/div/div[2]/div/div/div/div/div[1]/div/div/input').click()
time.sleep(1)
# 双击项目类别
pro_cat = wd.find_element(By.XPATH,'//*[@id="theme-default"]/div[7]/div/div[2]/div[1]/div[1]/div')
ActionChains(wd).double_click(pro_cat).perform()
time.sleep(1)
# 输入项目名称
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/fieldset[2]/div/form/div[5]/div/div[2]/div/div/div[1]/input').send_keys('人才培养项目')
time.sleep(1)
# 选择资金性质
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/fieldset[2]/div/form/div[6]/div/div[2]/div/div/div/div/div[1]/div/div/input').click()
time.sleep(1)
wd.find_element(By.XPATH,'//*[@id="theme-default"]/div[8]/div/div[2]/div[1]/div[1]/div').click()
time.sleep(1)
wd.find_element(By.XPATH,'//*[@id="theme-default"]/div[8]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div').click()
time.sleep(1)
# 双击资金性质
fundtype = wd.find_element(By.XPATH,'//*[@id="theme-default"]/div[8]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div')
ActionChains(wd).double_click(fundtype).perform()
time.sleep(1)
# 选择功能分类科目
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/fieldset[2]/div/form/div[7]/div/div[2]/div/div/div/div/div/div/div/input').click()
time.sleep(8)
wd.find_element(By.XPATH,'//*[@id="theme-default"]/div[9]/div/div[2]/div[1]/div[1]/div').click()
time.sleep(1)
wd.find_element(By.XPATH,'//*[@id="theme-default"]/div[9]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div').click()
time.sleep(1)
# 双击功能分类科目
expfunc = wd.find_element(By.XPATH,'//*[@id="theme-default"]/div[9]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div')
ActionChains(wd).double_click(expfunc).perform()
time.sleep(1)
# 选择资金来源
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/fieldset[2]/div/form/div[8]/div/div[2]/div/div/div/div/div[1]/div/div/input').click()
time.sleep(1)
wd.find_element(By.XPATH,'//*[@id="theme-default"]/div[10]/div/div[2]/div[1]/div[1]/div').click()
time.sleep(1)
# 双击资金来源
foundtype = wd.find_element(By.XPATH,'//*[@id="theme-default"]/div[10]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div')
ActionChains(wd).double_click(foundtype).perform()
time.sleep(1)
# 选择政府经济分类
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/fieldset[2]/div/form/div[9]/div/div[2]/div/div/div/div/div[1]/div/div/input').click()
time.sleep(1)
wd.find_element(By.XPATH,'//*[@id="theme-default"]/div[11]/div/div[2]/div[1]/div[1]/div').click()
time.sleep(1)
# 双击政府经济分类
govbgteco = wd.find_element(By.XPATH,'//*[@id="theme-default"]/div[11]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div')
ActionChains(wd).double_click(govbgteco).perform()
time.sleep(1)
# 选择部门经济分类
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/fieldset[2]/div/form/div[10]/div/div[2]/div/div/div/div/div[1]/div/div/input').click()
time.sleep(3)
wd.find_element(By.XPATH,'//*[@id="theme-default"]/div[12]/div/div[2]/div[1]/div[1]/div').click()
time.sleep(1)
# 双击部门经济分类
depbgteco = wd.find_element(By.XPATH,'//*[@id="theme-default"]/div[12]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div')
ActionChains(wd).double_click(depbgteco).perform()
time.sleep(1)
# 选择指标类型
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/fieldset[2]/div/form/div[12]/div/div[2]/div/div/div/div/div/div/div/input').click()
time.sleep(1)
# 点击指标类型
wd.find_element(By.XPATH,'//*[@id="theme-default"]/div[13]/div/div[2]/div[1]/div[1]/div').click()
time.sleep(1)
# 双击指标类型
bgttype = wd.find_element(By.XPATH,'//*[@id="theme-default"]/div[13]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div')
ActionChains(wd).double_click(bgttype).perform()
time.sleep(1)
# 选择指标来源
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/fieldset[2]/div/form/div[13]/div/div[2]/div/div/div/div/div/div/div/input').click()
time.sleep(1)
# 双击指标来源
sourcetype = wd.find_element(By.XPATH,'//*[@id="theme-default"]/div[14]/div/div[2]/div[1]/div[1]/div')
ActionChains(wd).double_click(sourcetype).perform()
time.sleep(1)
# 点击指标来源年度
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/fieldset[2]/div/form/div[14]/div/div[2]/div/div[2]/input').click()
time.sleep(1)
# 选择指标来源年度
wd.find_element(By.XPATH,'//*[@id="theme-default"]/div[15]/div/div[1]').click()
time.sleep(1)
# 点击支付方式
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/fieldset[2]/div/form/div[15]/div/div[2]/div/div/div/div/div[1]/div/div/input').click()
time.sleep(1)
# 双击支付方式
paytype = wd.find_element(By.XPATH,'//*[@id="theme-default"]/div[16]/div/div[2]/div[1]/div[1]/div')
ActionChains(wd).double_click(paytype).perform()
time.sleep(1)
# 点击拨款期间属性
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/fieldset[2]/div/form/div[16]/div/div[2]/div/div/div/div/div[1]/div/div/input').click()
time.sleep(1)
# 双击拨款期间属性
bkqjsx = wd.find_element(By.XPATH,'//*[@id="theme-default"]/div[17]/div/div[2]/div[1]/div[1]/div')
ActionChains(wd).double_click(bkqjsx).perform()
time.sleep(1)
# 输入金额
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/fieldset[2]/div/form/div[17]/div/div[2]/div/input').send_keys(1000000)
time.sleep(1)
# 点击保存
wd.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div[1]/div/div[2]/div[1]/div/div[1]/div/button[4]').click()
time.sleep(1)

