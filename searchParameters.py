

def define_search():
    search = input('Search Google Maps For Information About: ')
    return search

def search_paramters():
    sizes = ['small', 'medium', 'large', 'x-large', 'xlarge', 'x large', 'xl', 'xx-large', 'xxlarge', 'xx large', 'x x large', 'xxl']
    xl = ['x-large', 'xlarge', 'x large', 'xl']
    xxl = ['xx-large', 'xxlarge', 'xx large', 'x x large', 'xxl']
    search_size = input("Define search size (small, medium, large, x-large, xx-large): ")
    search_test = search_size.lower()
    while search_test not in sizes:
        search_size = input("Define search size (small, medium, large, x-large, xx-large): ")
        search_test = search_size.lower()
    if search_test == 'small':
        num_iterations = 3
    elif search_test == 'medium':
        num_iterations = 6
    elif search_test == 'large':
        num_iterations = 10
    elif search_test in xl:
        num_iterations = 15
    elif search_test in xxl:
        num_iterations = 20
    return num_iterations
