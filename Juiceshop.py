from BaseElements import BaseElements
from selenium.webdriver.common.by import By


class Label(BaseElements):

    locator_button_close_label = (By.XPATH, "//button[contains(@aria-label,'lose')]")

    def close_label(self):
        self.press_button(locator = self.locator_button_close_label)

class LandingPage(BaseElements):

    locator_button_search = (By.XPATH, "//mat-search-bar[contains(@aria-label,'lick')]")
    locator_search_query = (By.XPATH, "//input[@id='mat-input-0']")
    locator_button_account = (By.ID, "navbarAccount")
    locator_button_login = (By.ID, "navbarLoginButton")
    

    def search_juice_shop(self, text_search):
        self.press_button(locator = self.locator_button_search)
        self.press_button(locator = self.locator_search_query)
        self.enter_word_and_enter(locator = self.locator_search_query, word = text_search)

    def go_to_account(self):
        self.press_button(locator = self.locator_button_account)
        self.press_button(locator = self.locator_button_login)

class LoginPage(BaseElements):

    locator_email = (By.ID, "email")
    locator_password = (By.ID, "password")
    locator_button_log_in = (By.ID, "loginButton")
    locator_error_message = (By. XPATH, "//div[contains(@class,'error')]")


    def input_login_and_password(self,email,password):
        self.enter_word(locator = self.locator_email, word = email)
        self.enter_word(locator = self.locator_password, word = password )
        self.press_button(locator = self.locator_button_log_in)

    def is_displaye_error_message(self):
        self.element_is_displayed(locator = self.locator_error_message)

    def text_error_message(self):
        text_error = self.get_text(locator = self.locator_error_message)
        return text_error

class SearchPage(BaseElements):

    locator_search_value = (By.XPATH, "//span[@id='searchValue']")

    def text_result_search(self):
        text = self.get_text(locator=self.locator_search_value)
        return text

