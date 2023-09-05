
*** Settings ***

*** Keywords ***
Open Browser "${URL}"
    utils.open_browser  ${URL}

Close Browser
    utils.close_browser


user is on login page
    shopping.verify_login_page

user enters username ${user_name}
    shopping.enter_user_name  ${user_name}

user enters pwd valid
    shopping.enter_pwd

user clicks on ${click_var}
    shopping.click_on  ${click_var}

user should see error message "${err_msg}"
    shopping.verify_error_message  ${err_msg}

user should be successfully logged in 
    shopping.verify_login

User selects the product with Price "${price}"
    shopping.select_the_product_on_price  ${price}

User verifies the value of cart
    shopping.verify_cart_value