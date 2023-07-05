from selenium.webdriver.common.keys import Keys
from Browser import Browser


class BaseElements():

    def __init__(self, locator) -> None:
        self.locator = locator

    def press_button(self):   
        Browser().find_element(self.locator).click()

    def enter_word(self, word):
        Browser().find_element(self.locator).send_keys(word)

    def get_text(self):
        text = Browser().find_element(self.locator).text
        return text

    def enter_word_and_enter(self, word):
        Browser().find_element(self.locator).send_keys(word)
        Browser().find_element(self.locator).send_keys(Keys.ENTER)

    def element_is_displayed(self):
        element = Browser().find_elements(locator = self.locator)
        return element