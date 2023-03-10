class LocatorXPath():
    radio_button_male = "//input[@id='gender-male']"
    radio_button_female = "//input[@id='gender-female']"
    firstname = "//input[@id='FirstName']"
    lastname = "//input[@id='LastName']"
    email = "//input[@id='Email']"
    password = "//input[@id='Password']"
    confirm_password = "//input[@id='ConfirmPassword']"
    button_register = "//input[@id='register-button']"
    success_register = "//div[@class='result']"
    #success_register = "//div[@class='result']//span[contains(text(),'Your registration completed')]"
    register = "//a[@class='ico-register']"
    login = "//a[@class='ico-login']"
    button_login = "//input[@value='Log in']"
    button_continue = "//input[@value='Continue']"
    button_logout = "//a[@class='ico-logout']"
    validation_firstname = "//span[@class='field-validation-error']//span[@for='FirstName']"
    validation_lastname = "//span[@class='field-validation-error']//span[@for='LastName']"
    validation_email = "//span[@class='field-validation-error']//span[@for='Email']"
    validation_password = "//span[@class='field-validation-error']//span[@for='Password']"
    validation_confirm_password = "//span[@class='field-validation-error']//span[@for='ConfirmPassword']"
    validation_email_exist = "//li[normalize-space()='The specified email already exists']"
    error_login = "//span[contains(text(),'Login was unsuccessful. Please correct the errors and try again.')]"
    error_not_found = "//li[normalize-space()='No customer account found']"
    error_invalid_cred = "//li[normalize-space()='The credentials provided are incorrect']"
    error_invalid_email = "//span[@class='field-validation-error']//span[@for='Email']"
