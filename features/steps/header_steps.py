from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_ICON=(By.CSS_SELECTOR,'[data-test="@web/CartLink"]')
SIGNIN_ICON=(By.CSS_SELECTOR,'#account-sign-in')


# Click on Cart Icon code here
@when('click on cart icon')
def click_cart(context):
   context.driver.find_element(*CART_ICON).click()
sleep(5)


# Click on SignIn Icon code here
@when('click signin icon')
def click_signin_icon(context):
   context.driver.find_element(*SIGNIN_ICON).click()
sleep(5)