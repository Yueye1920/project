# Generated by Selenium IDE

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


class Test2:
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

    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def test_2(self):
        self.driver.get("http://10.17.8.228/#")
        self.driver.set_window_size(1366, 768)
        # self.driver.find_element(By.CSS_SELECTOR, ".grayTitle").click()
        # self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "username").send_keys("W420000010")
        self.driver.find_element(By.ID, "password").send_keys("Aa123456")
        self.driver.find_element(By.ID, "btnlogin").click()
        # self.vars["window_handles"] = self.driver.window_handles
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".page_card:nth-child(2)").click()
        self.vars["win6713"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win6713"])
        time.sleep(5)
        # 点击功能菜单
        #self.driver.find_element(By.CSS_SELECTOR, ".menu-panel:nth-child(1) .row-last-card .el-button:nth-child(1)").click()
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div/div[1]/div[1]/div[3]/div[2]/button[1]').click()
        # self.driver.execute_script("arguments[0].click();",element)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".menu-panel:nth-child(1) .menuData:nth-child(1) .third-menu-item:nth-child(2)").click()
        time.sleep(1)
        element = self.driver.find_element(By.CSS_SELECTOR, ".fn-inline > .theme--primary > .vxe-button--content")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        self.driver.find_element(By.CSS_SELECTOR, ".pointer > .theme--primary").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".el-row > .el-button:nth-child(1)").click()
        time.sleep(1)
        element = self.driver.find_element(By.CSS_SELECTOR, ".el-row > .el-button:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)
        # 选择数据(selector改为xpath)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="theme-default"]/div[3]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[1]/div/span/span[2]').click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary:nth-child(2) > span").click()
        time.sleep(1)

        self.driver.find_element(By.CSS_SELECTOR,
                                 ".vxe-form--item-content > .type--text > .vxe-input--inner").send_keys("1000000")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(4) > span").click()
        time.sleep(1)
        element = self.driver.find_element(By.CSS_SELECTOR, ".el-button:nth-child(4) > span")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(2)

        # 选择数据(selector改为xpath)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[1]/div/span/span[2]').click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".fn-inline:nth-child(3) .vxe-button--content").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".fn-inline:nth-child(3) .vxe-button--content")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        self.driver.find_element(By.CSS_SELECTOR, ".fn-inline:nth-child(1) > .tab-li .fn-inline > .fn-inline").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".menu-panel:nth-child(1) .menuData:nth-child(1) .third-menu-item:nth-child(3)").click()
        time.sleep(2)
        element = self.driver.find_element(By.CSS_SELECTOR,".vxe-cell > .vxe-cell--checkbox > .vxe-checkbox--unchecked-icon")
        #self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[1]/div/span/span[2]').click()
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".pointer > .theme--primary").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".pointer > .theme--primary")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)
        # 点击首页
        element = self.driver.find_element(By.CSS_SELECTOR, ".fn-inline:nth-child(1) > .tab-li")
        #self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div[1]/div/div[1]/ul/li[1]/div')
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)

        element = self.driver.find_element(By.CSS_SELECTOR,
                                 ".menu-panel:nth-child(1) .menuData:nth-child(1) .third-menu-item:nth-child(4)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)
        # 选择数据(selector改为xpath)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[3]/main/div/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[1]/div/span/span[2]').click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".pointer > .theme--primary").click()
        time.sleep(1)
        element = self.driver.find_element(By.CSS_SELECTOR, ".pointer > .theme--primary")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)

        self.driver.find_element(By.CSS_SELECTOR, ".fn-inline:nth-child(1) > .tab-li").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".menu-panel:nth-child(1) .third-menu-item:nth-child(5)").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".vxe-cell > .vxe-cell--checkbox > .vxe-checkbox--unchecked-icon").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".fn-inline > .theme--primary > .vxe-button--content").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".fn-inline > .theme--primary > .vxe-button--content")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()


