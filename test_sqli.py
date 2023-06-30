from task_3_owasp_juice.Juiceshop import LandingPage
from task_3_owasp_juice.Juiceshop import LoginPage
import time

def test_sqli(browser):
    log_in_account = LandingPage()
    log_in_account.account()
    time.sleep(2)
    input_login_and_password = LoginPage()
    input_login_and_password.input_login_and_password("' or true--","12345")
    error_message = LoginPage()
    error_message.error_message()
    assert error_message == "Invalid email or password."

