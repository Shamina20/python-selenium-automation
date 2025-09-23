from selenium.webdriver.common.by import By
from pages.base_page import Page



class SignInPage(Page):
    SEARCH_RESULTS_SIGNIN_TXT = (By.CSS_SELECTOR, 'h1[class*="styles_ndsHeading"]')
    def verify_signin_msg(self,text):
        self.verify_text(text, *self.SEARCH_RESULTS_SIGNIN_TXT)
