from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartPage(Page):
    SEARCH_RESULTS_CART_TXT = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')
    def verify_cart_empty_msg(self,msg):
        actual_text = self.driver.find_element(*self.SEARCH_RESULTS_CART_TXT).text
        assert actual_text == msg, f'{actual_text}'