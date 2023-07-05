from Browser import Browser


class BasePage:
  
    def page_is_opened(self,unique_locator):
        Browser().find_element(unique_locator).is_displayed()


        
    