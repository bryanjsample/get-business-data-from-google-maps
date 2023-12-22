

def define_search():
    search = input('Search Google Maps For Information About: ')
    return search

def search_paramters():
    sizes = ['small', 's', 'medium', 'm', 'large', 'l', 'x-large', 'xlarge', 'x large', 'xl', 'xx-large', 'xxlarge', 'xx large', 'x x large', 'xxl', 'unlimited', 'ul']
    xl = ['x-large', 'xlarge', 'x large', 'xl']
    xxl = ['xx-large', 'xxlarge', 'xx large', 'x x large', 'xxl']
    search_size = input("Define search size (s, m, l, xl, xxl, unlimited (ul)): ")
    search_test = search_size.lower()
    while search_test not in sizes:
        search_size = input("Define search size (s, m, l, xl, xxl, unlimited (ul)): ")
        search_test = search_size.lower()
    if search_test == 'small' or search_test == 's':
        num_iterations = 3
    elif search_test == 'medium' or search_test == 'm':
        num_iterations = 6
    elif search_test == 'large' or search_test == 'l':
        num_iterations = 10
    elif search_test in xl:
        num_iterations = 15
    elif search_test in xxl:
        num_iterations = 20
    elif search_test == 'unlimited' or search_test == 'ul':
        num_iterations = 5000
    return num_iterations
