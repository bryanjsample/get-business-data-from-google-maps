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
