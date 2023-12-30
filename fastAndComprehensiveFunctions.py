import searchParameters
import zipCodes
import scrapeUrlFromSearch
import scrapeInformationFromUrl
import formCsvFromInformation

from selenium import webdriver

def fast_search():
    href_list = []
    business_information = {}
    answers = ['yes', 'no', 'y', 'n']

    csv_write = 'write'
    csv_count = 0
    new_file = 'yes'

    #while loop for the entire program (after asking about a new file)
    do = 'yes'
    while do == 'yes' or do == 'y':
        #define search contents    
        searches = searchParameters.define_search()

        #establish chromedriver to stay open with each driver.get()
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(options = options)
        
        #load_num will determine wait time for window
        load_num = 0
        #extract search result urls
        for search in searches:
            scrapeUrlFromSearch.scrape_urls(driver, load_num, href_list, search)
            load_num += 1

        #scrape informatiom
        for url in href_list:
            scrapeInformationFromUrl.scrape(driver, load_num, url, business_information)
            load_num += 1

        driver.quit()

        #create new directory to hold csv files
        dirs = formCsvFromInformation.create_dir()
        parent_dir = dirs[0]
        dir_name = dirs[1]

        if new_file == 'yes' or new_file == 'y':
            #write a new file
            csv_count += 1
            csv_name = f'data_{csv_count}'
            formCsvFromInformation.formCsv(csv_write, business_information, parent_dir, dir_name, csv_name)
        elif new_file == 'no' or new_file == 'n':
            #write into an existing file
            csv_name = f'data_{csv_count}'
            formCsvFromInformation.formCsv(csv_write, business_information, parent_dir, dir_name, csv_name)

        #keep searching? if no, end program 
        #new file? if yes, next iteration will write in same file. if no, next iteration will write in new file.
        triggers = searchParameters.end_or_new(answers, csv_write, do, new_file)
        do = triggers[0]
        new_file = triggers[1]
        csv_write = triggers[2]
        href_list.clear()
        business_information.clear()

def comprehensive_search():
    href_list = []
    business_information = {}
    answers = ['yes', 'no', 'y', 'n']

    csv_write = 'write'
    csv_count = 0
    new_file = 'yes'

    #while loop for the entire program (after asking about a new file)
    do = 'yes'
    while do == 'yes' or do == 'y':
        #define search area, search topic, and find all zip codes within search area
        searches = zipCodes.comp_searches()

        #establish chromedriver to stay open with each driver.get()
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(options = options)

        #load_num will determine wait time for window
        load_num = 0
        #extract search result urls
        for search in searches:
            scrapeUrlFromSearch.scrape_urls(driver, load_num, href_list, search)
            load_num += 1

        #scrape informatiom
        for url in href_list:
            scrapeInformationFromUrl.scrape(driver, load_num, url, business_information)
            load_num += 1

        driver.quit()

        #create new directory to hold csv files
        dirs = formCsvFromInformation.create_dir()
        parent_dir = dirs[0]
        dir_name = dirs[1]

        if new_file == 'yes' or new_file == 'y':
            #write a new file
            csv_count += 1
            csv_name = f'data_{csv_count}'
            formCsvFromInformation.formCsv(csv_write, business_information, parent_dir, dir_name, csv_name)
        elif new_file == 'no' or new_file == 'n':
            #write into an existing file
            csv_name = f'data_{csv_count}'
            formCsvFromInformation.formCsv(csv_write, business_information, parent_dir, dir_name, csv_name)

        #keep searching? if no, end program 
        #new file? if yes, next iteration will write in same file. if no, next iteration will write in new file.
        triggers = searchParameters.end_or_new(answers, csv_write, do, new_file)
        do = triggers[0]
        new_file = triggers[1]
        csv_write = triggers[2]
        href_list.clear()
        business_information.clear()