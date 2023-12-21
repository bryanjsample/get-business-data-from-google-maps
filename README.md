# get-business-data-from-google-maps
 Python web scraping script to extract information from businesses in Bemidji, MN.


### Notes

---

### In maps search window
  
- Link to search result in list
  - `<a class="hfpxzc`
- Search Results XPATH to scroll
  - `/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]`


### In result page 

- **Name of Business**
  - `<h1 class="DUwDvf lfPIob">`
- **Address**
  - `<<div class="Io6YTe fontBodyMedium kR99db ">`
- **Phone Number**
  - `<div class="Io6YTe fontBodyMedium kR99db ">`
- **Reviews**
  - `<div class="F7nice ">`
    - `<span aria-hidden="true">5.0</span>`
- **Hours**
  - `<div class="OqCZI fontBodyMedium VrynGf WVXvdc">`
    - Table
      - `<div class="t39EBf GUrTXd">`
      - Day
        - `<td class="ylH6lf ">`
      - Hours
        - `<td class="mxowUb">`
          - `<li class="G8aQO">`
- **Website**
  - `<a class="CsEnBe" href="">` 

---

#### Pseudo

1. Access Google Maps search with Selenium
2. Access href of search result (add to list for duplicate protection? if in list dont do it)
   1. Add name of business to list
   2. If theres an address save to list
   3. If theres a website save to list
   4. If theres a phone number save to list
   5. If there are listed hours save to list
   6. If there are reviews save to list