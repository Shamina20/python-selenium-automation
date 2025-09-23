from selenium.webdriver.common.by import By
from behave import given, when, then
# from time import sleep


# SEARCH_RESULTS_SIGNIN_TXT=(By.CSS_SELECTOR,'h1[class*="styles_ndsHeading"]')
# SEARCH_RESULTS_PRODUCT_TXT=(By.XPATH,"//div[@data-test='lp-resultsCount']")
# TOTAL_TEXT=(By.XPATH,"//div[./span[contains(text(), 'subtotal')]]")

# Cart Page verification code here
@then('Verify {msg} message is shown')
def verify_search(context,msg):
    context.app.cart_page.verify_cart_empty_msg(msg)


# SignIn Page verification code here
@then('Verify {text} form opened')
def verify_search(context,text):
    # actual_text=context.driver.find_element(*SEARCH_RESULTS_SIGNIN_TXT).text
    # assert actual_text == text, f'{actual_text}'
    # print(actual_text)
    context.app.sign_in_page.verify_signin_msg(text)


#search Product and verify code here
@then('Verify search results are shown for {product}')
def verify_search(context, product):
    # actual_text_product = context.driver.find_element(SEARCH_RESULTS_PRODUCT_TXT).text
    # assert product in actual_text_product
    context.app.search_results_page.verify_search_results(product)
    context.app.search_results_page.verify_product_url(product)

# verify cart has 1 item
@then('verify cart has {amount} item(s)')
def verify_cart_item(context, amount):
    # cart_summary = context.driver.find_element(TOTAL_TEXT).text
    # assert f'{cart_summary} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"
    context.app.cart_page.verify_cart_item(amount)

