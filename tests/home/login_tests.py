from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_t1invalidLogin(self):
        self.lp.login("alexbichevoy211@gmail.com", "KseniBi2111")
        result = self.lp.verifyLoginFailed()
        assert result == True
        self.driver.refresh()

    @pytest.mark.run(order=2)
    def test_t2validLogin(self):
        self.lp.login("alexbichevoy211@gmail.com", "KseniBi211")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title Verification")
        result2 = self.lp.verifyLoginSuccessful()
        print("Result1: " + str(result1))
        print("Result2: " + str(result2))
        self.ts.markFinal("test_validLogin", result2, "Login Verification")






