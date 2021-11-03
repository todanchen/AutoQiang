import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By

from config import DriverPath


class JinDonBuy:
    def __init__(self, st: str = None, shop_url: str = None):
        self.start_time = time.mktime(time.strptime(st, '%Y-%m-%d %H:%M:%S'))
        self.shop_url = shop_url

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-gpu')
        self.chrome_browser = webdriver.Chrome(executable_path=DriverPath, options=chrome_options)

    def login(self):
        login_url = 'https://passport.jd.com/new/login.aspx'
        self.chrome_browser.get(login_url)
        while True:
            log_web = True
            try:
                self.chrome_browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/a')
            except Exception as e:
                print(e)
                log_web = False

            if not log_web:
                break

    def wait_to_start(self):
        while True:
            diff_time = self.start_time - time.time()
            if diff_time < 0.1:
                break

    def auto_buy(self):
        # 先手动登录到自动化平台
        self.login()

        # 第一次登录到商品页面
        self.chrome_browser.maximize_window()
        self.chrome_browser.get(self.shop_url)

        # 等待时间开始刷新页面
        self.wait_to_start()

        # 刷新页面
        self.chrome_browser.get(self.shop_url)

        break_flag = False
        while True:
            try:
                self.chrome_browser.find_element(By.XPATH, '//*[@id="fittings"]/div[2]/div[3]/div[3]/a').click()
                break_flag = True
            except Exception as e:
                print(datetime.datetime.now(), ":///", e)

            # 查找到购买按钮,并点击, 退出
            if break_flag:
                break

        # 切换窗口到购物车
        self.chrome_browser.switch_to.window(self.chrome_browser.window_handles[-1])

        # 点击结算按钮
        break_flag = False
        while True:
            try:
                self.chrome_browser.find_element(By.XPATH,
                                                 '//*[@id="cart-body"]/div[1]/div[5]/div/div[2]/div/div/div/div[2]/div[2]/div/div[1]/a').click()
                break_flag = True
            except Exception as e:
                print(datetime.datetime.now(), ":///", e)

            if break_flag:
                break

        # 检查提交按钮已经出现
        # break_flag = False
        # while True:
        #     try:
        #         self.chrome_browser.find_element(By.XPATH, '//*[@id="order-submit"]')
        #         break_flag = True
        #     except Exception as e:
        #         print(datetime.datetime.now(), ":///", e)
        #
        #     if break_flag:
        #         break

        # 激活密码输入
        # js = 'document.querySelector("#quark-pw-list > i:nth-child(1)").className="quark-pw-input active"'
        # self.chrome_browser.execute_script(js)
        #
        # js = 'document.querySelector("#cardwrap").style="left: -1px; visibility: visible;"'
        # self.chrome_browser.execute_script(js)
        #
        # # 模拟键盘输入密码
        # time.sleep(0.1)
        # pw = list('111111')
        # for p in pw:
        #     pyautogui.press(p)

        # 提交按钮点击
        break_flag = False
        while True:
            try:
                self.chrome_browser.find_element(By.XPATH, '//*[@id="order-submit"]').click()
                break_flag = True
            except Exception as e:
                print(datetime.datetime.now(), ":///", e)

            if break_flag:
                break


class LenovoBuy:
    def __init__(self, st: str = None, shop_url: str = None):
        self.start_time = time.mktime(time.strptime(st, '%Y-%m-%d %H:%M:%S'))
        self.shop_url = shop_url

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-gpu')
        self.chrome_browser = webdriver.Chrome(executable_path=DriverPath, options=chrome_options)

    def login(self):
        login_url = 'https://reg.lenovo.com.cn/auth/v1/login'
        self.chrome_browser.get(login_url)
        while True:
            log_web = True
            try:
                self.chrome_browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/a')
            except Exception as e:
                print(e)
                log_web = False

            if not log_web:
                break

    def wait_to_start(self):
        while True:
            diff_time = self.start_time - time.time()
            if diff_time < 0.1:
                break

    def auto_buy(self):
        # 先手动登录到自动化平台
        self.login()

        # 第一次登录到商品页面
        self.chrome_browser.maximize_window()
        self.chrome_browser.get(self.shop_url)

        # 等待时间开始刷新页面
        self.wait_to_start()

        # 刷新页面
        self.chrome_browser.get(self.shop_url)

        break_flag = False
        while True:
            try:
                self.chrome_browser.find_element(By.XPATH, '//*[@id="ljgm"]').click()
                break_flag = True
            except Exception as e:
                print(datetime.datetime.now(), ":///", e)

            # 查找到购买按钮,并点击， 退出刷新
            if break_flag:
                break

        # 点击结算按钮
        break_flag = False
        while True:
            try:
                self.chrome_browser.find_element(By.CLASS_NAME, 'fr submitBtn').click()
                break_flag = True
            except Exception as e:
                print(datetime.datetime.now(), ":///", e)

            if break_flag:
                break


if __name__ == '__main__':
    url = 'https://item.lenovo.com.cn/product/1017869.html'
    start_time = '2021-11-02 23:00:00'
    jdb = LenovoBuy(start_time, url)
    jdb.auto_buy()
