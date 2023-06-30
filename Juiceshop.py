from task_3_owasp_juice.BaseElements import BaseElements
from task_3_owasp_juice.BasePage import BasePage

class Label(BaseElements):
    def close_label(self):
        self.press_button_close_label()

class LandingPage(BaseElements):

    def search_juice_shop(self, text_search):
        self.enter_word_in_element_search(text_search = text_search)

    def log_in_account(self):
        self.account()

class LoginPage(BaseElements):

    def input_login_and_password(self,login,password):
        input_login = self.enter_word_login(email=login)
        input_password = self.enter_word_password(password = password)
        button_log_in = self.press_button_log_in()

    def error_message(self):
        error_message = self.element_error_message()
        return error_message.text

class SearshPage(BaseElements):

    def result_search(self):
        result = self.element_search_value()
        return result.text
