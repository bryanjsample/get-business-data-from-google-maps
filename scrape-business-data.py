from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium 
from bs4 import BeautifulSoup


driver = webdriver.Chrome()

driver.get('https://www.google.com/maps/search/restaurants+in+bemidji')

items =  driver.find_elements(By.CLASS_NAME, value='hfpxzc')

for i in items:
    href = i.find_element(By.XPATH, '//href[@href]')
    print(href.text)


    



    


driver.quit()