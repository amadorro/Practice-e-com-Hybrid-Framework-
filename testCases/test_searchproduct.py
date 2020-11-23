''' Sanity: Sanity testing is a kind of
testing performed to check whether a
 software product is working correctly
 when a new module or functionality gets
 implemented to an existing product.

 Regression: Regression testing is the
 verification of “bug fixes or any changes
 in the requirement” and making sure they
 are not affecting other functionalities
 of the application.
 note: to run this, I created pytest.ini file
 '''

from pageObjects.SearchProduct import SearchPrd
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium import webdriver
import pytest
import time


class Test_003_SearchPrd:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_searchPrd(self, setup):
        self.logger.info("***** Test_003_SearchPrd Started ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(5)

        # create a new variable
        self.logger.info("***** Search Product Started ****")
        self.srb = SearchPrd(self.driver)
        self.srb.setSearchPrd("Summer Dress")
        self.srb.clickSearch()

        # Validate title of the page
        self.logger.info("***** Validation Test Started ****")
        act_title = self.driver.title
        if act_title == "Search - My Store":
            self.logger.info("***** Validation Test Passed ****")
            assert True
        else:
            self.driver.save_screenshot("./Screenshots" + "Test_003_SearchPrd.png")
            self.logger.info("***** Validation Test Failed ****")
            assert False

        # sort by lowest price
        self.srb.setSortProduct("Price: Lowest first")
        self.logger.info("***** Test_003_SearchPrd Completed ****")









