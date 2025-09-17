from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SIGNIN_BUTTON=(By.CSS_SELECTOR,'[data-test="accountNav-signIn"]')
ADD_TO_CART=(By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCartButton']")

@when('Click on Signin button on navigation menu')
def navi_signin(context):
   context.driver.find_element(*SIGNIN_BUTTON).click()
sleep(5)

@when('Confirm Add to Cart button from navigation menu')
def navi_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART).click()
sleep(5)