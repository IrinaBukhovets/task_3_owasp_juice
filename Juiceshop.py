from BasePage import BasePage
from Button import Button
from Tex_box import Tex_box
from Line import Line
from selenium.webdriver.common.by import By


class WelcomeLabel(BasePage):

    LOCATOR_BUTTON_CLOSE_WELCOME_LABEL = (By.XPATH, "//button[contains(@aria-label,'lose')]")

    def welcomelable_is_opened(self):
        self.page_is_opened(unique_locator=self.LOCATOR_BUTTON_CLOSE_WELCOME_LABEL)

    def close_welcome_label(self):
        welcome_label_btn = Button(locator = self.LOCATOR_BUTTON_CLOSE_WELCOME_LABEL)
        welcome_label_btn.press_button()

class LandingPage(BasePage):

    LOCATOR_PRODUCTS = (By.XPATH,"//div[contains(text(),'All Products')]")
    LOCATOR_BUTTON_SEARCH = (By.XPATH, "//mat-search-bar[contains(@aria-label,'lick')]")
    LOCATOR_SEARCH_QUERY = (By.XPATH, "//input[@id='mat-input-0']")
    LOCATOR_BUTTON_ACCOUNT = (By.ID, "navbarAccount")
    LOCATOR_BUTTON_LOGIN = (By.ID, "navbarLoginButton")

    def landingpage_is_onened(self):
        self.page_is_opened(unique_locator=self.LOCATOR_PRODUCTS)

    def search_juice_shop(self, text_search):
        search_btn = Button(locator = self.LOCATOR_BUTTON_SEARCH)
        search_btn.press_button()
        search_query_btn = Button(locator = self.LOCATOR_SEARCH_QUERY)
        search_query_btn.press_button()
        enter_word_and_enter_in_textbox = Tex_box(locator = self.LOCATOR_SEARCH_QUERY)
        enter_word_and_enter_in_textbox.enter_word_and_enter(word = text_search)

    def go_to_account(self):
        account_btn = Button(locator=self.LOCATOR_BUTTON_ACCOUNT)
        account_btn.press_button()
        login_btn = Button(locator=self.LOCATOR_BUTTON_LOGIN)
        login_btn.press_button()

class LoginPage(BasePage):

    LOCATOR_EMEIL = (By.ID, "email")
    LOCATOR_PASSWORD = (By.ID, "password")
    LOCATOR_BUTTON_LOG_IN = (By.ID, "loginButton")
    LOCATOR_ERROR_MESSAGE = (By.XPATH, "//div[contains(@class,'error')]")
    LOCATOR_ERROR_MESSAGE = (By.XPATH, "//div[contains(@class,'error')]")
    LOCATOR_ERROR_MESSAGE_WITH_TEXT = (By.XPATH, "//div[contains(text(),'Invalid email or password.')]")

    def loginpage_is_opened(self):
        self.page_is_opened(unique_locator=self.LOCATOR_BUTTON_LOG_IN)


    def input_login_and_password(self,email,password):
        login_tex_box = Tex_box(locator = self.LOCATOR_EMEIL)
        login_tex_box.enter_word(word = email)
        password_tex_box = Tex_box(locator = self.LOCATOR_PASSWORD)
        password_tex_box.enter_word(word = password)
        log_in_btn = Button(locator = self.LOCATOR_BUTTON_LOG_IN)
        log_in_btn.press_button()

    def text_error_message(self):
        error_message_line = Line(locator = self.LOCATOR_ERROR_MESSAGE)
        text_error = error_message_line.get_text()
        return text_error

    def is_displaye_error_message_with_text(self):
        error_message_with_text = Line(locator = self.LOCATOR_ERROR_MESSAGE_WITH_TEXT)
        element = error_message_with_text.element_is_displayed()
        return element
        

class SearchPage(BasePage):

    LOCATOR_SEARCH_RESULT = (By.XPATH, "//span[contains(text(),'Search')]")
    LOCATOR_SEARCH_VALUE = (By.XPATH, "//span[@id='searchValue']")

    def searchpage_is_opened(self):
        self.page_is_opened(unique_locator=self.LOCATOR_SEARCH_RESULT)

    def text_result_search(self):
        result_search = Line(locator = self.LOCATOR_SEARCH_VALUE)
        text = result_search.get_text()
        return text

