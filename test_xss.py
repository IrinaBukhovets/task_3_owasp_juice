import logging
from Juiceshop import LandingPage
from Juiceshop import SearchPage


logger = logging.getLogger()

def test_xss(browser):
    landingpage = LandingPage()
    landingpage.landingpage_is_onened()
    logger.info("Главная страница открыта")
    search = '<iframe src="javascript:alert("hello")"'
    landingpage.search_juice_shop(text_search = search)
    searchpage = SearchPage()
    searchpage.searchpage_is_opened()
    logger.info("Страница поиска продуктов открыта")
    result_search = searchpage.text_result_search()
    assert result_search == search, "Текст в результате поиска НЕ соответствует тексту поискового запроса"
    logger.warning("Текст в результате поиска соответствует тексту поискового запроса")




