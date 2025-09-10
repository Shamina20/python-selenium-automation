from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_RESULTS_CART_TXT=(By.CSS_SELECTOR,'[data-test="boxEmptyMsg"]')
SEARCH_RESULTS_SIGNIN_TXT=(By.CSS_SELECTOR,'h1[class*="styles_ndsHeading"]')

# Cart Page verification code here
@then('Verify {word} message is shown')
def verify_search(context,word):
    actual_text=context.driver.find_element(*SEARCH_RESULTS_CART_TXT).text
    assert actual_text == word, f'{actual_text}'


# SignIn Page verification code here
@then('Verify {text} form opened')
def verify_search(context,text):
    actual_text=context.driver.find_element(*SEARCH_RESULTS_SIGNIN_TXT).text
    assert actual_text == text, f'{actual_text}'
    print(actual_text)