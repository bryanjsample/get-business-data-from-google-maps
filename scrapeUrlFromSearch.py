from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def scrape_urls(driver, load_num, href_list, search):
    #ensure that there are no browser failures
    loaded = False
    compare = 0
    restart_num = 0
    search_url = search.replace(' ', '+')
    while loaded == False:
        try:
            driver.get(f'https://www.google.com/maps/search/{search_url}')
            if compare != restart_num or load_num == 0:
                time.sleep(3)
                compare = restart_num
            loaded = True
        except:
            print('\n' + 'FAILURE' + '\n')
            time.sleep(2)
            driver.refresh()
            loaded = False
            restart_num = compare + 1
            time.sleep(3)

    #wait 3 seconds for all contents to load        
    time.sleep(2)
    #check to see how many results there are
    try:
        div_to_scroll = driver.find_element(By.XPATH, "//div[contains(@aria-label, 'Results for')]")
        div_to_scroll.send_keys(Keys.ARROW_DOWN)
    except:
        #if no results are present
        try:
            no_results_page = driver.find_element(By.XPATH, "//div[@class = 'Q2vNVc']")
            no_results = no_results_page.get_attribute('textContent')
            print(f'No results found for: {search}')
            return
        #if one result is present
        except:
            single_result = driver.current_url
            if single_result not in href_list:
                #add it to the list
                href_list.append(single_result)
                return

    #this will raise an exception until end of list is reached
    bottom = ''
    while bottom != 'found':
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
            bottom = 'found'

        #until the end is reached do this
        except:
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