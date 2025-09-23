from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartPage(Page):
    SEARCH_RESULTS_CART_TXT = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')
    ADD_TO_CART = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCartButton']")
    TOTAL_TEXT = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")

    def verify_cart_empty_msg(self,msg):
        # actual_text = self.driver.find_element(*self.SEARCH_RESULTS_CART_TXT).text
        # assert actual_text == msg, f'{actual_text}'
        self.verify_text(msg,*self.SEARCH_RESULTS_CART_TXT)

    def navi_add_to_cart_btn(self):
        self.wait_until_clickable_click(*self.ADD_TO_CART)

    def verify_cart_item(self,amount):
        self.verify_text(amount,self.TOTAL_TEXT)