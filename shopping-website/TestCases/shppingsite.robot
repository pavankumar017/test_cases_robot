
*** Settings ***
Library  SeleniumLibrary
Library   ../utils.py
Library  ../shopping.py

Resource  ../Resources/shopping_keyword.robot

Suite Setup  Open Browser "https://www.saucedemo.com/"
# Suite Teardown  Close Browser


***Test Cases***
User to verfiy login with invalid User name
    Given user is on login page
    When user enters username invalid
    When user enters pwd valid
    And user clicks on login-btn 
    Then user should see error message "Epic sadface: Username and password do not match any user in this service"

User to verify successfull login 
    Given user is on login page
    When user enters username valid
    When user enters pwd valid
    And user clicks on login-btn 
    Then user should be successfully logged in 
