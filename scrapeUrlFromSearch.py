from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def scrape_urls(driver, load_num, href_list, search):
    # search = searchParameters.define_search()
    # num_iterations = searchParameters.search_paramters()


    # driver = webdriver.Chrome()


    

    #ensure that there are no browser failures
    loaded = False
    compare = 0
    restart_num = 0
    search_url = search.replace(' ', '+')
    while loaded == False:
        try:
            driver.get(f'https://www.google.com/maps/search/{search_url}')
            if compare != restart_num or load_num == 0:
                time.sleep(2)
                compare = restart_num
            loaded = True
        except:
            print('\n' + 'FAILURE' + '\n')
            driver.quit()
            loaded = False
            restart_num = compare + 1
            time.sleep(5)

    # #format input for url
    # search_url = search.replace(' ', '+')
    # driver.get(f'https://www.google.com/maps/search/{search_url}')
    #wait 3 seconds for all contents to load
    time.sleep(3)
    #establish div to receive key down
    div_to_scroll = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]')
    

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
    # driver.quit()
    
