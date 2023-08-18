from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager



def open_browser(url):
   global driver
   driver = webdriver.Firefox(
            executable_path=GeckoDriverManager().install()
        )
   driver.get(url)
   driver.maximize_window()


def close_browser():
    driver.quit()