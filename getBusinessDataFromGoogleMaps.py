import searchParameters
import scrapeUrlFromSearch
import scrapeInformationFromUrl
import formCsvFromInformation
from selenium import webdriver

href_list = []
business_information = {}
answers = ['yes', 'no', 'y', 'n']

csv_write = 'write'
csv_count = 0
new_file_test = 'yes'
    

#while loop for the entire program (after asking about a new file)
do_test = 'yes'
while do_test == 'yes' or do_test == 'y':
    #define search contents    
    searches = searchParameters.define_search()
        
    # #while loop for intial search input
    # keep_test = 'yes'
    # while keep_test == 'yes' or test_keep == 'y':
    #     #scrape urls

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

    print(href_list)
    quit()
        # #do you want to search again?
        # test_keep = searchParameters.search_again(answers)

    #initiate detached driver to find information
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option('detach', True)
    # driver = webdriver.Chrome(options = options)
    
    #scrape informatiom
    for url in href_list:
        scrapeInformationFromUrl.scrape(driver, load_num, href_list, business_information)
        load_num += 1

    driver.quit()

    #create new directory to hold csv files
    dirs = formCsvFromInformation.create_dir()
    parent_dir = dirs[0]
    dir_name = dirs[1]

    if new_file_test == 'yes' or new_file_test == 'y':
        #write a new file
        csv_count += 1
        csv_name = f'data_{csv_count}'
        formCsvFromInformation.formCsv(csv_write, business_information, parent_dir, dir_name, csv_name)
    elif new_file_test == 'no' or new_file_test == 'n':
        #write into an existing file
        csv_name = f'data_{csv_count}'
        formCsvFromInformation.formCsv(csv_write, business_information, parent_dir, dir_name, csv_name)

    #keep searching? if no, end program 
    #new file? if yes, next iteration will write in same file. if no, next iteration will write in new file.
    tests = searchParameters.end_or_new(answers, csv_write, do_test, new_file_test)
    do_test = tests[0]
    new_file_test = tests[1]
    csv_write = tests[2]
    href_list.clear()
    business_information.clear()
        



