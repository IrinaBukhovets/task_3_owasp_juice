import pytest
from Juiceshop import LandingPage
from Juiceshop import LoginPage


@pytest.mark.parametrize("email", ['stan@juice-sh.op', 'admin@juice-sh.op'])
@pytest.mark.parametrize("password", ['Aa123456', ')4ever', 'admin', '1qaz@WSX', 'P@ssw0rd','123456QQAqqa_','1qaz!QAZ','wowecarts@123','film@123','Spiritwear_2004'])  
@pytest.mark.parametrize ("result", ['Invalid email or password.'])                 

def test_password_strength(browser, email, password, result):
    landingpage = LandingPage()
    landingpage.landingpage_is_onened()
    landingpage.go_to_account()
    loginpage = LoginPage()
    loginpage.loginpage_is_opened()
    loginpage.input_login_and_password(email = email, password = password)
    error = loginpage.text_error_message()
    assert error == result 



    