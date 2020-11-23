

class LoginPage:
    email_txtbox_id = "email"
    password_txtbox_id = "passwd"
    submit_box_id = "SubmitLogin"
    click_signin_xpath = "//*[@id='SubmitLogin']"
    signout_button_xpath = "//*[@id='header']/div[2]/div/div/nav/div[2]/a"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element_by_id(self.email_txtbox_id).clear()
        self.driver.find_element_by_id(self.email_txtbox_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.password_txtbox_id).clear()
        self.driver.find_element_by_id(self.password_txtbox_id).send_keys(password)

    def clickSign(self):
        self.driver.find_element_by_xpath(self.click_signin_xpath).click()

    def clickSignout(self):
        self.driver.find_element_by_xpath(self.signout_button_xpath).click()




