import time
from selenium import webdriver
driver = webdriver.Chrome("C:/Users/sbolleddu/Downloads/chromedriver_win32/chromedriver.exe")
driver.maximize_window()
driver.get('https://www.amazon.in/')
listA = driver.find_elements_by_xpath("//a")
tempo = 0
for each in listA:
    tempo = tempo+1

    if each.text == "Amazon Pay":
        time.sleep(5)
        driver.find_element_by_partial_link_text(each.text).click()
        break
print(tempo)

for each in listA:
    tempo = tempo+1

    if each.text == "Amazon Pay":
        time.sleep(5)
        driver.find_element_by_partial_link_text(each.text).click()
        break
print(tempo)