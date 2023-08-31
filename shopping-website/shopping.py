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


def verify_login_page():
    title_current = util.driver.title
    
    assert "Swag Labs" == title_current


def enter_user_name(usr_name):
    """enter user name"""
    util.driver.refresh()
    if usr_name == "invalid" :
        util.driver.find_element_by_id(get_element("locators.login.username")).send_keys(get_constant_data("data.invalid_username"))
    
    else:
        util.driver.find_element_by_id(get_element("locators.login.username")).send_keys(get_constant_data("data.valid_username"))

def enter_pwd():
    util.driver.find_element_by_id(get_element("locators.login.pwd")).send_keys(get_constant_data("data.valid_pwd"))

def click_on(element):
    util.driver.find_element_by_css_selector(get_element("locators.login."+ element)).click()

def verify_error_message(error_msg):
    WebDriverWait(util.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR , get_element("locators.login.error_msg"))))
    current_error_msg = util.driver.find_element_by_css_selector(get_element("locators.login.error_msg")).text

    assert error_msg == current_error_msg


def verify_login():
    WebDriverWait(util.driver, 10).until(EC.visibility_of_element_located((By.XPATH , get_element("locators.login.login_page") )))

    is_ele_present = util.driver.find_element_by_xpath(get_element("locators.login.login_page")).is_displayed()

    assert is_ele_present == True