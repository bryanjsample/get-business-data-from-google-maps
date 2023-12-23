import os

def create_dir():
    #make a directory for this search
    num_dir = 0
    dir_name = f'search_{num_dir}'
    parent_dir = os.path.dirname(__file__)
    parent_dir_ls = os.listdir(parent_dir)
    if 'searches' not in parent_dir_ls:
        os.mkdir(f'{parent_dir}/searches')
    test_dir = f'{parent_dir}/searches'
    test_dir_ls = os.listdir(test_dir)
    while dir_name in test_dir_ls:
        num_dir += 1
        dir_name = f'search_{num_dir}'
    os.mkdir(f'{test_dir}/{dir_name}')
    return (parent_dir, dir_name)

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




### ADD IN FUNCTION TO CHOOSE BETWEEN SINGLE SEARCH OR MULTI SEARCH

### MAKE MULTI SEARCH LIST TO PARSE THROUGH TO MAKE IT EASIER ON USER




def search_again(answers):
    keep_searching = input('Would you like to add an additional search to this CSV? (yes or no): ' )
    test_keep = keep_searching.lower()
    while test_keep not in answers:
        keep_searching = input('Would you like to add an additional search to this CSV? (yes or no): ' )
        test_keep = keep_searching.lower()
    return test_keep

def end_or_new(answers, csv_write, test_do, test_new_file):
    #keep going or end program?
    do = input('Do you want to search for more information? (yes or no): ')
    test_do = do.lower()
    while test_do not in answers:
        do = input('Do you want to search for more information? (yes or no): ')
        test_do = do.lower()
    #new file or same file?
    if test_do == 'yes' or test_do == 'y':
        new_file = input('Do you want to write this search in a new CSV file? (yes or no): ')
        test_new_file = new_file.lower()
        while test_new_file not in answers:
            new_file = input('Do you want to write this search in a new CSV file? (yes or no): ')
            test_new_file = new_file.lower()
        #if writing in new file, specify write
        if test_new_file == 'yes' or test_new_file == 'y':
            csv_write = 'write'
        #if not, specify append
        if test_new_file == 'no' or test_new_file == 'n':
            csv_write = 'append'
    return (test_do, test_new_file, csv_write)

