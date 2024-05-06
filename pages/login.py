from pages.base import BasePage
from locators.locators import TextLocator
from locators.locators import Input_All

class Login(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        url = Input_All
        self.driver.get(url.url)

    def fill_fields(self):
        locators = TextLocator()
        inputs = Input_All
        return self.find(locators.EMAIL).send_keys(inputs.email), self.find(locators.PASSWORD).send_keys(inputs.password), self.find(locators.LOGIN).click()

    def right_url(self, driver):
        url_cur = driver.current_url
        locators = Input_All()
        if(locators.dashboard == url_cur):
            print("User is logged in,", url_cur, "page is opened")
        else:
            print("Tried to connect to server but failed or the address is incorrect")
