from selenium import webdriver
from  selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os

import time

import requests
import random




def program():
    from selenium import webdriver
    from  selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options
    import os

    import time
    import requests
    import random


    driver_path = "home/hasario/Desktop/chromedriver"


    PROXY = "125.26.7.85:54888" # IP:PORT or HOST:PORT

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % PROXY)

    driver = webdriver.Chrome(options=chrome_options)

    sifren="1denemehasario"
    driver.get("https://temp-mail.org/tr/")
    kesposta=driver.find_element_by_xpath('//*[@id="mail"]').get_attribute("value")
    copy_xpath=driver.find_element_by_xpath('//*[@id="click-to-copy"]').click()
    delete_xpath=driver.find_element_by_xpath('//*[@id="click-to-delete"]').click()
    time.sleep(2)
           
    driver.get("https://www.instagram.com/")
    time.sleep(2)

    eposta=driver.find_element_by_name("emailOrPhone")
    time.sleep(3)
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
    driver.close()
       ##########################################################
    sıkayet=open("sıkayet.txt","a")
    sıkayet.write(kesposta+" 1denemehasario\n")
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










