from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.google.com/maps/search/restaurants+in+bemidji')

items = driver.find_elements(by=By.CLASS_NAME, value='hfpxzc')




    


driver.quit()