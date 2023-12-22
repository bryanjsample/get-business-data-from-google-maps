import csv
import os

#extra_information will either be a string or a list
def formCsv(business_information, csv_name):
    CsvRowValues = []
    cwd = os.getcwd()
    headers = ['Name', 'Rating', 'Number Of Ratings', 'Address', 'Phone Number', 'Website', 'Website to Book', 'Website to Search', 'Extra Information...']
    #write csv file
    with open(f'{cwd}/tests/{csv_name}.csv', 'w', newline='') as csvfile:
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