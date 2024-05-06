from pages.base import BasePage
from locators.locators import TextLocator
from selenium import webdriver

class Valid(BasePage):

    def create_post_link_valid(self):
        locators = TextLocator()
        return self.find(locators.TITLE).click(), self.find(locators.AUTHOR).click(), self.find(locators.DATE).click()

    def create_post_text(self):
        locators = TextLocator()
        return self.find(locators.VALID)

