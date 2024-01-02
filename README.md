

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
- [Python 3.12.0](https://www.python.org/)
  - **Package install required**
    - [Selenium](https://pypi.org/project/selenium/)
- [Chromium ChromeDriver](https://chromedriver.chromium.org/downloads/version-selection)
  - ChromeDriver must be located in your `PATH` : `/usr/local/bin`

---

### Initialization
1. Ensure that all [required software](#requirements) is installed.
2. Download repository template.
3. Execute `main.py`

---

### Specific Details

1. User will be prompted with `Fast or comprehensive search?`
   - **Fast Search**
      1. User will be prompted with `Search Google Maps For Information About: `
         - The default search location is not set. When prompted for search, it is best to include a location to search.
         - Example: `Businesses in Minneapolis`
   - **Comprehensive Search**
      1. User will be prompted with `What state would you like to search inside of?`
          - Example: `Colorado`
      2. User will be prompted with `What city would you like to search inside of?`
          - Input must be a city that is located inside of the selected state.
          - Example: `Colorado Springs`
      3. [`zipCodes.find_zip()`](https://github.com/bryanjsample/get-business-data-from-google-maps/blob/8f4f7bbb4131b1429fe6c6eb8ed79729944f4ab2/zipCodes.py) will form a list of all zip codes associated with that city.
      3. User will be prompted with `What are you searching for? (Fast food, restaurants, businesses, etc.)`
          - The more specific, the better.
          - Examples: `Tech Companies`, `Fast Food`, `Businesses`, `Electric Companies`, etc.
      4. [`zipCodes.comp_searches()`](https://github.com/bryanjsample/get-business-data-from-google-maps/blob/8f4f7bbb4131b1429fe6c6eb8ed79729944f4ab2/zipCodes.py) will form a string that will be used to search google maps, then user will be prompted to confirm the search string.
          - Example: 
              ```
              Searching for: 'Tech Companies in Colorado Springs, Colorado'
              Is that correct?
              ```
      5. After confirmation, [`zipCodes.comp_searches()`](https://github.com/bryanjsample/get-business-data-from-google-maps/blob/8f4f7bbb4131b1429fe6c6eb8ed79729944f4ab2/zipCodes.py) will form a list of search queries containing each zip code listed within the given city.
          - Example:
              ```
              [
                'Tech Companies in 80923',
                'Tech Companies in 80924',
                'Tech Companies in 80927',
                'Tech Companies in 80941',
                'Tech Companies in 80970'
              ]
              ```
2. [`scrapeUrlFromSearch.scrape_urls(href_list)`](https://github.com/bryanjsample/get-business-data-from-google-maps/blob/68d8a0237978bdf3cf5f5f195cb430300435fd68/scrapeUrlFromSearch.py) will open ChromeDriver.
   - Extracts and stores URL for each search result inside of `href_list`
3. After initial search, [`searchParameters.search_again(answers)`](https://github.com/bryanjsample/get-business-data-from-google-maps/blob/68d8a0237978bdf3cf5f5f195cb430300435fd68/searchParameters.py) will prompt user with `Would you like to add an additional search to this CSV? (yes or no): `
   - **If `yes`**
     - Repeat steps 2 - 4
   - **If `no`**
      - Continue
4. Iterate through URLs in `href_list`, passing each into [`scrapeInformationFromUrl.scrape(driver, load_num, url, business_information)`](https://github.com/bryanjsample/get-business-data-from-google-maps/blob/68d8a0237978bdf3cf5f5f195cb430300435fd68/scrapeInformationFromUrl.py).
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
     - ***If any information does not exist, field will be filled with `N/A` .***
   - Information is added into `business_information` dictionary
5. [`formCsvFromInformation.formCsv(csv_write, business_information, dir_name, csv_name)`](https://github.com/bryanjsample/get-business-data-from-google-maps/blob/68d8a0237978bdf3cf5f5f195cb430300435fd68/formCsvFromInformation.py) will write contents of `business_information` into a CSV file named `data_X` where `X` is the number of CSV files created inside of `search_X` directory.
    - This file is contained in `searches/search_X` directory inside of CWD.
6. [`searchParameters.end_or_new(answers, csv_write, test_do, test_new_file)`](https://github.com/bryanjsample/get-business-data-from-google-maps/blob/68d8a0237978bdf3cf5f5f195cb430300435fd68/searchParameters.py) will prompt user with `Do you want to search for more information? (yes or no): `
    - **If `yes`**
      - User will be prompted with `Do you want to write this search in a new CSV file? (yes or no): `
        - **If `yes`**
          - Repeat steps 2-7, writing into CSV file named `search_(X+1)`.
        - **If `no`**
          - Repeat steps 2-7, writing into the same CSV file.
    - **If `no`**
      - Program will end.

---

##### Application

>This program functions well to quickly scrape information about a specific Google Maps search. This information can then be utilized for many different applications. For example, the information can be used to map locations of specific industries using a GIS software. 

##### Challenges

>Many challenges were faced during the production of this application. This was my first time using Selenium to manipulate a browser, and manipulating Selenium to perform a specific task was by far the biggest challenge faced. Other challenges included inconsistencies in HTML elements across search results, maintaining idempotence regardless of source directories, and writing exceptions to properly handle ChromeDriver crashing or not responding.
