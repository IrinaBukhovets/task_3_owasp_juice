from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Singletone import Singletone
from selenium.webdriver.edge.service import Service


class Browser(metaclass=Singletone):

    def __init__(self):
        self.webdriver = {}

    def set_up_driver(self):
        #service = Service(executable_path="C:\\Users\\User\\Desktop\\msedgedriver.exe")
        #self.webdriver["browser"] = webdriver.Edge(service=service)
        self.webdriver["browser"] = webdriver.Firefox()

    def get_driver(self):
        return self.webdriver["browser"]
   
    def find_element(self,locator,time=5):   
        return WebDriverWait(self.get_driver(),time).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")
        
    def go_back(self):
        self.get_driver().back()

    def refresh(self):
        self.get_driver().refresh()

    def go_to_site(self, url):
        self.get_driver().get(url)
        self.get_driver().maximize_window()

    def current_url(self,url,time=5):
        return WebDriverWait(self.get_driver(),time).until(EC.url_changes(url))

    def quit(self):
        self.get_driver().quit()
        self.webdriver.pop("browser", None)

    def find_elements(self,locator):
        return self.get_driver().find_elements(locator)
    