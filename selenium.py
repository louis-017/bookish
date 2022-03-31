# #测试Chromedriver的环境是否配置好(path)
# from selenium import webdriver
# import time
# def main():
#     b=webdriver.Chrome()
#     b.get('http://www.baidu.com')
#     time.sleep(1)
#     b.quit()
# if __name__ == '__main__':
#     main()

import time
from selenium import webdriver  # 引入包
from selenium.webdriver.common.keys import Keys
#浏览器实例化并最大化窗口
def opendriver():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
class Test:
    def one(self):
        #浏览器实例化
        # driver = webdriver.Chrome()
        # driver.maximize_window()
        opendriver()
        #打开百度首页
        driver.get(r'https://www.baidu.com/')
        time.sleep(2)
        #获取当前URL，以及页面title并print
        cur_url = driver.current_url
        print(cur_url,'\n')
        cur_page_title = driver.title
        print(cur_page_title,'\n')
        #搜索selenium
        driver.find_element_by_xpath(r'//*[@id="kw"]').send_keys('selenium')
        time.sleep(2)
        driver.find_element_by_xpath(r'//*[@id="su"]').click()
        time.sleep(2)
        #判断‘百度一下’按钮是否正常显示
        if driver.find_element_by_xpath(r'//*[@id="su"]').is_displayed():
            print('--正常显示按钮--')
        #获取文本框中的文本，打印出来
        cur_txt = driver.find_element_by_xpath(r'//*[@id="kw"]').get_attribute('value')
        print(cur_txt)
        time.sleep(1)
        driver.find_element_by_xpath(r'//*[@id="kw"]').clear()
        time.sleep(2)
        text = driver.find_element_by_xpath(r'//*[@id="container"]/div[2]/div/div[2]/span').text
        print(text)
        driver.close()
    def two(self):
        opendriver()
        driver.get('https://www.baidu.com/')
        driver.find_element_by_id("kw").send_keys('seleniumm')
        time.sleep(0.5)
        driver.find_element_by_id('su').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="kw"]').send_keys(Keys.BACKSPACE)
        time.sleep(2)
        driver.find_element_by_id('su').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="kw"]').send_keys(Keys.CONTROL,'a')
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="kw"]').send_keys(Keys.CONTROL,'x')
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="kw"]').send_keys(Keys.CONTROL,'v')
        time.sleep(0.5)
        driver.find_element_by_id('su').send_keys(Keys.ENTER)
        time.sleep(0.5)
        driver.quit()




test = Test()
test.two()