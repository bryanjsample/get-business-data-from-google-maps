

# <div align="center">get-business-data-from-google-maps :mount_fuji:</div>

**<div align="center">Python Command Line Program to scrape information from Google Maps and write into a CSV file.</div>**

---

### General Overview
- When executed, the program will:
  1. Make a directory to store CSV files in.
  2. Prompt user to search Google Maps.
  3. Obtain and store URL for each search result.
  4. Scrape each URL for business information.
  5. Write information into CSV file.

**For more information, see [Specific Details](#specific-details)**

---

### Requirements
- Python 3.12.0
  - **Package install required**
    - Selenium
- Chromium ChromeDriver
  - ChromeDriver must be located in your `PATH` : `/usr/local/bin`

---

### Initialization
1. Ensure that all [required software](#requirements) is installed.
2. Download repository template.
3. Execute `getBusinessDataFromGoogleMaps.py`

---

### Specific Details


1. `searchParameters.create_dir()` will determine if `search` directory exist, if not it will be made.
2. `searchParameters.create_dir()` will create directory named `search_X` where X is the current iteration of the program.
3. User will be prompted with `Search Google Maps For Information About: `
   - The default search location is not set. When prompted for search, it is best to include a location to search.
   - Example: `Businesses in Minneapolis`
4. User will be prompted with `Define search size (s, m, l, xl, xxl, unlimited (ul)): `
   - User input will determine the number of scrolls that ChromeDriver will perform on the search results.
     - `s` = 3 scrolls
     - `m` = 6 scrolls
     - `l` = 10 scrolls
     - `xl` = 15 scrolls
     - `xxl` = 20 scrolls
     - `ul` = 5000 scrolls (practically unlimited)
5. `scrapeUrlFromSearch.scrape_urls(href_list)` will open ChromeDriver.
   - Extracts and stores URL for each search result inside of `href_list`
6. After initial search, `searchParameters.search_again(answers)` will prompt user with `Would you like to add an additional search to this CSV? (yes or no): `
   - **If `yes`**
     - Repeat steps 2 - 4
   - **If `no`**
      - Continue
7. Iterate through URLs in `href_list`, passing each into `scrapeInformationFromUrl.scrape(driver, load_num, url, business_information)`.
   - ChromeDriver will open URL and obtain information:
      - Name
      - Rating
      - Number of Ratings
      - Address
      - Phone Number
      - Website
      - Website to Book
      - Website to Search
      - Extra Information
     - **If any information does not exist, field will be filled with `N/A` .**
   - Information is added into `business_information` dictionary
8. `formCsvFromInformation.formCsv(csv_write, business_information, dir_name, csv_name)` will write contents of `business_information` into a CSV file named `data_X` where `X` is the number of CSV files created inside of `search_X` directory.
    - This file is contained in `searches/search_X` directory inside of CWD.
9. `searchParameters.end_or_new(answers, csv_write, test_do, test_new_file)` will prompt user with `Do you want to search for more information? (yes or no): `
    - **If `yes`**
      - User will be prompted with `Do you want to write this search in a new CSV file? (yes or no): `
        - **If `yes`**
          - Repeat steps 2-7, writing into CSV file named `search_(X+1)`.
        - **If `no`**
          - Repeat steps 2-7, writing into the same CSV file.
    - **If `no`**
      - Program will end.

---

### Conclusion

##### Application

>This program functions well to quickly scrape information about a specific Google Maps search. This information can then be utilized for many different applications. For example, the information can be used to map locations of specific industries using a GIS software. 

##### Challenges

>Many challenges were faced during the production of this application. This was my first time using Selenium to manipulate a browser, and manipulating Selenium to perform a specific task was by far the biggest challenge faced. Other challenges included inconsistencies in HTML elements across search results, maintaining idempotence regardless of source directories, and writing exceptions to properly handle ChromeDriver crashing or not responding.