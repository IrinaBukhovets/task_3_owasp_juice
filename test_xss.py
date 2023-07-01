from Juiceshop import LandingPage
from Juiceshop import SearshPage
from Juiceshop import Label
import time


def test_xss(browser):
    close_label = Label()
    close_label.close_label()
    time.sleep(2)
    search_juice_shop = LandingPage()
    search = '<iframe src="javascript:alert("hello")">'
    search_juice_shop.search_juice_shop(text_search = search)
    time.sleep(2)
    text_result_search = SearshPage()
    text_result_search.result_search()
    assert text_result_search == search

