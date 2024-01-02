import fastAndComprehensiveFunctions

answers = ['fast', 'f', 'comprehensive', 'c']
search_size = input('Fast search or comprehensive search? (f for fast, c for comprehensive) ').lower()
while search_size not in answers:
    search_size = input('Fast search or comprehensive search? (f for fast, c for comprehensive) ').lower()

if search_size == 'f':
    fastAndComprehensiveFunctions.fast_search()

if search_size == 'c':
    fastAndComprehensiveFunctions.comprehensive_search()


## some zip codes had no search results, I am almost certain that the url of the empty search is getting appended into href list.
## will raise exception when trying to gather information from url
## add if statement to href exception for if no results appear
    
## added some things to scrape functions. still raising an exception when trying to differentiate the no results pages.