
from pageObjects.CreateAccountPage import createAccount
import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_CreateAccount:
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_createAccount(self, setup):
        self.logger.info("***** Test_001_CreateAccount Started *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.pi = createAccount(self.driver)
        self.pi.clickSignin()
        self.logger.info("***** Completing the form Started *****")

        # validate title of the page
        act_title = self.driver.title
        time.sleep(10)
        if act_title == "Login - My Store":
            assert True
            self.logger.info("***** Title of the Page Passed *****")
        else:
            self.logger.error("***** Invalid Title of the Page *****")
            self.driver.save_screenshot("./Screenshots/" + "test_createAccount.png")
            assert False

        time.sleep(5)
        self.pi.setAccount(self.email)
        self.pi.clickEmail()
        time.sleep(5)
        self.pi.clickTitle()
        self.pi.setFirstName('Amador')
        self.pi.setLastname("Rodriguez")
        self.pi.setEmail(self.email)
        time.sleep(5)
        self.pi.setPassword(self.password)

        # Set day of birth
        time.sleep(10)
        self.pi.setDayOfBirth("6")
        time.sleep(10)
        self.pi.setMonthOfBirth("June")
        time.sleep(10)
        self.pi.setYearOfBirth("1995")

        self.pi.clickNewsletter()
        self.pi.setFstName("Amador")
        self.pi.setLstName("Rodriguez")
        self.pi.setCompany("New Stand")
        self.pi.setAddress("10089 Coco St")
        self.pi.setCity("Bell")
        time.sleep(10)
        self.pi.setState("California")
        self.pi.setZipcode("90228")
        self.pi.setCountry("United States")
        time.sleep(5)
        self.pi.setCellPhone("323 890-7700")
        self.pi.setAliasAddress("My address")
        self.pi.clickRegister()
        self.logger.info("***** Form Completed *****")
        self.logger.info("***** Test_001_CreateAccount Completed *****")









