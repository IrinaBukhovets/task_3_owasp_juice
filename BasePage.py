from task_3_owasp_juice.Browser import Browser
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    def find_element_page(self, locator, browser):
        browser = Browser()   
        browser.find_element(self, locator)
        return WebDriverWait(browser, 5).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")  

    def enter_word(self, locator, word):
        Browser().find_element(locator).send_keys(word)

    def click_on_the_button(self, locator, browser):
        browser = Browser()   
        browser.find_element(locator).click()

    def element_is_opened(self, locator, browser):
        browser = Browser()
        browser.find_element(locator).is_displayed()