from selenium.webdriver.common.by import By
import time

def scrape(driver, url, business_information, lengths_of_lists):

    try:
        driver.get(url)
    except:
        time.sleep(3)
        driver.refresh()
        time.sleep(2)

    time.sleep(2)
    print('\n')

    #find name
    name_element = driver.find_element(By.XPATH, "//h1[contains(@class, 'DUwDvf lfPIob')]")
    name = name_element.get_attribute('textContent')

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
    info_ls.insert(0, rating)
    info_ls.insert(1, num_ratings)
    print(info_ls)
    business_information.update({name : info_ls})

    length_of_list = len(info_elem)
    lengths_of_lists.append(length_of_list)

def parse_information(information_elements, info_elem):
    info_ls = []
    extra_info = []
    extra_info_strings =['Identifies as', 'LGBT']
    website_tags = ['.com', '.site', '.org', '.io', '.net', '.tv']
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
                tag_exists = False
                for tag in website_tags:
                    if tag in info:
                        tag_exists = True
                        try:
                            href = information_elements.find_element(By.XPATH, "//a[contains(@aria-label, 'Website: ')]")
                            website = href.get_attribute('href')
                            if website not in info_ls:
                                business_website = website
                            else:
                                raise Exception('already exists in list')
                        #if website is already in list, look for business website
                        except:
                            href2 = information_elements.find_element(By.XPATH, "//a[@data-item-id = 'action:3']")
                            website2 = href2.get_attribute('href')
                            if website2 not in info_ls:
                                booking_website = website2
                if tag_exists == True:
                    continue
                #find actual reference for website
                if 'Search ' in info:
                    href3 = information_elements.find_element(By.XPATH, "//a[@data-item-id = 'action:5']")
                    website3 = href3.get_attribute('href')
                    search_website = website3
                    continue
                extra_info_exists = False
                for s in extra_info_strings:
                    if s in info:
                        extra_info_exists = True
                        extra_info.append(info)
                if extra_info_exists == True:
                    continue
                
                info_ls.append(info)

    for i in info_ls:
        if 'Located in:' in i:
            address_location = info_ls[0] + ' | ' + info_ls[1]
            info_ls.pop(0)
            info_ls.pop(0)
            info_ls.insert(0, address_location)
        if ',' in i:
            address = i
            print(address)
    print(extra_info)
        
    return info_ls
        



        
