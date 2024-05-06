from selenium import webdriver
import pytest
import time
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    return driver