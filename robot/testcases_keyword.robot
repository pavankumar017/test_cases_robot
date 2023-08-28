**Settings**
# Resource  locators.py

**Keywords***

Open Browser "${URL}"
    utils.open_browser  ${URL}

Close Browser
    utils.close_browser

user is on Home page of amazon
    test_cases.user_is_on_home_page_of_amazon


verify the page is displayed in ${txt_english}
    test_cases.verify_the_page_is_displayed_in_english  ${txt_english}


user selects Books from the drop down
    test_cases.user_selects_books_from_the_drop_down

search for the book "${book_name}"
    test_cases.search_book  ${book_name}

User is on amazon searched page.
    test_cases.searched_page

User Selects the most gifted book
    test_cases.selects_most_gfted_book

User adds that book to cart
    test_cases.adds_to_cart
