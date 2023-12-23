import csv
import os

#extra_information will either be a string or a list
def formCsv(csv_write, business_information, parent_dir, dir_name, csv_name):
    CsvRowValues = []
    headers = ['Name', 'Rating', 'Number Of Ratings', 'Address', 'Phone Number', 'Website', 'Website to Book', 'Website to Search', 'Extra Information...']
    #write csv
    if csv_write == 'write':
    #write csv file
        with open(f'{parent_dir}/searches/{dir_name}/{csv_name}.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            writer.writerow(headers)
            for name, info_ls in business_information.items():
                CsvRowValues.append(name)
                for items in info_ls:
                    if type(items) == str:
                        CsvRowValues.append(items)
                    else:
                        for info in items:
                            CsvRowValues.append(info)
                writer.writerow(CsvRowValues)
                CsvRowValues.clear()
            csvfile.close()
        print(f'{csv_name} written inside of {parent_dir}/searches/{dir_name}')
    #append csv
    if csv_write == 'append':
        with open(f'{parent_dir}/searches/{dir_name}/{csv_name}.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            for name, info_ls in business_information.items():
                CsvRowValues.append(name)
                for items in info_ls:
                    if type(items) == str:
                        CsvRowValues.append(items)
                    else:
                        for info in items:
                            CsvRowValues.append(info)
                writer.writerow(CsvRowValues)
                CsvRowValues.clear()
            csvfile.close()
        print(f'{csv_name} written inside of {parent_dir}/searches/{dir_name}')