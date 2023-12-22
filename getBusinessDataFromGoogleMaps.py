import scrapeUrlFromSearch
import scrapeInformationFromUrl
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

for url in href_list:
    scrapeInformationFromUrl.scrape(driver, url, business_information)

driver.quit()

# for info in business_information:
#     print(info)
#     print('\n')

