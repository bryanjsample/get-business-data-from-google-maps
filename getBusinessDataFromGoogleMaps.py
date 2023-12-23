import searchParameters
import scrapeUrlFromSearch
import scrapeInformationFromUrl
import formCsvFromInformation
from selenium import webdriver

href_list = []
business_information = {}
answers = ['yes', 'no', 'y', 'n']

csv_write = 'write'
count = 0
test_new_file = 'yes'

#while loop for the entire program (after asking about a new file)
test_do = 'yes'
while test_do == 'yes' or test_do == 'y':
        
    #while loop for intial search input
    test_keep = 'yes'
    while test_keep == 'yes' or test_keep == 'y':
        #scrape urls
        scrapeUrlFromSearch.scrape_urls(href_list)
        #do you want to search again?
        test_keep = searchParameters.search_again(answers)

    #initiate detached driver to find information
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options = options)
    
    #scrape information, load_num will determine wait time for window
    load_num = 0
    for url in href_list:
        scrapeInformationFromUrl.scrape(driver, load_num, url, business_information)
        load_num += 1

    driver.quit()

    #create new directory to hold csv files
    dirs = searchParameters.create_dir()
    parent_dir = dirs[0]
    dir_name = dirs[1]

    if test_new_file == 'yes' or test_new_file == 'y':
        #write a new file
        count += 1
        csv_name = f'data_{count}'
        formCsvFromInformation.formCsv(csv_write, business_information, parent_dir, dir_name, csv_name)
    elif test_new_file == 'no' or test_new_file == 'n':
        #write into an existing file
        csv_name = f'data_{count}'
        formCsvFromInformation.formCsv(csv_write, business_information, parent_dir, dir_name, csv_name)

    #keep searching? if no, end program 
    #new file? if yes, clear business information
    tests = searchParameters.end_or_new(answers, csv_write, test_do, test_new_file)
    test_do = tests[0]
    test_new_file = tests[1]
    csv_write = tests[2]
    href_list.clear()
    business_information.clear()
        



