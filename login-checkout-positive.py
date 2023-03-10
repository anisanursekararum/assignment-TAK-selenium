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
    def test_a_login_success_and_checkout(self):
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
        success_login = driver.find_element(By.XPATH, LocatorXPath.success_login)
        self.assertIn(dataTest.static_email, success_login.get_attribute("innerText"))        
        #product detail
        driver.find_element(By.XPATH, LocatorXPath.product_detail).click()
        detail = driver.find_element(By.XPATH, LocatorXPath.detail)
        self.assertIn(dataTest.gift, detail.get_attribute("innerText"))
        self.assertEqual(driver.current_url,str(dataTest.base_url+"/25-virtual-gift-card"))
        #add to cart
        driver.find_element(By.XPATH, LocatorXPath.recipient_name).send_keys(dataTest.recipient_name)
        driver.find_element(By.XPATH, LocatorXPath.recipient_email).send_keys(dataTest.static_email)
        driver.find_element(By.XPATH, LocatorXPath.qty).clear()
        driver.find_element(By.XPATH, LocatorXPath.qty).send_keys(dataTest.qty)
        driver.find_element(By.XPATH, LocatorXPath.button_cart).click()
        #respon success add to cart
        driver.find_element(By.ID, 'bar-notification')
        #check cart
        driver.find_element(By.XPATH, LocatorXPath.cart).click()
        self.assertEqual(driver.current_url,str(dataTest.base_url+"/cart"))
        #self.assertEqual(By.XPATH, LocatorXPath.cart_qty)
        #cart_qty = driver.find_element(By.NAME, "itemquantity3079896")
        #self.assertIn(value.cart_qty, cart_qty.get_attribute("innerText"))
        #price = driver.find_element(By.XPATH, LocatorXPath.price)
        #self.assertIn(dataTest.price, price.get_attribute("innerText"))
    def tearDown(self):
        self.browser.close()
        
if __name__ == '__main__':
    unittest.main()