import scrapeUrlFromSearch
import scrapeInformationFromUrl
import formCsvFromInformation
from selenium import webdriver

href_list = []
business_information = {}
answers = ['yes', 'no', 'y', 'n']

count = 0
test_new_file = 'yes'

test_do = 'yes'
while test_do == 'yes' or test_do == 'y':

    test_keep = 'yes'
    while test_keep == 'yes' or test_keep == 'y':

        scrapeUrlFromSearch.list_urls(href_list)

        keep_searching = input('Would you like to add another search to this file? (yes or no): ' )
        test_keep = keep_searching.lower()
        while test_keep not in answers:
            keep_searching = input('Would you like to add another search to this file? (yes or no): ' )
            test_keep = keep_searching.lower()

    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options = options)

    load_num = 0
    for url in href_list:
        scrapeInformationFromUrl.scrape(driver, load_num, url, business_information)
        load_num += 1

    driver.quit()

    #write a new file
    if test_new_file == 'yes' or new_file == 'y':
        count += 1
        csv_name = f'data_{count}'
        formCsvFromInformation.formCsv(business_information, csv_name)
    #write into an existing file
    elif test_new_file == 'no' or new_file == 'n':
        csv_name = f'data_{count}'
        formCsvFromInformation.formCsv(business_information, csv_name)

    do = input('Do you want to search for more? (yes or no): ')
    test_do = do.lower()
    while test_do not in answers:
        do = input('Do you want to search for more? (yes or no): ')
        test_do = do.lower()
    if test_do == 'yes' or test_do == 'y':
        new_file = input('Do you want to write the search in a new CSV file? (yes or no): ')
        test_new_file = new_file.lower()
        while test_new_file not in answers:
            new_file = input('Do you want to write the search in a new CSV file? (yes or no): ')
            test_new_file = new_file.lower()
        if test_new_file == 'yes' or 'y':
            business_information.clear()
        



