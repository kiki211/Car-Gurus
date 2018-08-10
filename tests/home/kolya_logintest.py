from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time


#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome()
driver.get("https://www.cargurus.com/")
signin = driver.find_element_by_class_name("ft-auth-sign-in")
account_panel = driver.find_element_by_class_name("ft-user-name")

hover = ActionChains(driver).move_to_element(account_panel)
time.sleep(5)
hover.perform()
time.sleep(1)
signin.click()
time.sleep(1)

email_field = driver.find_element_by_id("registerEmail")
register_button = driver.find_element_by_id("registerButton")
email_field.send_keys("nshegai@mail.ru")

register_button.click()
time.sleep(1)

pass_field = driver.find_element_by_id("loginPassword")
signin_button = driver.find_element_by_id("loginButton")
pass_field.send_keys("rtetrt")

signin_button.click()
time.sleep(1)