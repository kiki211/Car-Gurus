"""
@package base

WebDriver Factory class implementation
It creates a webrdiver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
             None
        """

        self.browser = browser
    """
    Set Chrome driver ieexplorer environment based on OS
    
    chromedriver = "C:/.../chromedriver.exe"
    os.version["webdriver.chrome.driver"]= chromedriver
    se
    PREFERRED: Set the path on the machine where will be executed 
    lf.driver = webdriver.Chrome(chromedriver)
    
    """


    def getWebDriverInstance(self):
        """
        get WebDriver based on the browser configuration

        Returns:
            'WEbdriver Instance'
        """

        baseURL = "https://www.cargurus.com/"

        if self.browser == 'safari':
            driver = webdriver.Safari()
        elif self.browser == 'chrome':
            driver = webdriver.Chrome()
        elif self.browser == 'firefox':
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Firefox()
        # Setting Drive Implicit Time out for An Element
        driver.implicitly_wait(5)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver