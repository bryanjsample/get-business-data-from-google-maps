import fastAndComprehensiveFunctions

answers = ['fast', 'f', 'comprehensive', 'c']
search_size = input('Fast search or comprehensive search? (f for fast, c for comprehensive) ').lower()
while search_size not in answers:
    search_size = input('Fast search or comprehensive search? (f for fast, c for comprehensive) ').lower()

if search_size == 'f':
    fastAndComprehensiveFunctions.fast_search()

if search_size == 'c':
    fastAndComprehensiveFunctions.comprehensive_search()
