***Settings***
Library  SeleniumLibrary
Library   ../utils.py
Library  ../shopping.py
Library  ../selectors_hub.py


Resource  ../Resources/selectors_hub_keyword.robot
Resource  ../Resources/shopping_keyword.robot

Suite Setup  Open Browser "https://selectorshub.com/xpath-practice-page/"
Suite Teardown  Close Browser

**Test Cases***
Verfy successfully Opened the given link 
    Given User should be in the home page 

User to verify the firstname are not clickable until clicked on action button 
    Given User should be in the home page 
    And Firstname field is not interactable 
    And User click on Edit action SVG icon 
    Then User should be able to interact 

User to test the select class based on input 
    Given User should be in the home page 
    Then User should select dropdown "audi"

# User to scroll down and verify the table contents value change
# #CHANGE VALUSE AND CHECK BODU CONTENTS NUMBER


# User to test action class

# User to check the box with  username joe root

# User to pick todays date

//label[normalize-space()='Can you enter name here through automation']//*[name()='svg']    