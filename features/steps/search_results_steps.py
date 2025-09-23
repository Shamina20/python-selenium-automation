from xml import parsers

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# ADD_TO_CART_ICON=(By.CSS_SELECTOR,"[id*='addToCartButton']")
LISTING=(By.CSS_SELECTOR,"[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE=(By.CSS_SELECTOR,"[data-test='product-title']")
PRODUCT_IMAGE=(By.CSS_SELECTOR,'img')

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
    context.driver.execute_script("window.scrollBy(0, 1000);")
    # context.driver.execute_script("window.scrollBy(0, 2000)", "")
    # sleep(8)
    # context.driver.execute_script("window.scrollBy(0, 1000)", "")
    # element = context.driver.find_element(*ADD_TO_CART_ICON)
    # element.click()
    context.app.search_results_page.click_add_to_cart()

@then('verify product name and images')
def verify_product_name_image(context):
    # context.driver.execute_script("window.scrollBy(0, 2000)", "")
    # sleep(8)
    # context.driver.execute_script("window.scrollBy(0, 1000)", "")

    products = context.driver.find_elements(*LISTING)
    for product in products[:8]:
        title=product.find_element(*PRODUCT_TITLE).text
        assert title, "Product name not found"
        print(f'{title}')
        product.find_element(*PRODUCT_IMAGE)



