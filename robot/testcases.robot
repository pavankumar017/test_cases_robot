**Settings***
Library  SeleniumLibrary
Library  test_cases.py
Library  utils.py


Resource  testcases_keyword.robot
Resource  locators.robot

Suite Setup  Open Browser "https://www.amazon.in/"
# Suite Teardown  Close Browser

*** Test Cases ***
User to verify opening the amazon website and check it its on english
    Given user is on Home page of amazon
    Then verify the page is displayed in ${txt_english}


User to select book from drop down and search for "The Alchemist"
    Given user is on Home page of amazon
    When user selects Books from the drop down
    Then search for the book "The Alchemist"

User to add the searched book to cart and verify
    Given User is on amazon searched page.
    And User Selects the most gifted book 
    And User adds that book to cart

