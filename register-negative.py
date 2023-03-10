import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from assets.locator import LocatorXPath
from assets.data import dataTest

class RegisterNegative(unittest.TestCase):

    #setup browser yang dipakai / memanggil driver
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    #maintest 
    def test_a_register_empt_form(self):
        driver = self.browser
        #access url
        driver.get(str(dataTest.base_url))
        driver.maximize_window()
        #access register page
        driver.find_element(By.XPATH, LocatorXPath.register).click()
        self.assertEqual(driver.current_url,str(dataTest.base_url+"/register"))
        #empty form
        driver.find_element(By.XPATH, LocatorXPath.firstname).send_keys(dataTest.empty_field)
        driver.find_element(By.XPATH, LocatorXPath.lastname).send_keys(dataTest.empty_field)
        driver.find_element(By.XPATH, LocatorXPath.email).send_keys(dataTest.empty_field)
        driver.find_element(By.XPATH, LocatorXPath.password).send_keys(dataTest.empty_field)
        driver.find_element(By.XPATH, LocatorXPath.confirm_password).send_keys(dataTest.empty_field)
        driver.find_element(By.XPATH, LocatorXPath.button_register).click()
        #respon validation
        validation_firstname = driver.find_element(By.XPATH, LocatorXPath.validation_firstname)
        self.assertIn(dataTest.validation_firstname, validation_firstname.get_attribute("innerText"))
        validation_lastname = driver.find_element(By.XPATH, LocatorXPath.validation_lastname)
        self.assertIn(dataTest.validation_lastname, validation_lastname.get_attribute("innerText"))
        validation_email = driver.find_element(By.XPATH, LocatorXPath.validation_email)
        self.assertIn(dataTest.validation_email, validation_email.get_attribute("innerText"))
        validation_password = driver.find_element(By.XPATH, LocatorXPath.validation_password)
        self.assertIn(dataTest.validation_password, validation_password.get_attribute("innerText"))
        validation_confirm_password = driver.find_element(By.XPATH, LocatorXPath.validation_confirm_password)
        self.assertIn(dataTest.validation_password, validation_confirm_password.get_attribute("innerText"))

    def test_b_register_invalid_email(self):
        driver = self.browser
        #access url
        driver.get(str(dataTest.base_url))
        driver.maximize_window()
        #access register page
        driver.find_element(By.XPATH, LocatorXPath.register).click()
        self.assertEqual(driver.current_url,str(dataTest.base_url+"/register"))
        #invalid email
        driver.find_element(By.XPATH, LocatorXPath.radio_button_female).click()
        driver.find_element(By.XPATH, LocatorXPath.firstname).send_keys(dataTest.firstname)
        driver.find_element(By.XPATH, LocatorXPath.lastname).send_keys(dataTest.lastname)
        driver.find_element(By.XPATH, LocatorXPath.email).send_keys(dataTest.wrong_email_format)
        driver.find_element(By.XPATH, LocatorXPath.password).send_keys(dataTest.correct_password)
        driver.find_element(By.XPATH, LocatorXPath.confirm_password).send_keys(dataTest.correct_password)
        driver.find_element(By.XPATH, LocatorXPath.button_register).click()
        #respon validation
        validation_email = driver.find_element(By.XPATH, LocatorXPath.validation_email)
        self.assertIn(dataTest.validation_format_email, validation_email.get_attribute("innerText"))

    def test_c_register_pass_less_than6(self):
        driver = self.browser
        #access url
        driver.get(str(dataTest.base_url))
        driver.maximize_window()
        #access register page
        driver.find_element(By.XPATH, LocatorXPath.register).click()
        self.assertEqual(driver.current_url,str(dataTest.base_url+"/register"))
        #invalid email
        driver.find_element(By.XPATH, LocatorXPath.radio_button_female).click()
        driver.find_element(By.XPATH, LocatorXPath.firstname).send_keys(dataTest.firstname)
        driver.find_element(By.XPATH, LocatorXPath.lastname).send_keys(dataTest.lastname)
        driver.find_element(By.XPATH, LocatorXPath.email).send_keys(dataTest.email)
        driver.find_element(By.XPATH, LocatorXPath.password).send_keys(dataTest.less_char_password)
        driver.find_element(By.XPATH, LocatorXPath.confirm_password).send_keys(dataTest.less_char_password)
        driver.find_element(By.XPATH, LocatorXPath.button_register).click()
        #respon validation
        validation_password = driver.find_element(By.XPATH, LocatorXPath.validation_password)
        self.assertIn(dataTest.validation_char_password, validation_password.get_attribute("innerText"))

    def test_d_register_pass_mismatc(self):
        driver = self.browser
        #access url
        driver.get(str(dataTest.base_url))
        driver.maximize_window()
        #access register page
        driver.find_element(By.XPATH, LocatorXPath.register).click()
        self.assertEqual(driver.current_url,str(dataTest.base_url+"/register"))
        #invalid email
        driver.find_element(By.XPATH, LocatorXPath.radio_button_female).click()
        driver.find_element(By.XPATH, LocatorXPath.firstname).send_keys(dataTest.firstname)
        driver.find_element(By.XPATH, LocatorXPath.lastname).send_keys(dataTest.lastname)
        driver.find_element(By.XPATH, LocatorXPath.email).send_keys(dataTest.email)
        driver.find_element(By.XPATH, LocatorXPath.password).send_keys(dataTest.correct_password)
        driver.find_element(By.XPATH, LocatorXPath.confirm_password).send_keys(dataTest.wrong_password)
        driver.find_element(By.XPATH, LocatorXPath.button_register).click()
        #respon validation
        validation_confirm_password = driver.find_element(By.XPATH, LocatorXPath.validation_confirm_password)
        self.assertIn(dataTest.validation_mismatch_password, validation_confirm_password.get_attribute("innerText"))
    
    def test_e_register_email_exist(self):
        driver = self.browser
        #access url
        driver.get(str(dataTest.base_url))
        driver.maximize_window()
        #access register page
        driver.find_element(By.XPATH, LocatorXPath.register).click()
        self.assertEqual(driver.current_url,str(dataTest.base_url+"/register"))
        #invalid email
        driver.find_element(By.XPATH, LocatorXPath.radio_button_female).click()
        driver.find_element(By.XPATH, LocatorXPath.firstname).send_keys(dataTest.firstname)
        driver.find_element(By.XPATH, LocatorXPath.lastname).send_keys(dataTest.lastname)
        driver.find_element(By.XPATH, LocatorXPath.email).send_keys(dataTest.static_email)
        driver.find_element(By.XPATH, LocatorXPath.password).send_keys(dataTest.correct_password)
        driver.find_element(By.XPATH, LocatorXPath.confirm_password).send_keys(dataTest.correct_password)
        driver.find_element(By.XPATH, LocatorXPath.button_register).click()
        #respon validation
        validation_email_exist = driver.find_element(By.XPATH, LocatorXPath.validation_email_exist)
        self.assertIn(dataTest.validation_email_exist, validation_email_exist.get_attribute("innerText"))

    def tearDown(self):
        self.browser.close()

if __name__ == '__main__':
    unittest.main()