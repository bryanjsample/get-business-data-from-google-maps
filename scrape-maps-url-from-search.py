from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

search = input('Search Google Maps For: ')



def scrape_url_from_search(search):
    search_url = search.replace(' ', '+')
    driver = webdriver.Chrome()
    driver.get(f'https://www.google.com/maps/search/{search_url}')

    time.sleep(5)

    div_to_scroll = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]')

    href_list = []

    for count, scrolls in enumerate(range(5)):
        if count == '0':
            time.sleep(5)
            items =  driver.find_elements(By.CLASS_NAME, value='m6QErb WNBkOb ')
            for i in items:
                href = i.get_attribute('href')
                if i:
                    href_list.append(href)
        else:
            for key_input in range(0, 20):
                div_to_scroll.send_keys(Keys.PAGE_DOWN)
            time.sleep(5)
            items =  driver.find_elements(By.CLASS_NAME, value='hfpxzc')
            for i in items:
                href = i.get_attribute('href')
                if i:
                    if href not in href_list:
                        href_list.append(href)
    for n in href_list:
        print(n)

    driver.quit()

scrape_url_from_search(search)