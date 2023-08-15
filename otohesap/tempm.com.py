#https://tempm.com/
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException

import time
import requests
import random

a = "/home/hasario/Desktop/chromedriver"
driver = webdriver.Chrome(executable_path=a)
time.sleep(9)
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
try:

    def program():

        sifren = "1denemehasario"
        for i in range(1, 999):

        #driver.find_element_by_xpath('/html/body/div[3]/div/div/p/a[1]').click()

            driver.get("https://www.instagram.com/accounts/emailsignup/")
            time.sleep(2)



            eposta = driver.find_element_by_name("emailOrPhone")
            eposta.send_keys(Keys.CONTROL, "v")

            time.sleep(2)
            adsoyad = driver.find_element_by_name("fullName")

            adsoyad.send_keys("hasario")
            kadı = driver.find_element_by_name("username")
            taktaktak = random.randint(1, 10000)
            masa = ("hasario" + str(taktaktak))
            kadı.send_keys(masa)
            ################

            sıfre = driver.find_element_by_name("password")
            sıfre.send_keys(sifren)
            time.sleep(3)

            time.sleep(2)
            buton = driver.find_element_by_xpath("//button[@type='submit']")
            buton.click()
            time.sleep(5)
            ###ay
            driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[1]/select').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[2]')
            ####gün
            driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[4]').click()
            time.sleep(1)
            ##yıl
            driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[20]').click()
            ileris=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[5]/div[2]/button').click()
            #### onay
            time.sleep(15)
            conf=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[3]/form/div[1]/input')
            conf.send_keys(Keys.CONTROL, "v")




            #######32
            driver.get("https://www.instagram.com/" + masa)
            time.sleep(3)
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="inbox-table"]/tbody/tr/td[1]').click()
            time.sleep(3)
            kod=driver.find_element_by_xpath('//*[@id="email_content"]/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]').text
            print(kod)

            cıkış = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div/button/span')
            cıkış.click()
            time.sleep(2)
            gogo = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/button[6]")
            time.sleep(5)
            gogo.click()

            time.sleep(1)
            print("#" * 10)
            print("kulanıcı adı :=:=:" + masa)
            # print(masa)
            print("#" * 20)
            print("adsoyad:=:=:""hasario")
            print("#" * 20)
            print("sifre:=:=:" + sifren)
            print("#" * 20)
            print("epostanız==" + kesposta)
            # print(posta)
            print("#" * 20)
            ################
            print("başarıyla hesabınız oluşturulmuştur ")
            kulanıcı = ("KULANICIADI==" + masa)

            r = requests.get("https://www.instagram.com/" + masa)
            xx = r.status_code
            a = print(xx)
            dosya = open("hesaplar.txt", "a")

            dosya.write(kulanıcı + "\n")

            dosya.write("adsoyad===hasario\n")

            dosya.write("sifre==="+str(sifren)+"\n")

            dosya.write("eposta==" + kesposta + "\n")

            dosya.write("\t\n")

            dosya.close()
            ##########################################################
            sıkayet = open("sıkayet.txt", "a")
            sıkayet.write(kesposta + " 1denemehasario\n")
            sıkayet.close()






except NoSuchElementException:
    while True:
        program()
        while True:
            try:
                program()
            except Exception as e:
                print("Bir hata oluştu:", e)
                continue
                while True:
                    program()






