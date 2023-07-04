from selenium.webdriver.common.by import By
from BasePage import BasePage
from Browser import Browser


class BaseElements(BasePage):

    locator_button_close_label = (By.XPATH, "//button[contains(@aria-label,'lose')]")
    locator_button_search = (By.XPATH, "//mat-search-bar[contains(@aria-label,'lick')]")
    locator_search_query = (By.XPATH, "//input[@id='mat-input-0']")
    locator_button_account = (By.ID, "navbarAccount")
    locator_button_login = (By.ID, "navbarLoginButton")
    locator_email = (By.ID, "email")
    locator_password = (By.ID, "password")
    locator_button_log_in = (By.ID, "loginButton")
    locator_error_message = (By. XPATH, "//div[contains(@class,'error')]")
    locator_search_value = (By.XPATH, "//span[@id='searchValue']")

    def press_button_close_label(self):
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
        return text
    
    