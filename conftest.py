import pytest
import logging
from Browser import Browser
from general_config import GeneralConfigs
from Juiceshop import WelcomeLabel

logger = logging.getLogger()

@pytest.fixture(scope="function")  #Это означает что данная функция-фикстура будет исполнятся только 1 раз за тестовую сессию
def browser():
    browser = Browser()
    browser.set_up_driver()
    browser.go_to_site(GeneralConfigs.BASE_URL)
    browser.current_url(GeneralConfigs.BASE_URL)
    logger.info("Успешная загрузка веб сайта")
    label = WelcomeLabel()
    if not label.welcomelable_is_opened():
        pass
    label.close_welcome_label()
    logger.info("Приветственная страница закрыта")
    yield browser
    browser.quit()
    logger.info("Выход из браузера")