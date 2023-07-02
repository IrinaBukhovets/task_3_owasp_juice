from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Browser import Browser


class BasePage:

    def find_element_page(self, locator, browser):
        browser = Browser()   
        browser.find_element(locator)
        return WebDriverWait(browser, 5).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")  

    def enter_word(self, locator, word):
        Browser().find_element(locator).send_keys(word)

    def click_on_the_button(self, locator, browser):
        browser = Browser()   
        browser.find_element(locator).click()

    def element_is_opened(self, locator, browser):
        browser = Browser()
        browser.find_element(locator).is_displayed()

    def text(self, locator, browser):
        browser = Browser()
        text = browser.find_element(locator).text
        return text
    
    def enter_word_and_enter(self, locator, word):
        Browser().find_element(locator).send_keys(word)
        Browser().find_element(locator).send_keys(Keys.ENTER)
        
    