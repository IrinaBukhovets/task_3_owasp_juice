from Juiceshop import Label
from Juiceshop import LandingPage
from Juiceshop import LoginPage

def test_sqli(browser):
    label = Label()
    label.close_label()
    landingpage = LandingPage()
    landingpage.go_to_account()
    loginpage = LoginPage()
    loginpage.input_login_and_password("' or true--","12345")
    loginpage.is_displaye_error_message()
    error = loginpage.text_error_message()
    assert error == "Invalid email or password."



"""def test_sqli(browser):
    close_label = Label()
    close_label.close_label()
    log_in_account = LandingPage()
    log_in_account.account()
    input_login_and_password = LoginPage()
    input_login_and_password.input_login_and_password("' or true--","12345")
    error_message = LoginPage()
    error = error_message.text_error_message_invalid_log_pass()
    assert error == "Invalid email or password."""""
    

