from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager, ChromeType
import json
import jsonpath

def open_browser(url):
   global driver
#    driver = webdriver.Firefox(
#             executable_path=GeckoDriverManager().install()
#         )
   # driver.get(url)
   driver = webdriver.Chrome(executable_path="/Users/pavankumar/VSCODE/test_cases_robot/chromedriver")  

   # s = Service("/Users/pavankumar/VSCODE/test_cases_robot/chromedriver")
   # driver = webdriver.Chrome(service=s)      
   driver.maximize_window()
   driver.get(url)
    # driver = webdriver.Chrome(executable_path=ChromeDriverManager(chrome_type=ChromeType.CHROMIUM)).install()
    # 
    # 
    # driver = webdriver.Chrome()
    # driver.get("https://www.crawler-test.com")
    # print(driver.title)

    

def close_browser():
    driver.quit()


def get_element(location_name):
    """to access the element using the jsonpath provided"""
    file_path = open("/Users/pavankumar/VSCODE/test_cases_robot/shopping-website/Locators/locators.json", "r", encoding="UTF-8")
    response = json.loads(file_path.read())
    value = jsonpath.jsonpath(response, location_name)
    file_path.close()
    return value[0]


def get_constant_data(location_name):
    """to access the constane value using the jsonpath provided"""
    file_path = open("/Users/pavankumar/VSCODE/test_cases_robot/shopping-website/Locators/consant.json", "r", encoding="UTF-8")
    response = json.loads(file_path.read())
    value = jsonpath.jsonpath(response, location_name)
    file_path.close()
    return value[0]