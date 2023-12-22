from selenium.webdriver.common.by import By
import time

def scrape(driver, url, business_information):

    try:
        driver.get(url)
    except:
        time.sleep(3)
        driver.refresh()
        time.sleep(2)

    time.sleep(1)
    print('\n')

    #find name
    name_element = driver.find_element(By.XPATH, "//h1[contains(@class, 'DUwDvf lfPIob')]")
    name = name_element.get_attribute('textContent')
    # if "'" in name:
    #     name = name.replace("'", '')

    #find rating
    rating_element = driver.find_element(By.XPATH, "//div[@class = 'F7nice ']")
    rating_and_num = rating_element.get_attribute('textContent')
    if rating_and_num != '':
        rating_ls = rating_and_num.split('(')
        rating = rating_ls[0]
        num_ratings = rating_ls[1].rstrip((rating_ls[1])[-1])
    else:
        rating = ''
        num_ratings = ''
    

    #find information
    information_elements = driver.find_element(By.XPATH, f"//div[contains(@aria-label, 'Information for ')]")
    info_elem = information_elements.find_elements(By.XPATH, "//div[contains(@class, 'Io6YTe fontBodyMedium kR99db ')]")


    print(name)
    info_ls = parse_information(information_elements, info_elem)
    print(info_ls)
    info_ls.insert(0, rating)
    info_ls.insert(0, num_ratings)
    business_information.update({name : info_ls})

def parse_information(information_elements, info_elem):
    info_ls = []
    for i in info_elem:
        info = i.get_attribute('textContent')
        #exclude google play address
        if len(info) >= 5:
            if info[4] == '+':
                continue
            else:

                #exclude phone link
                if 'Send to your phone' in info:
                    continue
                #exclude menus
                if info.lower() == 'menu':
                    continue
                #exclude claim this business
                if 'Claim this business' in info:
                    continue
                #exclude hours
                if ' Opens ' in info:
                    continue
                if ' Closes ' in info:
                    continue
                #find actual reference for website
                if '.com' in info:
                    try:
                        href = information_elements.find_element(By.XPATH, "//a[contains(@aria-label, 'Website: ')]")
                        website = href.get_attribute('href')
                        if website not in info_ls:
                            info_ls.append(website)
                            continue
                        else:
                            raise Exception('already exists in list')
                    #if website is already in list, look for business website
                    except:
                        href2 = information_elements.find_element(By.XPATH, "//a[@data-item-id = 'action:3']")
                        website2 = href2.get_attribute('href')
                        info_ls.append(website2)
                        continue
                #find actual reference for website
                if '.site' in info:
                    try:
                        href = information_elements.find_element(By.XPATH, "//a[contains(@aria-label, 'Website: ')]")
                        website = href.get_attribute('href')
                        if website not in info_ls:
                            info_ls.append(website)
                            continue
                        else:
                            raise Exception('already exists in list')
                    except:
                        href2 = information_elements.find_element(By.XPATH, "//a[@data-item-id = 'action:3']")
                        website2 = href2.get_attribute('href')
                        info_ls.append(website2)
                        continue
                #find actual reference for website
                if 'Search ' in info:
                        href3 = information_elements.find_element(By.XPATH, "//a[@data-item-id = 'action:5']")
                        website3 = href3.get_attribute('href')
                        info_ls.append(website3)
                        continue
                
                info_ls.append(info)

    return info_ls
        



        
