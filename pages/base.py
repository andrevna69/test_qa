from locators.locators import Input_All
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, args):
        return self.driver.find_element(*args)

    def click(self, locator):
        self.find(*locator).click()

    def find_click_date(self, args):
        return self.driver.find_element(*args).click()


