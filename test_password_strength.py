import pytest
from Juiceshop import LandingPage
from Juiceshop import LoginPage
from Juiceshop import Label



@pytest.mark.parametrize("email", ['stan@juice-sh.op', 'admin@juice-sh.op'])
@pytest.mark.parametrize("password", ['Aa123456', ')4ever', 'admin', '1qaz@WSX', 'P@ssw0rd','123456QQAqqa_','1qaz!QAZ','wowecarts@123','film@123','Spiritwear_2004'])  
@pytest.mark.parametrize ("result", ['Invalid email or password.'])                 

"""def test_password_strength(browser, email, password, result):
    close_label = Label()
    close_label.close_label()
    log_in_account = LandingPage()
    log_in_account.account()
    input_login_and_password = LoginPage()
    input_login_and_password.input_login_and_password(login=email,password=password)
    error_message = LoginPage()
    error = error_message.text_error_message_invalid_log_pass()
    assert error == result"""
    