
from behave import given, when, then



@given('Open target main page')
def open_main(context):
    # context.driver.get('https://www.target.com/')
    context.app.main_page.open_main()

@given('Open target Circle page')
def open_taget_circle(context):
    context.driver.get('https://www.target.com/circle')

@when('Open Cart page')
def open_taget_cart_page(context):
    context.driver.get('https://www.target.com/cart')