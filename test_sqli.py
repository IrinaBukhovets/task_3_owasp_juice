from Juiceshop import LandingPage
from Juiceshop import LoginPage
from Juiceshop import Label
import time

def test_sqli(browser):
    close_label = Label()
    close_label.close_label()
    time.sleep(2)
    log_in_account = LandingPage()
    log_in_account.account()
    time.sleep(2)
    input_login_and_password = LoginPage()
    input_login_and_password.input_login_and_password("' or true--","12345")
    #"' or true--"
    time.sleep(2)
    error_message = LoginPage()
    error = error_message.text_error_message_invalid_log_pass()
    assert error == "Invalid email or password."
    

