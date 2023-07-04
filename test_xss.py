import logging
from Juiceshop import Label
from Juiceshop import LandingPage
from Juiceshop import SearchPage


logger = logging.getLogger()

def test_xss(browser):
    close_label = Label()
    close_label.close_label()
    logger.info("Приветственное окно закрыто")
    search_juice_shop = LandingPage()
    search = '<iframe src="javascript:alert("hello")"'
    search_juice_shop.search_juice_shop(text_search = search)
    logger.info("Поиск информации произведен")
    text_result_search = SearchPage()
    result_search = text_result_search.text_result_search()
    logger.info("Открыта страница с результатом поиска")
    assert result_search == search, "Текст в результате поиска НЕ соответствует тексту поискового запроса"
    logger.warning("Текст в результате поиска соответствует тексту поискового запроса")
