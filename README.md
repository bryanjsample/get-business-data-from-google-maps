

# <div align="center">get-business-data-from-google-maps :mount_fuji:</div>

>**<div align="center">Python Command Line Program to scrape information from Google Maps and write into a CSV file.</div>**

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


1. If a directory named `searches` doesn't already exist inside of CWD, it will be made.
2. User will be prompted with `Search Google Maps For Information About: `
   - The default search location is not set. When prompted for search, it is best to include a location to search.
   - Example: `Businesses in Minneapolis`
3. User will be prompted with `Define search size (s, m, l, xl, xxl, unlimited (ul)): `
   - User input will determine the number of scrolls that ChromeDriver will perform on the search results.
     - `s` = 3 scrolls
     - `m` = 6 scrolls
     - `l` = 10 scrolls
     - `xl` = 15 scrolls
     - `xxl` = 20 scrolls
     - `ul` = 5000 scrolls (practically unlimited)
4. `scrapeUrlFromSearch.scrape_urls(href_list)` will open ChromeDriver.
   - Extracts and stores URL for each search result inside of `href_list`
5. After initial search, user will be prompted with `Would you like to add an additional search to this CSV? (yes or no): `
   - **If `yes`**
     - Repeat steps 2 - 4
   - **If `no`**
      - Continue
6. Iterate through URLs in `href_list`, passing each into `scrapeInformationFromUrl.scrape(driver, load_num, url, business_information)`.
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
7. `formCsvFromInformation.formCsv(business_information, dir_name, csv_name)` will write contents of `business_information` into a CSV file named `search_X` where `X` is the number of searches written into a CSV file.
    - This file is contained in `searches` directory inside of CWD.
8. User will be prompted with `Do you want to search for more information? (yes or no): `
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

>This program functions well to quickly scrape information about a specific Google Maps search. This information can then be utilized for many different applications. For example, the information can be used to map locations of specific industries using a GIS software. 
>Many challenges were faced during the production of this application. This was my first time using Selenium to manipulate a browser, and manipulating Selenium to perform a specific task was by far the biggest challenge faced. Other challenges include inconsistencies in HTML elements across search results, maintaining idempotence regardless of the system 