from task_3_owasp_juice.BasePage import BasePage 
from selenium.webdriver.common.by import By
from task_3_owasp_juice.Browser import Browser


class BaseElements(BasePage):

    locator_button_close_label = (By.XPATH, "///button[contains(@aria-label,’Close Welcome Banner’)]")
    locator_search_query = (By.ID, "searchQuery")
    locator_button_account = (By.ID, "navbarAccount")
    locator_button_login = (By.ID, "navbarLoginButton")
    locator_email = (By.ID, "email")
    locator_password = (By.ID, "password")
    locator_button_log_in = (By.ID, "loginButton")
    locator_error_message = (By.XPATH, "//div[@class='error ng-star-inserted']")
    locator_search_value = (By.ID, "searchValue")

    def element_button_search(self):
        self.find_element_page(locator = self.locator_search_query, browser = Browser())

    def element_button_account(self):
        self.find_element_page(self.locator_button_account, browser = Browser())

    def element_button_login(self):
        self.find_element_page(self.locator_button_login, browser = Browser())

    def element_email(self):
        self.find_element_page(self.locator_email, browser = Browser())

    def element_password(self):
        self.find_element_page(self.locator_password, browser = Browser())

    def element_button_log_in(self):
        self.find_element_page(self.locator_button_log_in, browser = Browser())

    def element_error_message(self):
        self.find_element_page(self.locator_error_message, browser = Browser()) 

    def element_search_value(self):
        self.find_element_page(self.locator_search_value, browser = Browser())

    def press_button_close_label(self):
        self.click_on_the_button(Locator = self.locator_button_close_label, browser = Browser())

    def enter_word_in_element_search(self, text_search):
        self.enter_word(locator = self.locator_search_query, word = text_search)

    def account(self):
        self.click_on_the_button(locator = self.locator_button_account, browser = Browser())
        self.click_on_the_button(locator = self.locator_button_account, browser = Browser())
        self.click_on_the_button(locator = self.locator_button_login, browser = Browser()) 
        #??????

    def enter_word_login(self,email):
        self.enter_word(self.locator_email, word = email)

    def enter_word_password(self,password):
        self.enter_word(self.locator_password, word = password)

    def press_button_log_in(self):
        self.click_on_the_button(self.locator_button_log_in, browser = Browser())