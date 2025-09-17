from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')

@given('Open target Circle page')
def open_taget_circle(context):
    context.driver.get('https://www.target.com/circle')

@when('Open Cart page')
def open_taget_cart_page(context):
    context.driver.get('https://www.target.com/cart')