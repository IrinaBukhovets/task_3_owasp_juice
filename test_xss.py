from task_3_owasp_juice.Juiceshop import LandingPage
from task_3_owasp_juice.Juiceshop import SearshPage
from task_3_owasp_juice.Juiceshop import Label


def test_xss(browser):
    close_label = Label()
    close_label.close_label()
    search_juice_shop = LandingPage()
    search = '<iframe src="javascript:alert("hello")">'
    search_juice_shop.search_juice_shop(text_search = search)
    text_result_search = SearshPage()
    text_result_search.result_search()
    assert text_result_search == search

