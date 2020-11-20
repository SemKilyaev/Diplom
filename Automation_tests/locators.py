from selenium.webdriver.common.by import By
from data import Data

class Locators:

    BUTTON_SIGN_UP = ".//a[@href='/register/']"
    INPUT_USERNAME = ".//input[@name='username']"
    INPUT_EMAIL = ".//input[@name='email']"
    INPUT_PASSWORD = ".//input[@name='password1']"
    INPUT_PASSWORD_CONFIRM = ".//input[@name='password2']"
    BUTTON_REGISTER_ACCOUNT = ".//input[@value='Register Account']"
    LINK_LOGIN = ".//a[@href='/login/']"
    CHECK_REGISTER = f".//p[text()='Account was created for{Data.NAME}']"
    INPUT_LOGIN = ".//input[@name='username']"
    INPUT_PASSWORD_LOGIN = ".//input[@name='password']"
    BUTTON_LOGIN = ".//input[@value='Login']"
    CHECK_LOGIN = f".//span[text()='Hello, {Data.NAME}']"
    INPUT_TASK = ".//input[@name='text']"
    BUTTON_ADD = ".//button[text()='ADD']"
    LINK_TASK = f".//li[text()='{Data.TASK1}']"
    LINK_TASK_DELETE = f".//li[text()='{Data.TASK_FOR_DELETE}']"
    BUTTON_DELETE_COMPLETED = ".//a[@href='/deletecompleted']/button[@type='button']"
    BUTTON_DELETE_ALL = ".//a[@href='/deleteall']/button[@type='button']"
    LINK_WEATHER = ".//a[text()='Weather']"
    INPUT_ADD_CITY = ".//input[@name='name']"
    BUTTON_CONFIRM = ".//input[@name='send']"
    CHECK_CITY = ".//b[text()='City: ']"
    CHECK_TEMPERATURE = ".//b[text()='Temperature: ']"
    BUTTON_DELETE_CITY = ".//a/button[@type='button']"
    LINK_HOME = ".//a[text()='Home']"
    ERROR_CITY_CHECK = ".//li[@class='info']"
    LINK_LOGOUT = ".//span/a[@href='/logout/']"
    CHECK_LOGIN = ".//h3[text()='LOGIN']"

    