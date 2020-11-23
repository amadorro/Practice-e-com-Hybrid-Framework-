from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.CreateAccountPage import createAccount
from utilities import ExcelUtils
import pytest
import string
import time

class Test_003_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    # include the path variable
    path = "./TestData/" + "data.xlsx"
    logger = LogGen.loggen()

    def test_loginPage_ddt(self, setup):
        self.logger.info("***** Test_003_DDT_Login Started *****")
        self.driver = setup
        time.sleep(5)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(5)

        # create variable
        self.cap = createAccount(self.driver)
        self.cap.clickSignin()

        # create new variable
        time.sleep(5)
        self.lp = LoginPage(self.driver)

        # read data from excel file
        self.rows = ExcelUtils.getRowCount(self.path,"Sheet1")

        # empty list variable for exp values
        lst_status = []
        time.sleep(5)
        print('Number of Rows:', self.rows)
        for row in range(2,self.rows + 1):
            # read email(column 1)
            self.email = ExcelUtils.readData(self.path,'Sheet1',row,1)
            # read password(column 2)
            self.password = ExcelUtils.readData(self.path,'Sheet1',row,2)
            # read exp(column 3)
            self.exp = ExcelUtils.readData(self.path,'Sheet1',row,3)

            # Get the email and password from excel
            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickSign()
            self.logger.info("***** Login Success *****")
            time.sleep(5)

            # validate title of the page
            act_title = self.driver.title
            exp_title = "My account - My Store"
            if exp_title == act_title:
                # validate exp value from excel
                if self.exp == 'Pass':
                    self.logger.info("***** Login Passed *****")
                    self.lp.clickSignout();
                    lst_status.append('Pass')
                elif self.exp == 'Fail':
                    self.logger.error("***** Failed *****")
                    self.lp.clickSignout();
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.error("***** Login Failed *****")
                    lst_status.append('Failed')
                elif self.exp == 'Fail':
                    self.logger.info("***** Passed *****")
                    lst_status.append("Pass")

    # for failed exp values
        if "Fail" not in lst_status:
            self.logger.info("***** Login Passed *****")
            self.driver.close()
            assert True
        else:
            self.logger.error("***** Login Failed *****")
            self.driver.close()
            assert False

        self.logger.info("***** Test_003_DDT_Login Completed *****")








