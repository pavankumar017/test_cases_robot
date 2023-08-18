import utils as util
from robot.api import logger


def user_is_on_home_page_of_amazon():
    """Verify that user is on home page of amazon"""
    util.driver.find_element_by_id("nav-logo")


def verify_the_page_is_displayed_in_english():
    """verfy english language is displayed"""
    lang = util.driver.find_element_by_xpath("//span[@class='nav-line-2']//div").text
    logger.console(lang)
    assert(lang == "EN")