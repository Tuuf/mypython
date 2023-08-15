from selenium import webdriver
from  selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os

import time
import requests
import random
print("ornek 1.1.1.1:port")
proxy=input("proxy giriniz:")
PROXY = proxy
webdriver.DesiredCapabilities.CHROME['proxy']={
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,
    "noProxy":None,
    "proxyType":"MANUAL",
    "autodetect":False
}





a = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=a)

sifren="1denemehasario"
for i in range(1,999):
    driver.get("https://temp-mail.org/tr/")
    kesposta = driver.find_element_by_xpath('//*[@id="mail"]').get_attribute("value")
    copy_xpath = driver.find_element_by_xpath('//*[@id="click-to-copy"]').click()
    delete_xpath = driver.find_element_by_xpath('//*[@id="click-to-delete"]').click()
    time.sleep(2)

    driver.get("https://www.instagram.com/")
    time.sleep(2)

    eposta=driver.find_element_by_name("emailOrPhone")
    eposta.send_keys(Keys.CONTROL,"v")

   
    time.sleep(2)
    adsoyad=driver.find_element_by_name("fullName")

    adsoyad.send_keys("hasario")
    kadı=driver.find_element_by_name("username")
    taktaktak=random.randint(1,10000)
    masa=("hasario"+str(taktaktak))
    kadı.send_keys(masa)
    ################


    sıfre=driver.find_element_by_name("password")
    sıfre.send_keys(sifren)
    time.sleep(3)

    time.sleep(2)
    buton=driver.find_element_by_xpath("//button[@type='submit']")
    buton.click()
    time.sleep(5)
    driver.get("https://www.instagram.com/"+masa)
    time.sleep(3)


    cıkış=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div/button/span')
    cıkış.click()
    time.sleep(2)
    gogo=driver.find_element_by_xpath('/html/body/div[3]/div/div/div/button[6]')
    time.sleep(5)
    gogo.click()






    time.sleep(1)
    print("#"*10)
    print("kulanıcı adı :=:=:"+masa)
   #print(masa)
    print("#"*20)
    print("adsoyad:=:=:""hasario")
    print("#"*20)
    print("sifre:=:=:"+sifren)
    print("#"*20)
    print("epostanız=="+kesposta)
    #print(posta)
    print("#"*20)
    ################
    print("başarıyla hesabınız oluşturulmuştur ")
    kulanıcı=("KULANICIADI=="+masa)

    r=requests.get("https://www.instagram.com/"+masa)
    xx=r.status_code
    a=print(xx)
    #Buraya kadar çalışıyor UHUSDFKSLŞFSLK sonunda lan jsklfsddfsdjklfsdklfdsxfgljköşmrtçhyçö.mşökmfgh
    dosya=open("hesaplar.txt","a")


    dosya.write(kulanıcı+"\n")

    dosya.write("adsoyad===hasario\n")

    dosya.write("sifre===1denemehasario\n")


    dosya.write("eposta=="+kesposta+"\n")

    dosya.write("\t\n")

    dosya.close()
   ##########################################################
    sıkayet=open("sıkayet.txt","a")
    sıkayet.write(kesposta+" 1denemehasario\n")
    sıkayet.close()











