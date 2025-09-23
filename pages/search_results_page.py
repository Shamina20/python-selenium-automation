from pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResultsPage(Page):
    SEARCH_RESULTS_PRODUCT_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    ADD_TO_CART_ICON = (By.CSS_SELECTOR, "[id*='addToCartButton']")

    def verify_search_results(self,product):
        # actual_text_product = self.find_element(*self.SEARCH_RESULTS_PRODUCT_TXT).text
        # assert product in actual_text_product, f'Error. Expected text {product} but got {actual_text_product}'
        self.verify_partial_text(product,*self.SEARCH_RESULTS_PRODUCT_TXT)

    def verify_product_url(self, product):
        # self.verify_url(f'https://www.target.com/s?searchTerm={product}')
            self.verify_partial_url(f'searchTerm={product}')

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART_ICON)