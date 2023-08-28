from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager, ChromeType


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