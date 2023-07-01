from BasePage import BasePage 
from selenium.webdriver.common.by import By
from Browser import Browser
from selenium.webdriver.common.keys import Keys


class BaseElements(BasePage):

    locator_button_close_label = (By.XPATH, "//button[@aria-label='Close Welcome Banner']")
    locator_button_search = (By.XPATH, "//mat-search-bar[@aria-label='Click to search']")
    locator_search_query = (By.XPATH, "//input[@id='mat-input-0']")
    #locator_search_query = (By.XPATH, "//div[@class='mat-form-field-underline ng-tns-c21-6 ng-star-inserted']")
    #locator_search_query = (By.XPATH, "//mat-form-field[@class='mat-form-field mat-search_field ng-tns-c21-6 mat-primary ng-tns-c113-1 ng-trigger ng-trigger-slideInOut mat-form-field-type-mat-input mat-form-field-appearance-standard mat-form-field-can-float ng-valid ng-star-inserted ng-touched ng-dirty mat-form-field-should-float mat-focuced']")
    #locator_search_query = (By.XPATH, "//span[@class='mat-search_icons ng-tns-c113-1 mat-search_icons--active']")
    locator_button_account = (By.ID, "navbarAccount")
    locator_button_login = (By.ID, "navbarLoginButton")
    locator_email = (By.ID, "email")
    locator_password = (By.ID, "password")
    locator_button_log_in = (By.ID, "loginButton")
    locator_error_message = (By. XPATH, "//div[@class='error ng-star-inserted']")
    locator_search_value = (By.XPATH, "//span[@id='searchValue']")

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
    
    