from pages.login import Login
from pages.create import Create
from pages.valid import Valid
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
import time
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    return driver


#Test for login page
def test_login(driver):
    login = Login(driver)
    login.open()
    login.fill_fields()
    time.sleep(3)
    assert "https://test.qa.saritasa.com/admin/dashboard" == driver.current_url
    login.right_url(driver)
    driver.close();

#Test for create page
def test_create_post(driver):
    login = Login(driver)
    login.open()
    login.fill_fields()
    time.sleep(3)
    create_post = Create(driver)
    create_post.create_post_link()
    time.sleep(2)
    create_post.create_post_fields()
    create_post.create_post()
    time.sleep(3)
    assert "Post was successfully created!"
    driver.close();

#Test for validation messages about required fields
def test_valid(driver):
    login = Login(driver)
    login.open()
    login.fill_fields()
    time.sleep(3)
    create_post = Create(driver)
    create_post.create_post_link()
    create_post = Valid(driver)
    create_post.create_post_link_valid()
    assert len(driver.find_element(By.CLASS_NAME, "validation").text) != 0, "Сannot be empty!"
    #print(driver.find_element(By.CLASS_NAME, "validation").text)
    create_post = Create(driver)
    create_post.create_post_fields()
    time.sleep(5)
    driver.close();



#Test all together

def test_all(driver):
    login = Login(driver)
    login.open()
    login.fill_fields()
    time.sleep(3)
    test_all = Create(driver)
    test_all.create_post_link()
    test_all = Valid(driver)
    test_all.create_post_link_valid()
    assert len(driver.find_element(By.CLASS_NAME, "validation").text) != 0, "Сannot be empty!"
    test_all = Create(driver)
    time.sleep(2)
    test_all.create_post_fields()
    test_all.create_post()
    time.sleep(3)
    assert "Post was successfully created!"
    driver.close();
