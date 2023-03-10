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
    def test_a_login_success(self):
        driver = self.browser
        #access url
        driver.get(str(dataTest.base_url))
        driver.maximize_window()
        #access register page
        driver.find_element(By.XPATH, LocatorXPath.login).click()
        self.assertEqual(driver.current_url,str(dataTest.base_url+"/login"))
        #fill form
        driver.find_element(By.XPATH, LocatorXPath.email).send_keys(dataTest.static_email)
        driver.find_element(By.XPATH, LocatorXPath.password).send_keys(dataTest.correct_password)
        driver.find_element(By.XPATH, LocatorXPath.button_login).click()
        #respon success
        
        
        
    def tearDown(self):
        self.browser.close()
        
if __name__ == '__main__':
    unittest.main()