from selenium.webdriver.common.by import By

from pages.base_page import Page


class TargetAppPage(Page):
    TC_Link = (By.CSS_SELECTOR, "a[aria-label*='terms & conditions']")
    def open_signin_page(self):
        self.open_url('https://www.target.com/orders?lnk=acct_nav_my_account')

    def click_tc_link(self):
        self.click(*self.TC_Link)