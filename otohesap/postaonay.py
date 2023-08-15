from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
from selenium.common.exceptions import NoSuchElementException

import time
import requests
import random


a = "/home/hasario/Desktop/chromedriver"
driver = webdriver.Chrome(executable_path=a)



try:

    def boşmohal():

        driver.get("https://www.mohmal.com/tr/inbox")
        time.sleep(1)
        postas=driver.find_element_by_xpath('//*[@id="email"]/div[1]').click()
        time.sleep(1)
        emaılss=driver.find_element_by_xpath('//*[@id="email"]/div[1]').text
        time.sleep(1)
        kesposta=emaılss
        time.sleep(30)
        time.sleep(1)
        driver.get('https://www.mohmal.com/tr/inbox')
        driver.get('https://www.mohmal.com/tr/inbox')

        driver.find_element_by_class_name('unseen').click()
        time.sleep(4)




except NoSuchElementException:
    print("hata bulunmakta")