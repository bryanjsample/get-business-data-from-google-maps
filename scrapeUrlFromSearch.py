from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import searchParameters

def list_urls(href_list):
    search = searchParameters.define_search()
    num_iterations = searchParameters.search_paramters()


    driver = webdriver.Chrome()

    #format input for url
    search_url = search.replace(' ', '+')
    driver.get(f'https://www.google.com/maps/search/{search_url}')
    #wait 3 seconds for all contents to load
    time.sleep(3)
    #establish div to receive key down
    div_to_scroll = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]')
    #move down the page x times
    for movement in range(num_iterations):
        #this will raise an exception until end of list is reached
        try:
            driver.find_element(By.CLASS_NAME, value='HlvSq')
            print("All results acquired")
            #find all elements containing a result
            results =  driver.find_elements(By.CLASS_NAME, value='hfpxzc')
            #iterate through results
            for i in results:
                #get the url for each result
                href = i.get_attribute('href')
                #if there is a url
                if i:
                    if href not in href_list:
                        #add it to the list
                        href_list.append(href)
            return href_list
        #until the end is reached do this
        except:
            #for the first iteration
            if movement == 0:
                time.sleep(3)
                #find all elements containing a result
                results =  driver.find_elements(By.CLASS_NAME, value='hfpxzc')
                #iterate through results
                for i in results:
                    #get the url for each result
                    href = i.get_attribute('href')
                    #if there is a url
                    if i:
                        #add it to the list
                        href_list.append(href)
            else:
                #key down x times to move page
                for key_input in range(50):
                    div_to_scroll.send_keys(Keys.PAGE_DOWN)
                time.sleep(2)
                #find all elements containing a result
                results =  driver.find_elements(By.CLASS_NAME, value='hfpxzc')
                #iterate through results
                for i in results:
                    #get the url for each result
                    href = i.get_attribute('href')
                    #if there is a url
                    if i:
                        if href not in href_list:
                            #add it to the list
                            href_list.append(href)
    driver.quit()
        
