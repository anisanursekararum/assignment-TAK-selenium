from datetime import datetime

class dataTest():
    base_url = "https://demowebshop.tricentis.com"
    firstname = "Ryujin"
    lastname = "Shin"
    dt_string = datetime.now().strftime("%Y%m%d-%H%M%S")
    email = "ryujin"+dt_string+"@gmail.com"
    static_email = "moonbyul2805@gmail.com"
    wrong_email_format = "haha.com"
    correct_password = "Pass123"
    wrong_password = "papapa123"
    less_char_password = "12"
    empty_field = ""
    validation_firstname = "First name is required."
    validation_lastname = "Last name is required."
    validation_email = "Email is required."
    validation_format_email = "Wrong email"
    validation_password = "Password is required."
    validation_char_password = "The password should have at least 6 characters."
    validation_mismatch_password = "The password and confirmation password do not match."
    validation_email_exist = "The specified email already exists"
    validation_message = "Your registration completed"
    #success_message = "Your registration completed"
    welcome = "Welcome to our store"
    error_login = "Login was unsuccessful. Please correct the errors and try again"
    error_not_found = "No customer account found"
    error_invalid_cred = "The credentials provided are incorrect"
    error_invalid_email = "Please enter a valid email address."
    laptop = "14.1-inch Laptop"
    shopping = "Shopping cart"
    shipping = "Estimate shipping"