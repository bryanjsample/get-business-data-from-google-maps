from selenium.webdriver.common.by import By
import time

def scrape(driver, url, business_information):

    driver.get(url)
    time.sleep(2)
    #print name
    try:
        name_element = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[1]/h1')
        name = name_element.get_attribute('textContent')
    except:
        name = 'There is no name.'
    #print rating
    try:
        rating_element = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/span[1]/span[1]')
        rating = rating_element.get_attribute('textContent')
    except:
        rating = 'There is no rating.'
    #print address
    try:
        address_element = driver.find_element(By.CLASS_NAME, value='RcCsl fVHpi w4vB1d NOE9ve M0S7ae AG25L ')
        address = address_element.get_attribute('textContent')
    except:
        address = 'There is no address.'
    #print hours
    try:
        hours_table = driver.find_element(By.CLASS_NAME, value='t39EBf GUrTXd')
        day_names = hours_table.find_elements(By.CLASS_NAME, value='ylH6lf ')
        day_hours = hours_table.find_elements(By.CLASS_NAME, value='G8aQO')
        day_name_ls = []
        day_hours_ls = []
        for n in day_names:
            name_content = n.get_attribute('textContent')
            day_name_ls.append(name_content)
        for h in day_hours:
            hours_content = h.get_attribute('textContent')
            day_hours_ls.append(hours_content)
        for i in range(7):
            hours = []
            hours.append(day_name_ls[i])
            hours.append(day_hours_ls[i])
            return hours
    except:
        hours = 'There are no hours listed.'
    #print website hrefs
    try:
        website_element = driver.find_element(By.CLASS_NAME, value='RcCsl fVHpi w4vB1d NOE9ve M0S7ae AG25L ')
        website = website_element.get_attribute('href')
    except:
        website = 'There is no website.'
    #print phone
    try:
        phone_element = driver.find_element(By.CLASS_NAME, value='RcCsl fVHpi w4vB1d NOE9ve M0S7ae AG25L ')
        phone = phone_element.get_attribute('textContent')
    except:
        phone = 'There is no phone.'
    
    business_information.update({name : [rating, address, hours, website, phone]})
    
