import scrapeUrlFromSearch
import scrapeInformationFromUrl
from selenium import webdriver

href_list = []
business_information = {}
test_keep = 'yes'
lengths_of_lists = []

while test_keep == 'yes':
    scrapeUrlFromSearch.list_urls(href_list)

    keep_searching = input('Would you like to search again? (yes or no): ' )
    test_keep = keep_searching.lower()

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options = options)

for url in href_list:
    scrapeInformationFromUrl.scrape(driver, url, business_information, lengths_of_lists)

driver.quit()

for info in business_information:
    print(info)
    print('\n')


print(lengths_of_lists)