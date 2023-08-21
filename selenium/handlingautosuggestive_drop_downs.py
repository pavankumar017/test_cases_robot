from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

service = Service(executable_path=ChromeDriverManager().install())


global driver
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.maximize_window()

driver.find_element(By.ID, "autosuggest").send_keys("IND")

# NOW store all the dropdown utosuggestive in one var  - using find_elements


time.sleep(3)
drop_downs = driver.find_elements(By.CSS_SELECTOR , 'li[class="ui-menu-item"] a')
print(len(drop_downs))

# now iterate through each elemnts found using for loop and check if its india - and click 

for country in drop_downs:
    if country.text == "India":
        country.click()
        break
    # the above can be achived using  //a[text() = "India"]


# for dynamicalliy entering text box - to get the entered or selected values - we cant use .text method of selenium becoz it works only for preloaded - for this situtaion use ger_attribute


print(driver.find_element(By.ID, 'autosuggest').get_attribute('value'))