from selenium.webdriver.support.ui import Select
import time

class createAccount:
    signin_button_xpath = "//*[@id='header']/div[2]/div/div/nav/div[1]/a"
    create_account_txt_id = "email_create"
    create_account_button_id = "SubmitCreate"
    radio_button_id = "id_gender1"
    firstname_txtbox_id = "customer_firstname"
    lastname_txtbox_id = "customer_lastname"
    email_txtbox_id = "email"
    password_txtbox_id = "passwd"
    days_bthday_id = "days"
    months_bthday_id = "months"
    years_bthday_id = "years"
    new_letter_id = "newsletter"
    firstname2_id = "firstname"
    lastname2_id = "lastname"
    company_name_id = "company"
    address_id = "address1"
    city_id = "city"
    state_drpbox_id = "id_state"
    zip_code_id = "postcode"
    country_drpbox_id = "id_country"
    cell_phone_id = "phone_mobile"
    address_alias_id = "alias"
    register_button_id = "submitAccount"

    def __init__(self, driver):
        self.driver = driver

    def clickSignin(self):
        self.driver.find_element_by_xpath(self.signin_button_xpath).click()

    def setAccount(self, account):
        self.driver.find_element_by_id(self.create_account_txt_id).clear()
        self.driver.find_element_by_id(self.create_account_txt_id).send_keys(account)

    def clickEmail(self):
        self.driver.find_element_by_id(self.create_account_button_id).click()

    def clickTitle(self):
        self.driver.find_element_by_id(self.radio_button_id).click()


    def setFirstName(self, fname):
        self.driver.find_element_by_id(self.firstname_txtbox_id).clear()
        self.driver.find_element_by_id(self.firstname_txtbox_id).send_keys(fname)

    def setLastname(self, lname):
        self.driver.find_element_by_id(self.lastname_txtbox_id).clear()
        self.driver.find_element_by_id(self.lastname_txtbox_id).send_keys(lname)

    def setEmail(self, email):
        self.driver.find_element_by_id(self.email_txtbox_id).clear()
        self.driver.find_element_by_id(self.email_txtbox_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.password_txtbox_id).clear()
        self.driver.find_element_by_id(self.password_txtbox_id).send_keys(password)

    def setDayOfBirth(self, day):
        time.sleep(3)
        self.driver.find_element_by_id(self.days_bthday_id).send_keys(day)

    def setMonthOfBirth(self, month):
        time.sleep(3)
        self.driver.find_element_by_id(self.months_bthday_id).send_keys(month)

    def setYearOfBirth(self, year):
        time.sleep(3)
        self.driver.find_element_by_id(self.years_bthday_id).send_keys(year)

    def clickNewsletter(self):
        self.driver.find_element_by_id(self.new_letter_id).click()

    def setFstName(self, fstname):
        self.driver.find_element_by_id(self.firstname2_id).clear()
        self.driver.find_element_by_id(self.firstname2_id).send_keys(fstname)

    def setLstName(self, lstname):
        self.driver.find_element_by_id(self.lastname2_id).clear()
        self.driver.find_element_by_id(self.lastname2_id).send_keys(lstname)

    def setCompany(self, company):
        self.driver.find_element_by_id(self.company_name_id).clear()
        self.driver.find_element_by_id(self.company_name_id).send_keys(company)

    def setAddress(self, address):
        self.driver.find_element_by_id(self.address_id).clear()
        self.driver.find_element_by_id(self.address_id).send_keys(address)

    def setCity(self, city):
        self.driver.find_element_by_id(self.city_id).clear()
        self.driver.find_element_by_id(self.city_id).send_keys(city)

    def setState(self, state):
        self.driver.find_element_by_id(self.state_drpbox_id).send_keys(state)


    def setZipcode(self, zipcode):
        self.driver.find_element_by_id(self.zip_code_id).send_keys(zipcode)

    def setCountry(self, country):
        element = self.driver.find_element_by_id(self.country_drpbox_id)
        drp = Select(element)

    def setCellPhone(self, phone):
        self.driver.find_element_by_id(self.cell_phone_id).send_keys(phone)

    def setAliasAddress(self, alias):
        self.driver.find_element_by_id(self.address_alias_id).clear()
        self.driver.find_element_by_id(self.address_alias_id).send_keys(alias)

    def clickRegister(self):
        self.driver.find_element_by_id(self.register_button_id).click()


