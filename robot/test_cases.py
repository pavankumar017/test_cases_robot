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
    # # adding  wait 
    ele = "//span[contains(text(),'1-16 of over 5,000 results for')]"
    WebDriverWait(util.driver , 10 ).until(EC.presence_of_element_located((By.XPATH ,ele)))

    res = util.driver.find_element_by_xpath("//span[contains(text(),'1-16 of over 5,000 results for')]/following-sibling::span[2]").text
    
    logger.console(res)
    logger.console(book_name)
    assert book_name in res

def searched_page():
    res = util.driver.find_element_by_xpath("//span[contains(text(),'1-16 of over 5,000 results for')]/following-sibling::span[2]").text
    
    logger.console(res)
    assert "The Alchemist" in res

def selects_most_gfted_book():
    util.driver.find_element_by_xpath("//span[contains(text() , 'Best seller')]").click()
                                           

def adds_to_cart():
    window_after = util.driver.window_handles[1]
    util.driver.switch_to(window_after)

    util.driver.find_element_by_id("add-to-cart-button")

