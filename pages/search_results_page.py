from pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResultsPage(Page):
    SEARCH_RESULTS_PRODUCT_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    def verify_search_results(self,product):
        actual_text_product = self.find_element(*self.SEARCH_RESULTS_PRODUCT_TXT).text
        assert product in actual_text_product, f'Error. Expected text {product} but got {actual_text_product}'