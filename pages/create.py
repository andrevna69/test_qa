from pages.base import BasePage
from locators.locators import TextLocator
from locators.locators import Input_All

class Create(BasePage):
    def create_post_link(self):
        locators = TextLocator()
        return self.find(locators.CREATE_POST).click()

    def create_post_fields(self):
        locators = TextLocator()
        inputs = Input_All
        return self.find(locators.TITLE).send_keys(inputs.title), self.find(locators.EDITOR).send_keys(inputs.editor),\
               self.find(locators.AUTHOR).send_keys(inputs.author),  self.find(locators.DATE).send_keys(inputs.actual_date)

    def create_post(self):
        locators = TextLocator()
        return self.find(locators.CREATE).click()

