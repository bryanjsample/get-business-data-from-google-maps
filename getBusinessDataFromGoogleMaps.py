import scrapeUrlFromSearch
import scrapeInformationFromUrl
import formCsvFromInformation
from selenium import webdriver

href_list = []
business_information = {}

test_keep = 'yes'
while test_keep == 'yes':
    scrapeUrlFromSearch.list_urls(href_list)

    keep_searching = input('Would you like to search again? (yes or no): ' )
    test_keep = keep_searching.lower()

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options = options)

load_num = 0
for url in href_list:
    scrapeInformationFromUrl.scrape(driver, load_num, url, business_information)
    load_num += 1

driver.quit()

formCsvFromInformation.formatForCsv(business_information)

