from xml import parsers

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

ADD_TO_CART_ICON=(By.CSS_SELECTOR,"[id*='addToCartButton']")
# After Seacrh the product , click on add to cart button code here
@when('Click on Add to cart icon')
def click_add_to_cart(context):
    # WebDriverWait(context.driver, 10).until(
    #     EC.element_to_be_clickable(ADD_TO_CART_ICON)
    # ).click()

   # context.driver.find_element(*ADD_TO_CART_ICON).click()

    # element = context.driver.find_element(*ADD_TO_CART_ICON)
    # context.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    # element.click()

    sleep(5)
    context.driver.execute_script("window.scrollBy(0, 500);")
    element = context.driver.find_element(*ADD_TO_CART_ICON)
    element.click()