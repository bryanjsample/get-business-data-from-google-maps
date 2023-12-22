#extra_information will either be a string or a list
def formatForCsv(business_information):
    CsvRowValues = []
    for name, info_ls in business_information.items():
        print('\n')
        CsvRowValues.append(name)
        for items in info_ls:
            if items == '':
                items = 'N/A'
            if type(items) == str:
                CsvRowValues.append(items)
            else:
                for info in items:
                    CsvRowValues.append(info)
        print(CsvRowValues)
        CsvRowValues.clear()