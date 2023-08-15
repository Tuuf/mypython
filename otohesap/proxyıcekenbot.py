from selenium import webdriver
import time
driver_path = "chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.maximize_window()
port=input("port:")
for i in range(1,999):

    driver.get("https://hidemyna.me/en/proxy-list/?start=222#list")

    time.sleep(7)

    ip_porxy=driver.find_elements_by_class_name("tdl")

    ts=driver.find_element_by_id("ports")
    ts.send_keys(port)





    for proxy in ip_porxy:
        ass=proxy.text



    dosya=open("proxyler.txt","a")
    dosya.write(str(ass)+str(port)+"\n")
    dosya.close()




