
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.CreateAccountPage import createAccount
import pytest
import string
import time

class Test_002_Login:
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_loginPage(self, setup):
        self.logger.info("***** Test_002_Login Test Started *****")
        self.driver = setup
        time.sleep(5)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(5)

        # create variable
        self.cap = createAccount(self.driver)
        self.cap.clickSignin()

        # create new variable
        time.sleep(10)
        self.lp = LoginPage(self.driver)
        time.sleep(7)
        self.lp.setEmail(self.email)
        time.sleep(7)
        self.lp.setPassword(self.password)
        time.sleep(7)
        self.lp.clickSign()
        self.logger.info("***** Login Success *****")

        # validate
        time.sleep(10)
        self.logger.info("***** Title Page Validation Started *****")
        act_title = self.driver.title
        if act_title == "My account - My Store":
            assert True
            self.logger.info("***** Title Page Validation Passed *****")
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_loginPage.png")
            self.logger.error("***** Title Page Validation Failed *****")
            assert False

        # click Sign-out
        time.sleep(10)
        self.lp.clickSignout()
        self.logger.info("***** Test_002_Login Test Completed *****")


