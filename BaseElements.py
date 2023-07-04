
from selenium.webdriver.common.keys import Keys
from BasePage import BasePage
from Browser import Browser


class BaseElements():

    def press_button(self, locator, browser = Browser()):   
        Browser().find_element(locator).click()

    def enter_word(self, locator, word):
        Browser().find_element(locator).send_keys(word)

    def get_text(self, locator):
        text = Browser().find_element(locator).text
        return text
    
    def enter_word_and_enter(self, locator, word):
        Browser().find_element(locator).send_keys(word)
        Browser().find_element(locator).send_keys(Keys.ENTER)

    def element_is_displayed(self, locator):
        Browser().find_element(locator).is_displayed()


    """def press_button_close_label(self):
        self.click_on_the_button(locator = self.locator_button_close_label, browser = Browser())

    def enter_word_in_element_search(self, text_search):
        self.click_on_the_button(locator=self.locator_button_search, browser = Browser())
        self.click_on_the_button(locator=self.locator_search_query, browser = Browser())
        self.enter_word_and_enter(locator = self.locator_search_query, word = text_search)

    def account(self):
        self.click_on_the_button(locator = self.locator_button_account, browser = Browser())
        self.click_on_the_button(locator = self.locator_button_login, browser = Browser()) 

    def enter_word_login(self,email):
        self.enter_word(self.locator_email, word = email)

    def enter_word_password(self,password):
        self.enter_word(self.locator_password, word = password)

    def press_button_log_in(self):
        self.click_on_the_button(self.locator_button_log_in, browser = Browser())

    def text_error_message(self):
        text = self.text(locator = self.locator_error_message, browser = Browser())
        return text
    
    def text_search_value(self):
        text = self.text(locator=self.locator_search_value, browser = Browser())
        return text"""
    
    