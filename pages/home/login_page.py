from selenium.webdriver.common.by import By
#from base.selenium_driver import SeleniumDriver
import time
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    _login_Menu = "ft-user-name"
    _login_Link = "ft-auth-sign-in"
    _email_Field = "registerEmail"
    _next_Button = "registerButton"
    _password_Field = "loginPassword"
    _signin_Button = "loginButton"

    # Locating elements methods with inserting locators above
    # def getLoginMenu(self):
    #         return self.driver.find_element(By.XPATH, self._login_Menu)
    #
    # def getLoginLink(self):
    #     return self.driver.find_element(By.LINK_TEXT, self._login_Link)
    #
    # def getEmailField(self):
    #     return self.driver.find_element(By.ID, self._email_Field)
    #
    # def getNextButton(self):
    #     return self.driver.find_element(By.ID, self._next_Button)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.ID, self._password_Field)
    #
    # def getSigninButton(self):
    #     return self.driver.find_element_by_id(self._signin_Button)

    #Action methods
    def clickLoginMenu(self):
        self.elementClick(self._login_Menu, locatorType="class")

    def clickLoginLink(self):
        self.elementClick(self._login_Link, locatorType="class")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_Field)

    def clickNextButton(self):
        self.elementClick(self._next_Button, locatorType="id")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_Field)

    def clickSigninButton(self):
        self.elementClick(self._signin_Button, locatorType="id")


   #_Functionality. It wraps all the actions________________________________________________________________________________

    def login(self, email="", password=""):
        self.clickLoginMenu()
        self.clickLoginLink()
        self.enterEmail(email)
        time.sleep(1)
        self.clickNextButton()
        self.enterPassword(password)
        time.sleep(1)
        self.clickSigninButton()
        time.sleep(2)

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("ft-user-name", locatorType="class")

        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("errorMessageBox", locatorType="id")

        return result

    def verifyLoginTitle(self):
        if "Incorrect password" in self.getTitle():
            return self.verifyPageTitle("Lala")

