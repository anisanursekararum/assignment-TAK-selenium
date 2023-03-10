import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from assets.locator import LocatorXPath
from assets.data import dataTest

class LoginNegative(unittest.TestCase):

    #setup browser yang dipakai / memanggil driver
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    #maintest 
    def test_a_login_empt_form(self):
        driver = self.browser
        #access url
        driver.get(str(dataTest.base_url))
        driver.maximize_window()
        #access register page
        driver.find_element(By.XPATH, LocatorXPath.login).click()
        self.assertEqual(driver.current_url,str(dataTest.base_url+"/login"))
        #fill form
        driver.find_element(By.XPATH, LocatorXPath.email).send_keys(dataTest.empty_field)
        driver.find_element(By.XPATH, LocatorXPath.password).send_keys(dataTest.empty_field)
        driver.find_element(By.XPATH, LocatorXPath.button_login).click()
        #respon fail
        error_login = driver.find_element(By.XPATH, LocatorXPath.error_login)
        self.assertIn(dataTest.error_login, error_login.get_attribute("innerText"))
        error_not_found = driver.find_element(By.XPATH, LocatorXPath.error_not_found)
        self.assertIn(dataTest.error_not_found, error_not_found.get_attribute("innerText"))
    
    def test_b_login_empt_pass(self):
        driver = self.browser
        #access url
        driver.get(str(dataTest.base_url))
        driver.maximize_window()
        #access register page
        driver.find_element(By.XPATH, LocatorXPath.login).click()
        self.assertEqual(driver.current_url,str(dataTest.base_url+"/login"))
        #fill form
        driver.find_element(By.XPATH, LocatorXPath.email).send_keys(dataTest.static_email)
        driver.find_element(By.XPATH, LocatorXPath.password).send_keys(dataTest.empty_field)
        driver.find_element(By.XPATH, LocatorXPath.button_login).click()
        #respon fail
        error_login = driver.find_element(By.XPATH, LocatorXPath.error_login)
        self.assertIn(dataTest.error_login, error_login.get_attribute("innerText"))
        error_invalid_cred = driver.find_element(By.XPATH, LocatorXPath.error_invalid_cred)
        self.assertIn(dataTest.error_invalid_cred, error_invalid_cred.get_attribute("innerText"))
        
    def test_c_login_invalid_email(self):
        driver = self.browser
        #access url
        driver.get(str(dataTest.base_url))
        driver.maximize_window()
        #access register page
        driver.find_element(By.XPATH, LocatorXPath.login).click()
        self.assertEqual(driver.current_url,str(dataTest.base_url+"/login"))
        #fill form
        driver.find_element(By.XPATH, LocatorXPath.email).send_keys(dataTest.wrong_email_format)
        driver.find_element(By.XPATH, LocatorXPath.password).send_keys(dataTest.correct_password)
        driver.find_element(By.XPATH, LocatorXPath.button_login).click()
        #respon fail
        error_invalid_email = driver.find_element(By.XPATH, LocatorXPath.error_invalid_email)
        self.assertIn(dataTest.error_invalid_email, error_invalid_email.get_attribute("innerText"))

    def tearDown(self):
        self.browser.close()
        
if __name__ == '__main__':
    unittest.main()