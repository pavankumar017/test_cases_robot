from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service = Service(executable_path=ChromeDriverManager().install())


global driver
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get("https://rahulshettyacademy.com/AutomationPractice/")


# writing CSS SYNTAX = tagname[attribute='value']-->  input[type = 'submit']   - also for ID - use #idvalue  - ex = #name




# writing xpath syntax = //tagname[@attributename = 'value']  --> //input[@type='submit']
# if there are multiple elements with same locator values then  -  (//input[@type='submit'])[2] - This selects 2nd elemnt with same value

# different ways of finding the locators ?
    #  to find using link text --> THE tag should start with "a" only
driver.find_element(By.LINK_TEXT , "Free Access to InterviewQues/ResumeAssistance/Material").click()
driver.back()


# parent to child traversing - Use one "/"   for CSS - Give space only  - also instead of [] in Css ()
# driver.find_element(By.XPATH ,  "")


# BASED ON TEXT   -- //tagname[text()="entire text"]
driver.find_element(By.XPATH, "//button[text()='Home']").click()
driver.back()

# testing for static dropdowns  - Use select class
dropdown = Select(driver.find_element(By.ID , "dropdown-class-example"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Option2")
dropdown.select_by_value("option3")


# handling java script alrert
driver.find_element(By.CSS_SELECTOR , "#name").send_keys("pAVAN")
driver. find_element(By.CSS_SELECTOR , "#confirmbtn").click()

alert = driver.switch_to.alert
print(alert.text)
# to accept the alert 
alert.accept() 

# to cancel alert 
alert.dismiss()


