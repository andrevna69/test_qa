from selenium.webdriver.common.by import By
class TextLocator:
    EMAIL =(By.ID,"email")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.CLASS_NAME,"btn")
    CREATE_POST = (By.LINK_TEXT,"Create post")
    TITLE = (By.ID,"title")
    EDITOR = (By.CLASS_NAME,"ql-editor")
    AUTHOR = (By.ID,"author")
    DATE = (By.ID,"actual-date")
    VALID = (By.CLASS_NAME, "validation")
    CREATE = (By.CLASS_NAME, "btn")


class Input_All:
    email = "testuser@saritasa.com"
    password = "NewQA123!"
    title = "Post Title"
    author = "Author"
    editor = "P0st text"
    actual_date = "11052024"
    url ="https://test.qa.saritasa.com/admin/login"
    dashboard="https://test.qa.saritasa.com/admin/dashboard"

