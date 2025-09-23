from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class Header(Page):
    CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartLink"]')
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BUTTON = (By.XPATH, '//button[@data-test="@web/Search/SearchButton"]')
    SIGNIN_ICON = (By.CSS_SELECTOR, '#account-sign-in')
    SIGNIN_BUTTON = (By.CSS_SELECTOR, '[data-test="accountNav-signIn"]')

    def search_product(self,product):
        self.input_text(product,*self.SEARCH_FIELD)
        self.click(*self.SEARCH_BUTTON)
        sleep(5)

    def click_cart(self):
        self.wait_until_clickable_click(*self.CART_ICON)

    def click_sign_in(self):
        self.wait_until_clickable_click(*self.SIGNIN_ICON)
    def click_sign_in_button(self):
        self.wait_until_clickable_click(*self.SIGNIN_BUTTON)