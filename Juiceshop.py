from BaseElements import BaseElements


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
        self.enter_word_login(email=login)
        self.enter_word_password(password = password)
        self.press_button_log_in()

    def find_error_message_element_page(self):
        self.element_error_message()

    def text_error_message_invalid_log_pass(self):
        text_error = self.text_error_message()
        return text_error

class SearchPage(BaseElements):
    def text_result_search(self):
        text_search = self.text_search_value()
        return text_search
