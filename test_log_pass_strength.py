from Juiceshop import LandingPage
from Juiceshop import LoginPage
from Juiceshop import Label
import pytest


@pytest.mark.parametrize("login, password, result", 
                         [('admin','123','Invalid email or password.'),
                          ('stan@juice-sh.op','1234abc','Invalid email or password.'),
                           ('admin@juice-sh.op', 'admin123','Invalid email or password.')])


def test_log_pass_strength(browser, login, password, result):
    close_label = Label()
    close_label.close_label()
    log_in_account = LandingPage()
    log_in_account.account()
    input_login_and_password = LoginPage()
    input_login_and_password.input_login_and_password(login=login,password=password)
    error_message = LoginPage()
    error = error_message.text_error_message_invalid_log_pass()
    assert error == result
    