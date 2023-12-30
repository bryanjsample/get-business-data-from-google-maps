def define_search():
    searches = []
    answers = ['yes', 'y', 'no', 'n']

    # keep asking for searches until user confirms there are no more
    done_searching = 'no'
    while done_searching == 'no' or done_searching == 'n':
        search = input('Search Google Maps For Information About: ')
        #append each search into searches list
        searches.append(search)
        done_searching = input('Are you finished inputting searches? (yes or no): ').lower()
        while done_searching not in answers:
            done_searching = input('Are you finished inputting searches? (yes or no): ').lower()
    return searches
            
# AT END OF PROGRAM....do you want to do another?
def end_or_new(answers, csv_write, do, new_file):
    #keep going or end program?
    do = input('Do you want to search for more information? (yes or no): ').lower()
    while do not in answers:
        do = input('Do you want to search for more information? (yes or no): ').lower()
    #new file or same file?
    if do == 'yes' or do == 'y':
        new_file = input('Do you want to write this search in a new CSV file? (yes or no): ').lower()
        while new_file not in answers:
            new_file = input('Do you want to write this search in a new CSV file? (yes or no): ').lower()
        #if writing in new file, specify write
        if new_file == 'yes' or new_file == 'y':
            csv_write = 'write'
        #if not, specify append
        if new_file == 'no' or new_file == 'n':
            csv_write = 'append'
    return (do, new_file, csv_write)
