import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from assets.locator import LocatorXPath
from assets.data import dataTest

class RegisterPositive(unittest.TestCase):

    #setup browser yang dipakai / memanggil driver
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    #maintest 
    def test_a_register_success(self):
        driver = self.browser
        #access url
        driver.get(str(dataTest.base_url))
        driver.maximize_window()
        #access register page
        driver.find_element(By.XPATH, LocatorXPath.register).click()
        self.assertEqual(driver.current_url,str(dataTest.base_url+"/register"))
        #fill form
        driver.find_element(By.XPATH, LocatorXPath.radio_button_female).click()
        driver.find_element(By.XPATH, LocatorXPath.firstname).send_keys(dataTest.firstname)
        driver.find_element(By.XPATH, LocatorXPath.lastname).send_keys(dataTest.lastname)
        driver.find_element(By.XPATH, LocatorXPath.email).send_keys(dataTest.email)
        driver.find_element(By.XPATH, LocatorXPath.password).send_keys(dataTest.correct_password)
        driver.find_element(By.XPATH, LocatorXPath.confirm_password).send_keys(dataTest.correct_password)
        driver.find_element(By.XPATH, LocatorXPath.button_register).click()
        #respon success
        self.assertEqual(driver.current_url,str(dataTest.base_url+"/registerresult/1"))
        driver.find_element(By.XPATH, LocatorXPath.success_register).text
        driver.find_element(By.XPATH, LocatorXPath.button_continue).click()
        driver.find_element(By.XPATH, LocatorXPath.button_logout).click()
        print("Register email "+dataTest.email+" berhasil")
        
    def tearDown(self):
        self.browser.close()
        
if __name__ == '__main__':
    unittest.main()