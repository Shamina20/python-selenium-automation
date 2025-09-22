from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SIGNIN_ICON=(By.CSS_SELECTOR,'#account-sign-in')
# SEARCH_FIELD=(By.ID,'search')
# SEARCH_BUTTON=(By.XPATH, '//button[@data-test="@web/Search/SearchButton"]')

# Click on Cart Icon code here
@when('click on cart icon')
def click_cart(context):
   context.app.header.click_cart()


# Click on SignIn Icon code here
@when('click signin icon')
def click_signin_icon(context):
   context.driver.find_element(*SIGNIN_ICON).click()
sleep(5)


#Click on search tab and enter product
@when('Search for {product}')
def search_product(context, product):
    # context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    # context.driver.find_element(*SEARCH_BUTTON).click()
    # sleep(5)
    context.app.header.search_product(product)

