
def define_search():
    searches = []
    answers = ['yes', 'y', 'no', 'n']

    # keep asking for searches until user confirms there are no more
    done_searching_test = 'no'
    while done_searching_test == 'no' or done_searching_test == 'n':
        search = input('Search Google Maps For Information About: ')
        #append each search into searches list
        searches.append(search)
        done_searching = input('Are you finished inputting searches? (yes or no): ')
        done_searching_test = done_searching.lower()
        while done_searching_test not in answers:
            done_searching = input('Are you finished inputting searches? (yes or no): ')
            done_searching_test = done_searching.lower()
    return searches
            
# AT END OF PROGRAM....do you want to do another?
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

def state_search():
    state_names = ['']
    state_full = input('What state would you like to search inside of? ')
