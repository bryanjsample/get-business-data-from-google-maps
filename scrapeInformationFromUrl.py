from selenium.webdriver.common.by import By
import time

def scrape(driver, url, business_information):

    driver.get(url)
    time.sleep(2)
    #print name
    name_element = driver.find_element(By.XPATH, "//h1[contains(@class, 'DUwDvf lfPIob')]")
    name = name_element.get_attribute('textContent')
    print(name)
    #print information
    information_elements = driver.find_element(By.XPATH, f"//div[@aria-label = 'Information for {name}']")
    info_elem = information_elements.find_elements(By.XPATH, "//div[contains(@class, 'Io6YTe fontBodyMedium kR99db ')]")
    print('\n')
    for i in info_elem:
        info = i.get_attribute('textContent')
        if len(info) >= 5:
            if info[4] == '+':
                continue
        if 'Send to your phone' in info:
            continue
        if 'Menu' in info:
            continue
        if '.com' in info:
            href = information_elements.find_element(By.XPATH, "//a[contains(@aria-label, 'Website')]")
            website = href.get_attribute('href')
            info = website
        
        print(info)



        
