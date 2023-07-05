import logging
from Juiceshop import LandingPage
from Juiceshop import LoginPage


logger = logging.getLogger()

def test_sqli(browser):
    landingpage = LandingPage()
    landingpage.landingpage_is_onened()
    logger.info("Главная страница открыта")
    landingpage.go_to_account()
    loginpage = LoginPage()
    loginpage.loginpage_is_opened()
    logger.info("Страница входа в аккаунт открыта")
    loginpage.input_login_and_password("' or true--","12345")
    error = loginpage.text_error_message()
    logger.info("Ошибка входа в аккаунт - Invalid email or password.")
    assert error == "Invalid email or password."




