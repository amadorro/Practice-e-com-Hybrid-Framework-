# Goal = search for the lowest-price summer dress
class SearchPrd:
    # locators
    search_box_id = "search_query_top"
    click_search_xpath = "//*[@id='searchbox']/button"
    select_lowest_price_id = "selectProductSort"

    def __init__(self, driver):
        self.driver = driver

    def setSearchPrd(self, product):
        self.driver.find_element_by_id(self.search_box_id).send_keys(product)

    def clickSearch(self):
        self.driver.find_element_by_xpath(self.click_search_xpath).click()

    def setSortProduct(self, price):
        self.driver.find_element_by_id(self.select_lowest_price_id).send_keys(price)




