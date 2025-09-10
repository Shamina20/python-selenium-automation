from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SIGNIN_BUTTON=(By.CSS_SELECTOR,'[data-test="accountNav-signIn"]')

@when('Click on Signin button on navigation menu')
def click_signin_navigation(context):
   context.driver.find_element(*SIGNIN_BUTTON).click()
sleep(5)