from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os

import time
import requests
import random


a = "/home/hasario/Desktop/chromedriver"
driver = webdriver.Chrome(executable_path=a)

sifren = "deniz123"
for i in range(1, 999):
    driver.get("https://tempail.com/tr/")
    time.sleep(8)
    tıkla = driver.find_element_by_id("eposta_adres")
    tıkla.click()
    karekod = driver.find_element_by_xpath('/html/body/section[1]/div[2]/div/div[4]/a[3]')
    karekod.click()
    time.sleep(2)
    postas = driver.find_element_by_xpath('/html/body/section[1]/div[2]/div/div[3]/div/h2/span')
    kesposta = postas.text
    referle = driver.find_element_by_class_name("yoket-link")
    referle.click()
    time.sleep(2)
    driver.get("https://www.instagram.com/")
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
    driver.get("https://www.instagram.com/"+masa)
    time.sleep(3)

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










