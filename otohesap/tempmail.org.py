from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os

import time
import requests
import random


a = "/home/hasario/Desktop/chromedriver"
driver = webdriver.Chrome(executable_path=a)
def program():
    sifren = "1denemehasario"
    for i in range(1, 999):








        time.sleep(2)

        driver.get("https://temp-mail.org/tr/")
        time.sleep(8)
        kesposta=driver.find_element_by_xpath('//*[@id="mail"]').get_attribute("value")
        copy_xpath=driver.find_element_by_xpath('//*[@id="click-to-copy"]').click()
        delete_xpath=driver.find_element_by_xpath('//*[@id="click-to-delete"]').click()
        time.sleep(2)





        driver.get("https://www.instagram.com/")
        time.sleep(2)

        eposta = driver.find_element_by_name("emailOrPhone")
        eposta.send_keys(kesposta)

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







        driver.get("https://www.instagram.com/" + masa)
        time.sleep(3)
        driver.get("https://temp-mail.org/tr/")
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[4]/ul/li[4]/div[1]/a/span[1]').click()#inboxsender vs onay
        #onay icin
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        driver.find_element_by_xpath('/html/body/main/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div[3]/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/a').click()










        cıkış = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div/button/span')
        cıkış.click()
        time.sleep(2)
        gogo = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/button[6]')
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
        # Buraya kadar çalışıyor UHUSDFKSLŞFSLK sonunda lan jsklfsddfsdjklfsdklfdsxfgljköşmrtçhyçö.mşökmfgh
        dosya = open("hesaplar.txt", "a")

        dosya.write(kulanıcı + "\n")

        dosya.write("adsoyad===hasario\n")

        dosya.write("sifre===1denemehasario\n")

        dosya.write("eposta==" + kesposta + "\n")

        dosya.write("\t\n")

        dosya.close()
        ##########################################################
        sıkayet = open("sıkayet.txt", "a")
        sıkayet.write(kesposta + " 1denemehasario\n")
        sıkayet.close()


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









