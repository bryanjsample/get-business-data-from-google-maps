import scrapeUrlFromSearch
import scrapeInformationFromUrl

href_list = []
business_information = {}
test_keep = 'yes'

while test_keep == 'yes':
    scrapeUrlFromSearch.list_urls(href_list)

    keep_searching = input('Would you like to search again? (yes or no): ' )
    test_keep = keep_searching.lower()

for url in href_list:
    scrapeInformationFromUrl.scrape(url, business_information)

print(business_information)

