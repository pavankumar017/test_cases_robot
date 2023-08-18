**Settings***
Library  SeleniumLibrary
Library  test_cases.py
Library  utils.py
Library  locators.py

Resource  testcases_keyword.robot

Suite Setup  Open Browser "https://www.amazon.in/"
Suite Teardown  Close Browser

*** Test Cases ***
User to verify opening the amazon website and check it its on english
    Given user is on Home page of amazon
    Then verify the page is displayed in english


