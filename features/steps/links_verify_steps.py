from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

HEADER_LINKS=(By.CSS_SELECTOR,"[data-test='@web/slingshot-components/CellsComponent/Link']")

# links and verification code here
@then('verify header 15 links')
def verify_links_count(context):
    links=context.driver.find_elements(*HEADER_LINKS)
    print(f'links{links}')
    print(len(links))
    assert len(links) == 15
