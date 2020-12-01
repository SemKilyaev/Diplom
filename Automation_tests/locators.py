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
    LINK_TASK = f".//a//p[text()='Date completed - {Data.DATETIME_FIND} ']"
    LINK_TASK_DELETE = f".//a//p[text()='Date completed - {Data.DATETIME_FIND_2} ']"
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
    INPUT_DATETIME = ".//input[@name='make_up']"
    BUTTON_CHECK = ".//a[@href='/datecomplete']/button[@type='button']"


    