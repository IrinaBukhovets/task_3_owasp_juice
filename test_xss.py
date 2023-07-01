from Juiceshop import LandingPage
from Juiceshop import SearchPage
from Juiceshop import Label
from BaseElements import BaseElements
import time

def test_xss(browser):
    close_label = Label()
    close_label.close_label()
    time.sleep(2)
    search_juice_shop = LandingPage()
    search = '<iframe src="javascript:alert("hello")"'
    #<iframe src="javascript:alert("hello")">
    search_juice_shop.search_juice_shop(text_search = search)
    time.sleep(2)
    text_result_search = SearchPage()
    result_search = text_result_search.text_result_search()
    assert result_search == search

