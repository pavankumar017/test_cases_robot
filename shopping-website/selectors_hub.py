import utils as util
from utils import  get_constant_data, get_element
from robot.api import logger
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium import webdriver



def homepage():
    title  = util.driver.title
    assert "Xpath Practice Page | Shadow dom, nested shadow dom, iframe, nested iframe and more complex automation scenarios."  == title

def field_notinteract():
    is_enabled = util.driver.find_element_by_xpath(get_element("locators.selectors_hub.first_name")).is_enabled()
    logger.console(is_enabled)
    assert is_enabled == False


def click_on_edit():
    util.driver.find_element_by_xpath(get_element("locators.selectors_hub.edit_action")).click()

def field_interaact():
    is_enabled = util.driver.find_element_by_xpath(get_element("locators.selectors_hub.first_name")).is_enabled()
    logger.console(is_enabled)
    assert is_enabled == True

def select_a_dropdwon(drop_down_value):
    select = Select(util.driver.find_element_by_id("cars"))
    select.select_by_value(drop_down_value)
    
def hoover_on_checkout():
    act = ActionChains(util.driver)
    element = util.driver.find_element_by_xpath("//button[contains(text(),'Checkout here')]")
    act.move_to_element(element).perform()

def dropdwon_verify():
    is_dropdown_visible = util.driver.find_element_by_xpath(get_element("locators.selectors_hub.drop_down_visible")).is_displayed()

    assert is_dropdown_visible == True