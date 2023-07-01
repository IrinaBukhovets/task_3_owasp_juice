from Juiceshop import LandingPage
from Juiceshop import LoginPage



@pytest.mark.parametrize("login", [0, 1])

@pytest.mark.parametrize("password", [2, 3])

def parametr(login,password):

    pass



def test_log_pass_strength(browser):

    log_in_account = LandingPage()

    log_in_account.account()

    input_login_and_password = LoginPage()

    input_login_and_password.input_login_and_password("' or true--","12345")
