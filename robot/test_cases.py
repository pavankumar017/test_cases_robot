import utils as util
from robot.api import logger
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver
def user_is_on_home_page_of_amazon():
    """Verify that user is on home page of amazon"""
    util.driver.find_element_by_id("nav-logo")


def verify_the_page_is_displayed_in_english(txt_english):
    """verfy english language is displayed"""
    lang = util.driver.find_element_by_xpath(txt_english).text
    logger.console(lang)
    assert(lang == "EN")

def user_selects_books_from_the_drop_down():
    """select a book"""
    time.sleep(4)
    action = ActionChains(util.driver)
    ele = util.driver.find_element_by_css_selector("[id='searchDropdownBox']").click()
    action.click(ele)
    action.perform()
    
    select_dropdown =  Select(util.driver.find_element_by_css_selector("[id='searchDropdownBox']"))
    select_dropdown.select_by_visible_text("Books")

def search_book(book_name):


    """searches the book"""
    util.driver.find_element_by_id("twotabsearchtextbox").send_keys(book_name)
    util.driver.find_element_by_id("nav-search-submit-button").click()
    # adding  wait 
    WebDriverWait(util.driver , 10 ).until(EC.text_to_be_present_in_element((By.XPATH ,"//span[@class='a-color-state a-text-bold']"), "The alchemist"))




