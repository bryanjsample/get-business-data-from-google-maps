import pandas
import os


# one time function, already ran
def clean_csv():
    parent_dir = os.path.dirname(__file__)
    df = pandas.read_csv(f'{parent_dir}/all_zip_codes.csv', delimiter = ',', header = 0, dtype = str)
    df.drop(['type', 'decommissioned', 'unacceptable_cities', 'timezone', 'area_codes', 'world_region', 'country', 'latitude', 'longitude', 'irs_estimated_population'], axis = 1, inplace = True)
    # drop any non-states
    # american samoa
    df.drop(df[df['state'] == 'AS'].index, inplace = True)
    # federated states of micronesia
    df.drop(df[df['state'] == 'FM'].index, inplace = True)
    # guam
    df.drop(df[df['state'] == 'GU'].index, inplace = True)
    # marshall islands
    df.drop(df[df['state'] == 'MH'].index, inplace = True)
    # northern mariana islands
    df.drop(df[df['state'] == 'MP'].index, inplace = True)
    # puerto rico
    df.drop(df[df['state'] == 'PR'].index, inplace = True)
    # virgin islands
    df.drop(df[df['state'] == 'VI'].index, inplace = True)
    # armed forces americas
    df.drop(df[df['state'] == 'AA'].index, inplace = True)
    # armed forces europe
    df.drop(df[df['state'] == 'AE'].index, inplace = True)
    # armed forces pacific
    df.drop(df[df['state'] == 'AP'].index, inplace = True)
    # form new filtered csv
    df.to_csv('filtered_zip_codes.csv', index = False)

def find_zip(zip_list, state_abbr, city):
    parent_dir = os.path.dirname(__file__)
    df = pandas.read_csv(f'{parent_dir}/filtered_zip_codes.csv', delimiter = ',', header = 0, dtype = str)
    # filter out any other states
    df.drop(df[df['state'] != state_abbr].index, inplace = True)
    # filter other cities
    acceptable_df = df[df['acceptable_cities'].str.contains(str(city)) == True]
    primary_df = df[df['primary_city'] == city]
    #add zips into list
    for row in acceptable_df.itertuples():
        zip_code = row.zip
        if zip_code not in zip_list:
            zip_list.append(zip_code)
    #add zips into list
    for row in primary_df.itertuples():
        zip_code = row.zip
        if zip_code not in zip_list:
            zip_list.append(zip_code)

def comp_searches():
    state_names = {
        'alabama' : 'AL',
        'alaska' : 'AK',
        'arizona' : 'AZ',
        'arkansas' : 'AR',
        'california' : 'CA',
        'colorado' : 'CO',
        'connecticut' : 'CT',
        'delaware' : 'DE',
        'washington dc' : 'DC',
        'washington d.c.' : 'DC',
        'dc' : 'DC',
        'd.c.' : 'DC',
        'florida' : 'FL',
        'georgia' : 'GA',
        'hawaii' : 'HI',
        'idaho' : 'ID',
        'illinois' : 'IL',
        'iowa' : 'IA',
        'kansas' : 'KS',
        'kentucky' : 'KY',
        'louisiana' : 'LA',
        'maine' : 'ME',
        'maryland' : 'MD',
        'massachusetts' : 'MA',
        'michigan' : 'MI',
        'minnesota' : 'MN',
        'mississippi' : 'MS',
        'missouri' : 'MO',
        'montana' : 'MT',
        'nebraska' : 'NE',
        'nevada' : 'NV',
        'new hampshire' : 'NH',
        'new jersey' : 'NJ',
        'new mexico' : 'NM',
        'new york' : 'NY',
        'north carolina' : 'NC',
        'north dakota' : 'ND',
        'ohio' : 'OH',
        'oklahoma' : 'OK',
        'oregon' : 'OR',
        'pennsylvania' : 'PA',
        'rhode island' : 'RI',
        'south carolina' : 'SC',
        'south dakota' : 'SD',
        'tennessee' : 'TN',
        'texas' : 'TX',
        'utah' : 'UT',
        'vermont' : 'VT',
        'virginia' : 'VA',
        'washington' : 'WA',
        'west virginia' : 'WV',
        'wisconsin' : 'WI',
        'wyoming' : 'WY',
    }

    zip_list = []
    
    confirm = 'n'
    while confirm == 'n' or confirm == 'no':
        state = input('What state would you like to search inside of? ').lower()
        while state not in state_names:
            state = input('State name not found, please enter a valid US state: ').lower()
        state_abbr = state_names[state]
        city = input('What city do you want to search? ').title()
        find_zip(zip_list, state_abbr, city)
        # form search string
        searches = []
        search_topic = input('What are you searching for? (Fast food, restaurants, businesses, etc.) ')
        answers = ['yes', 'y', 'no', 'n']
        confirm = input(f"\nSearching for: '{search_topic} in {city}, {state}'\nIs that correct? (y or n) ").lower()
        while confirm not in answers:
            confirm = input(f"\nSearching for: '{search_topic} in {city}, {state}'\nIs that correct? (y or n) ").lower()
    if confirm == 'yes' or confirm == 'y':
        for zip in zip_list:
            search = f'{search_topic} in {zip}'
            searches.append(search)
        return searches

