import datetime
import os.path
import sys
import time
import allure

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


# sys.dont_write_bytecode = True


# 指定驱动路径
# driver=webdriver.Chrome(service=Service(r'E:\pypro\driver\chromedriver.exe'))

# 将驱动放入python安装路径.\python\Scripts中，无需指定驱动路径

@allure.epic('熟悉pytest+selenium+allure自动化测试框架'.center(30, '*'))
@allure.feature('用款计划测试模块')
@allure.suite('测试套件')
class TestPlan():

    def setup_method(self):
        # 定义chrome
        chrome_options = Options()
        # 设置无界面格式
        chrome_options.headless = True
        # 创建无界面对象
        self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver = webdriver.Chrome()
        # self.vars = {}

    # def teardown_method(self):
    #     self.driver.quit()

    @allure.story('用户故事描述：用款计划测试')
    @allure.title('测试标题：用款计划全流程测试')
    @allure.description('测试用例描述：用款计划全流程测试，包含正向流程逆向流程')
    @allure.testcase('测试用例地址：http://10.17.8.111/#')
    @allure.tag('测试用例标签：用例一')
    def test_planwhole(self):
        try:
            # 最大化窗口
            self.driver.maximize_window()
            # self.driver.get('chrome://settings/')
            # self.driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.8);')
            self.driver.get('http://10.17.8.111/#')
            time.sleep(2)
            # 点击class文字
            # self.driver.find_element(By.CLASS_NAME, 'loginTitle active').click()
            # element=self.driver.find_element(By.CLASS_NAME,'grayTitle')
            # print(element.text)
            print('\n')
            self.driver.find_element(By.ID, 'username').send_keys('W420000010')
            print("**用户账户：W420000010")
            self.driver.find_element(By.ID, 'password').send_keys('Aa111111')
            print("**用户密码：Aa111111")
            time.sleep(2)

            # self.driver.find_element(By.ID, 'btnlogin').click()
            # 点击元素被覆盖，使用Keys.ENTER
            self.driver.find_element(By.ID, 'btnlogin').send_keys(Keys.ENTER)

            print("**用户登录成功")
            time.sleep(2)

            # 关闭公告弹窗
            self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/button/i').click()
            # element = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/button/i')
            # actions = ActionChains(self.driver)
            # actions.move_to_element(element).perform()
            time.sleep(3)

            # driver.find_element(By.CSS_SELECTOR,'#menhu > section > div.page_l > div:nth-child(9)').click()
            self.driver.find_element(By.XPATH, '/html/body/div[1]/section/section/div/div[2]').click()
            time.sleep(2)

            # //*[@id="app"]/div/div[3]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/button[1]
            # 获取窗口列表
            list_windows = self.driver.window_handles
            # 切换窗口
            self.driver.switch_to.window(list_windows[1])
            time.sleep(2)
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/button[1]').click()

            # 直达元素位置
            target = self.driver.find_element(By.XPATH,
                                              '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/span[1]')
            # js代码
            js = "arguments[0].scrollIntoView()"
            # 执行聚焦元素操作
            self.driver.execute_script(js, target)
            time.sleep(1)

            # 点击用款计划录入（单位）菜单
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/span[1]').click()

            time.sleep(3)
            # 选择数据
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[4]/div').click()

            time.sleep(1)
            # 点击新增
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
            # 填写金额
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[2]/div[1]/div/div[3]/div/div/section/aside/div[1]/div[1]/div[2]/div/input').send_keys(
                '10')
            # 填写计划说明
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[2]/div[1]/div/div[3]/div/div/section/aside/div[1]/div[3]/div/div/textarea').send_keys(
                '测试新增')
            # 点击保存
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[3]/div/div[2]/div[3]/div/button[2]').click()
            time.sleep(5)
            print('**用款计划录入（单位）保存成功')
            # 点击确定
            self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/button[2]').click()
            time.sleep(3)
            # 点击额度列表
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[1]/button').click()
            time.sleep(2)
            # 选择数据
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[4]/div').click()
            time.sleep(1)
            # 点击新增
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
            # 填写金额
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[2]/div[1]/div/div[3]/div/div/section/aside/div[1]/div[1]/div[2]/div/input').send_keys(
                '5')
            # 填写计划说明
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[2]/div[1]/div/div[3]/div/div/section/aside/div[1]/div[3]/div/div/textarea').send_keys(
                '测试作废')
            # 点击保存
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[3]/div/div[2]/div[3]/div/button[2]').click()
            time.sleep(1)
            print('**用款计划录入（单位）保存成功')
            # 点击确定
            self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/button[2]').click()
            time.sleep(1)

            # 选择数据
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div/span').click()
            # 点击作废
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[2]/button').click()
            # 点击确定
            self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div[3]/button[2]').click()
            time.sleep(1)
            print('**用款计划录入（单位）作废成功')
            # 选择数据
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div/span').click()
            # 点击送审

            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
            print('**用款计划录入（单位）送审成功')
            time.sleep(3)
            # 点击已办事项
            # self.driver.find_element(By.XPATH,
            #                          '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[3]/div/div[1]/span[2]').click()
            # self.driver.find_element(By.XPATH,
            #                          '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[3]/div/div[1]/span[2]').send_keys(Keys.ENTER)
            element = self.driver.find_element(By.XPATH,
                                               '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[3]/div/div[1]/span[2]')
            ActionChains(self.driver).move_to_element(element).perform()

            # 点击已送审
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[3]/div/div[2]/div/div[1]/div[1]/ul/li[1]').click()
            time.sleep(1)
            # 选择数据
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div/span').click()
            # 点击撤销
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li/button').click()
            print('**用款计划录入（单位）撤销成功')
            time.sleep(1)
            # 点击待办事项
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[2]/div/div[1]/span[2]').click()
            # 点击未送审
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[2]/div/div[2]/div/div[1]/div[1]/ul/li[1]').click()
            time.sleep(1)
            # 选择数据
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div/span').click()
            # 点击送审
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
            print('**用款计划录入（单位）送审成功')
            # 关闭用款计划录入（单位）菜单
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[2]/div/div/em').click()

            # # 点击首页
            # self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[1]/div').click()

            time.sleep(1)
            # 直达元素位置
            # target = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/span[2]')
            # js代码
            # js = "arguments[0].scrollIntoView()"
            # 执行聚焦元素操作
            self.driver.execute_script(js, target)
            time.sleep(1)

            # 点击用款计划审核（单位）菜单
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/span[4]').click()
            time.sleep(2)
            # 选择数据
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div').click()
            time.sleep(1)
            # 点击退回
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[2]/button').click()

            time.sleep(1)

            # 文本框输入
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[7]/div/div[2]/div/textarea').send_keys(
                '退回操作')
            # 点击确定
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[7]/div/div[3]/span/button[2]').click()
            time.sleep(1)
            print('**用款计划审核（单位）退回成功')

            # 关闭用款计划审核（单位）菜单
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[2]/div/div/em').click()

            # 点击用款计划录入（单位）菜单
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/span[1]').click()
            time.sleep(1)

            self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div/div[3]/div[1]').click()

            # 点击待办事项
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[2]/div/div[1]/span[2]').click()
            # 点击被退回
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[2]/div/div[2]/div/div[1]/div[1]/ul/li[2]').click()
            time.sleep(1)
            # 选择数据
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div/span').click()
            # 点击送审
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
            print('**用款计划录入（单位）送审成功')
            time.sleep(2)

            # 关闭用款计划录入（单位）菜单
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[2]/div/div/em').click()

            # 点击用款计划审核（单位）菜单
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/span[4]').click()
            time.sleep(1)

            # # 点击刷新
            # self.driver.find_element(By.XPATH,
            #                          '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[1]/div/div[2]/div[5]/button[1]').click()
            # time.sleep(2)

            # 选择数据
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div').click()
            time.sleep(1)
            # 点击审核
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
            time.sleep(2)
            print('**用款计划审核（单位）审核成功')
            # 点击已办事项
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[2]/div/div[1]/span[2]').click()
            # 点击已审核
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[2]/div/div[2]/div/div[1]/div[1]/ul/li[1]').click()
            time.sleep(1)
            # 选择数据
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div').click()
            time.sleep(1)
            # 点击撤销审核
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li/button').click()
            print('**用款计划审核（单位）撤销审核成功')
            time.sleep(2)
            # 点击待办事项
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[1]/div/div[1]/span[2]').click()
            # 点击待审核
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[1]/div/div[2]/div/div[1]/div[1]/ul/li[1]').click()
            time.sleep(1)
            # 选择数据
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div').click()
            time.sleep(1)
            # 点击审核
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
            print('**用款计划审核（单位）审核成功')
            time.sleep(2)

            # # 点击首页
            # self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[1]/div').click()
            # time.sleep(1)

            # 关闭用款计划审核（单位）菜单
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[2]/div/div/em').click()

            # # 执行聚焦元素操作
            # self.driver.execute_script(js, target)
            # time.sleep(1)

            # 点击用款计划审核（部门）菜单
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/span[6]').click()
            time.sleep(2)
            # 选择数据
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div').click()
            time.sleep(1)
            # 点击退回
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[2]/button').click()
            time.sleep(1)

            # 文本框输入
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[7]/div/div[2]/div/textarea').send_keys(
                '退回操作')
            # 点击确定
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[7]/div/div[3]/span/button[2]').click()
            print('**用款计划审核（部门）退回成功')
            time.sleep(1)

            # 关闭用款计划审核（部门）菜单
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[2]/div/div/em').click()

            # 点击用款计划审核（单位）菜单
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/span[4]').click()
            time.sleep(1)
            # 点击待办事项
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[1]/div/div[1]/span[2]').click()
            # 点击被退回
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[1]/div/div[2]/div/div[1]/div[1]/ul/li[2]').click()
            time.sleep(1)

            # 选择数据
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div/span').click()
            # 点击送审
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
            print('**用款计划审核（单位）审核成功')
            time.sleep(2)

            # 关闭用款计划审核（审核）菜单
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[2]/div/div/em').click()

            # 点击用款计划审核（部门）菜单
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/span[6]').click()
            time.sleep(1)

            # # 点击刷新
            # self.driver.find_element(By.XPATH,
            #                          '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[1]/div/div[2]/div[5]/button[1]').click()
            # time.sleep(2)

            # 选择数据
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div').click()
            time.sleep(1)
            # 点击审核
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
            print('**用款计划审核（部门）审核成功')
            time.sleep(2)

            # 点击已办事项
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[2]/div/div[1]/span[2]').click()
            # 点击已审核
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[2]/div/div[2]/div/div[1]/div[1]/ul/li[1]').click()
            time.sleep(1)
            # 选择数据
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div').click()
            time.sleep(1)
            # 点击撤销审核
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li/button').click()
            print('**用款计划审核（部门）撤销审核成功')
            time.sleep(2)
            # 点击待办事项
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[1]/div/div[1]/span[2]').click()
            # 点击待审核
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[1]/div/div[2]/div/div[1]/div[1]/ul/li[1]').click()
            time.sleep(1)
            # 选择数据
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div').click()
            time.sleep(1)
            # 点击审核
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
            print('**用款计划审核（部门）审核成功')
            time.sleep(2)

            # 关闭用款计划审核（部门）菜单
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[2]/div/div/em').click()

            # # 点击首页
            # self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[1]/div').click()
            # time.sleep(1)

            # 执行聚焦元素操作
            self.driver.execute_script(js, target)
            time.sleep(1)

            # 点击用款计划审核（复审）菜单
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/span[7]').click()
            time.sleep(2)
            # 选择数据
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[4]/div').click()
            time.sleep(1)

            # 点击退回
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[2]/button').click()
            time.sleep(1)

            # 文本框输入
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[7]/div/div[2]/div/textarea').send_keys(
                '退回操作')
            # 点击确定
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[7]/div/div[3]/span/button[2]').click()
            print('**用款计划审核（复审）退回成功')
            time.sleep(1)

            # 关闭用款计划审核（复审）菜单
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[2]/div/div/em').click()

            # 点击用款计划审核（部门）
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/span[6]').click()
            time.sleep(1)
            # 点击待办事项
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[1]/div/div[1]/span[2]').click()
            # 点击被退回
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[1]/div/div[2]/div/div[1]/div[1]/ul/li[2]').click()
            time.sleep(1)
            # 选择数据
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[5]/div/span').click()
            # 点击审核
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
            print('**用款计划审核（部门）审核成功')
            time.sleep(2)

            # 关闭用款计划审核（部门）菜单
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[2]/div/div/em').click()

            # 点击用款计划审核（复审）
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/span[7]').click()
            time.sleep(1)
            # # 点击刷新
            # self.driver.find_element(By.XPATH,
            #                          '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[1]/div/div[2]/div[5]/button[1]').click()
            # time.sleep(2)

            # 选择数据
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[4]/div').click()
            time.sleep(1)
            # 点击审核
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
            print('**用款计划审核（复审）审核成功')
            time.sleep(2)

            # 点击已办事项
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[2]/div/div[1]/span[2]').click()
            # 点击已审核
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[2]/div/div[2]/div/div[1]/div[1]/ul/li[1]').click()
            time.sleep(1)
            # 选择数据
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[4]/div').click()
            time.sleep(1)
            # 点击撤销审核
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li/button').click()
            print('**用款计划审核（复审）撤销审核成功')
            time.sleep(2)
            # 点击待办事项
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[1]/div/div[1]/span[2]').click()
            # 点击待审核
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[1]/div/div[2]/div/div[1]/div[1]/ul/li[1]').click()
            time.sleep(1)
            # 选择数据
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[4]/div').click()
            time.sleep(1)
            # 点击审核
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
            print('**用款计划审核（复审）审核成功')

            # 关闭用款计划审核（复审）菜单
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[2]/div/div/em').click()

            # # 点击首页
            # self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[1]/div').click()
            # time.sleep(1)
            # 执行聚焦元素操作

            self.driver.execute_script(js, target)
            time.sleep(1)

            # 点击用款计划批复（国库）菜单
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/span[8]').click()
            time.sleep(2)
            # 选择数据
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[4]/div').click()
            time.sleep(1)
            # 点击退回
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[2]/button').click()
            # 文本框输入
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[7]/div/div[2]/div/textarea').send_keys(
                '退回操作')
            # 点击确定
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[7]/div/div[3]/span/button[2]').click()
            print('**用款计划批复（国库）退回成功')
            time.sleep(1)

            # 关闭用款计划批复（国库）菜单
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[2]/div/div/em').click()

            # 点击用款计划审核（复审）菜单
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/span[7]').click()
            time.sleep(1)
            # 点击待办事项
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[1]/div/div[1]/span[2]').click()
            # 点击被退回
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[1]/div/div[2]/div/div[1]/div[1]/ul/li[2]').click()
            time.sleep(1)
            # 选择数据
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[4]/div').click()
            # 点击审核
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
            print('**用款计划审核（复审）审核成功')
            time.sleep(2)

            # 关闭用款计划审核（复审）菜单
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[2]/div/div/em').click()

            # 点击用款计划批复（国库）菜单
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/span[8]').click()
            time.sleep(1)
            # # 点击刷新
            # self.driver.find_element(By.XPATH,
            #                          '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[1]/div/div[2]/div[5]/button[1]').click()
            # time.sleep(2)
            # 选择数据
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[4]/div').click()
            time.sleep(1)
            # 点击批复
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
            print('**用款计划批复（国库）批复成功')
            time.sleep(2)
            # 点击已批复页签
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[2]/button').click()
            time.sleep(1)
            # 选择数据
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[4]/div').click()
            time.sleep(1)
            # 点击撤销
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li/button').click()
            print('**用款计划批复（国库）撤销批复成功')
            time.sleep(2)
            # 点击待批复页签
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[1]/div/div/ul/li[1]/button').click()
            time.sleep(1)
            # 选择数据
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[4]/div').click()
            time.sleep(1)
            # 点击批复
            self.driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[1]/div/ul/li[2]/div/ul/li[1]/button').click()
            time.sleep(1)
            allure.dynamic.description('计划批复成功')
            print('**计划批复成功')

        except :
            name = time.strftime("%Y%m%d%H%M%S")
            self.driver.get_screenshot_as_file('E:/pypro/Selenium_test/ErrorPng/%s.png' % name)
            print('程序异常终止，截图成功')
            except_type, except_value, except_traceback = sys.exc_info()
            except_file = os.path.split(except_traceback.tb_frame.f_code.co_filename)[1]
            exc_dict = {
                "报错类型": except_type,
                "报错信息": except_value,
                "报错文件": except_file,
                "报错行数": except_traceback.tb_lineno,
            }
            print(exc_dict)
            raise



    @allure.story('用户故事描述：用例二')
    @allure.title('测试标题：国库集中支付')
    @allure.description('测试用例描述：用例二')
    @allure.testcase('测试用例地址：http://10.17.8.111/#')
    @allure.tag('测试用例标签：用例二')
    def test_payvoucher(self):
        print('ִ执行第二个用例')
        assert True == True


    @allure.story('用户故事描述：用例三')
    @allure.title('测试标题：单位资金支付')
    @allure.description('测试用例描述：用例三')
    @allure.testcase('测试用例地址：http://10.17.8.111/#')
    @allure.tag('测试用例标签：用例二')
    def test_inc(self):
        print('ִ执行第三个用例')
        assert True == True


# if __name__ == "__main__":
#     pytest.main(['-x'])

# if __name__ == "__main__":
#     pytest.main(['-s', '-v', 'T_AllurePlanWholeflowWT_111.py
#     ir=./allure-results

# 执行测试用例
# python test_Demo.py
# 生成报告
# allure generate allure-results -o allure-reports/
# 打开报告
# allure open allure-reports/
