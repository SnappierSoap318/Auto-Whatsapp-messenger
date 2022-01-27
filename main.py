from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(EdgeChromiumDriverManager().install())

file = open("./numbers.txt") # Containing name and number in the format specified in file
numbers = file.readlines()
whatsapp_invite = "https://web.whatsapp.com/send?phone="
string = "Hey {0}," #Modify this to change what you send
name = ''
driver.get('https://web.whatsapp.com/')
input('After scanning the QR Code please press enter')
for i in numbers:
    name = i.split()[0].replace('.',' ')
    number = i.split()[1]
    driver.get(whatsapp_invite + i + "&text=" + string.format(name))
    while True:
        try:
            send_button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
            send_button.click()
            try:
                alert = driver.switch_to.alert()
                alert.accept()
            except:
                pass
            break
        except:
            WebDriverWait(driver, 5)
    name = ''