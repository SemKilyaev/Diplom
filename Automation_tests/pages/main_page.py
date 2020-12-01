import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators import Locators
from allure_commons.types import AttachmentType



class MainPage(BasePage):
    BUTTON_SIGN_UP = (By.XPATH, Locators.BUTTON_SIGN_UP)
    INPUT_USERNAME = (By.XPATH, Locators.INPUT_USERNAME)
    INPUT_EMAIL = (By.XPATH, Locators.INPUT_EMAIL)
    INPUT_PASSWORD = (By.XPATH, Locators.INPUT_PASSWORD)
    INPUT_PASSWORD_CONFIRM = (By.XPATH, Locators.INPUT_PASSWORD_CONFIRM)
    BUTTON_REGISTER_ACCOUNT = (By.XPATH, Locators.BUTTON_REGISTER_ACCOUNT)
    LINK_LOGIN = (By.XPATH, Locators.LINK_LOGIN)
    CHECK_REGISTER = (By.XPATH, Locators.CHECK_REGISTER)
    INPUT_LOGIN = (By.XPATH, Locators.INPUT_LOGIN)
    INPUT_PASSWORD_LOGIN = (By.XPATH, Locators.INPUT_PASSWORD_LOGIN)
    BUTTON_LOGIN = (By.XPATH, Locators.BUTTON_LOGIN)
    CHECK_LOGIN = (By.XPATH, Locators.CHECK_LOGIN)
    INPUT_TASK = (By.XPATH, Locators.INPUT_TASK)
    BUTTON_ADD = (By.XPATH, Locators.BUTTON_ADD)
    LINK_TASK = (By.XPATH, Locators.LINK_TASK)
    LINK_TASK_DELETE = (By.XPATH, Locators.LINK_TASK_DELETE)
    BUTTON_DELETE_COMPLETED = (By.XPATH, Locators.BUTTON_DELETE_COMPLETED)
    BUTTON_DELETE_ALL = (By.XPATH, Locators.BUTTON_DELETE_ALL)
    LINK_WEATHER = (By.XPATH, Locators.LINK_WEATHER)
    INPUT_ADD_CITY = (By.XPATH, Locators.INPUT_ADD_CITY)
    BUTTON_CONFIRM = (By.XPATH, Locators.BUTTON_CONFIRM)
    CHECK_CITY = (By.XPATH, Locators.CHECK_CITY)
    CHECK_TEMPERATURE = (By.XPATH, Locators.CHECK_TEMPERATURE)
    BUTTON_DELETE_CITY = (By.XPATH, Locators.BUTTON_DELETE_CITY)
    LINK_HOME = (By.XPATH, Locators.LINK_HOME)
    ERROR_CITY_CHECK = (By.XPATH, Locators.ERROR_CITY_CHECK)
    LINK_LOGOUT = (By.XPATH, Locators.LINK_LOGOUT)
    CHECK_LOGIN = (By.XPATH, Locators.CHECK_LOGIN)
    INPUT_DATETIME = (By.XPATH, Locators.INPUT_DATETIME)
    BUTTON_CHECK = (By.XPATH, Locators.BUTTON_CHECK)


    def input_datetime(self, date):
        input_datetime = self.driver.find_element(*self.INPUT_DATETIME)
        assert self.is_element_present(*self.INPUT_DATETIME), "Datetime input is not presented"
        input_datetime.send_keys(date)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def click_check_datetime(self):
        button_check = self.driver.find_element(*self.BUTTON_CHECK)
        assert self.is_element_present(*self.BUTTON_SIGN_UP), "Button check is not presented"
        button_check.click()
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def go_to_register_page(self):
        login_link = self.driver.find_element(*self.BUTTON_SIGN_UP)
        assert self.is_element_present(*self.BUTTON_SIGN_UP), "Button sign up is not presented"
        login_link.click()
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def enter_username(self, username):
        input_username = self.driver.find_element(*self.INPUT_USERNAME)
        assert self.is_element_present(*self.INPUT_USERNAME), "Username input is not presented"
        input_username.send_keys(username)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def enter_email(self, email):
        input_email = self.driver.find_element(*self.INPUT_EMAIL)
        assert self.is_element_present(*self.INPUT_EMAIL), "Email input is not presented"
        input_email.send_keys(email)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)
    
    def enter_password(self, password):
        input_password = self.driver.find_element(*self.INPUT_PASSWORD)
        assert self.is_element_present(*self.INPUT_PASSWORD), "Password input is not presented"
        input_password.send_keys(password)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def enter_password_confirm(self, password_confirm):
        input_password_confirm = self.driver.find_element(*self.INPUT_PASSWORD_CONFIRM)
        assert self.is_element_present(*self.INPUT_PASSWORD_CONFIRM), "Password confirm input is not presented"
        input_password_confirm.send_keys(password_confirm)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def click_button_register(self):
        button_register = self.driver.find_element(*self.BUTTON_REGISTER_ACCOUNT)
        assert self.is_element_present(*self.BUTTON_REGISTER_ACCOUNT), "Button register is not presented"
        button_register.click()
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def check_register(self):
        assert self.is_element_present(*self.CHECK_REGISTER), "Text is not presented"
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def go_to_login_page_reverse(self):
        login_link_reverse = self.driver.find_element(*self.LINK_LOGIN)
        assert self.is_element_present(*self.LINK_LOGIN), "Login link up is not presented"
        login_link_reverse.click()
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def input_login(self, login):
        input_login = self.driver.find_element(*self.INPUT_LOGIN)
        assert self.is_element_present(*self.INPUT_LOGIN), "Login input is not presented"
        input_login.send_keys(login)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def input_password_login(self, password):
        input_password_login = self.driver.find_element(*self.INPUT_PASSWORD_LOGIN)
        assert self.is_element_present(*self.INPUT_PASSWORD_LOGIN), "Login input is not presented"
        input_password_login.send_keys(password)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def click_button_login(self):
        button_login = self.driver.find_element(*self.BUTTON_LOGIN)
        assert self.is_element_present(*self.BUTTON_LOGIN), "Button login is not presented"
        button_login.click()
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def check_login_after(self):
        assert self.is_element_present(*self.LINK_HOME), "Not home"
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def check_login(self):
        assert self.is_element_present(*self.CHECK_LOGIN), "Not login"
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def input_task(self, task):
        input_task = self.driver.find_element(*self.INPUT_TASK)
        assert self.is_element_present(*self.INPUT_TASK), "Task input is not presented"
        input_task.send_keys(task)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def click_button_add(self):
        button_add = self.driver.find_element(*self.BUTTON_ADD)
        assert self.is_element_present(*self.BUTTON_ADD), "Button add is not presented"
        button_add.click()
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def check_task(self):
        assert self.is_element_present(*self.LINK_TASK), "Task is not presented"
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def check_task_before_delete(self):
        assert self.is_element_present(*self.LINK_TASK_DELETE), "Task is not presented"
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def click_task(self):
        button_task = self.driver.find_element(*self.LINK_TASK_DELETE)
        assert self.is_element_present(*self.LINK_TASK_DELETE), "Button link is not presented"
        button_task.click()
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def click_delete_completed_task(self):
        button_delete_completed = self.driver.find_element(*self.BUTTON_DELETE_COMPLETED)
        assert self.is_element_present(*self.BUTTON_DELETE_COMPLETED), "Button delete complited is not presented"
        button_delete_completed.click()
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def check_task_after_delete(self):
        assert not self.is_element_present(*self.LINK_TASK_DELETE), "Task is presented"
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def delete_completed_task(self):
        button_delete_completed = self.driver.find_element(*self.BUTTON_DELETE_COMPLETED)
        assert self.is_element_present(*self.BUTTON_DELETE_COMPLETED), "Button delete complited is not presented"
        button_delete_completed.click()
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def click_delete_all_tasks(self):
        button_delete_all = self.driver.find_element(*self.BUTTON_DELETE_ALL)
        assert self.is_element_present(*self.BUTTON_DELETE_ALL), "Button delete all is not presented"
        button_delete_all.click()
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)
    
    def check_tasks_after_delete_all(self):
        assert not self.is_element_present(*self.LINK_TASK_DELETE), "Task is presented"
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)
        assert not self.is_element_present(*self.LINK_TASK), "Task is presented"
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def click_link_weather(self):
        link_weather = self.driver.find_element(*self.LINK_WEATHER)
        assert self.is_element_present(*self.LINK_WEATHER), "Link weather is not presented"
        link_weather.click()
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def input_city(self, city):
        input_add_city = self.driver.find_element(*self.INPUT_ADD_CITY)
        assert self.is_element_present(*self.INPUT_ADD_CITY), "Add city input is not presented"
        input_add_city.send_keys(city)
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def click_button_confirm(self):
        button_confirm = self.driver.find_element(*self.BUTTON_CONFIRM)
        assert self.is_element_present(*self.BUTTON_CONFIRM), "Button confirm is not presented"
        button_confirm.click()
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def check_city(self):
        assert self.is_element_present(*self.CHECK_CITY), "City is not presented"
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def check_temperature(self):
        assert self.is_element_present(*self.CHECK_TEMPERATURE), "Temperature is not presented"
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def click_button_delete_city(self):
        button_delete_city = self.driver.find_element(*self.BUTTON_DELETE_CITY)
        assert self.is_element_present(*self.BUTTON_DELETE_CITY), "Button delete is not presented"
        button_delete_city.click()
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def check_city_after_delete(self):
        assert not self.is_element_present(*self.CHECK_CITY), "City is presented"
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def check_temperature_after_delete(self):
        assert not self.is_element_present(*self.CHECK_TEMPERATURE), "Temperature is presented"
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def click_button_home(self):
        link_home = self.driver.find_element(*self.LINK_HOME)
        assert self.is_element_present(*self.LINK_HOME), "Link home is not presented"
        link_home.click()
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def check_error_city(self):
        assert self.is_element_present(*self.ERROR_CITY_CHECK), "Error city is not presented"
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def click_logout(self):
        link_logout = self.driver.find_element(*self.LINK_LOGOUT)
        assert self.is_element_present(*self.LINK_LOGOUT), "Logout link is not presented"
        link_logout.click()
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def check_login_after_logout(self):
        assert self.is_element_present(*self.CHECK_LOGIN), "Text LOGIN is not presented"
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)

    def check_link_weather(self):
        assert self.is_element_present(*self.LINK_WEATHER), "Link Weather is not presented"
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)


    def click_button_check(self):
        button_check = self.driver.find_element(*self.BUTTON_CHECK)
        assert self.is_element_present(*self.BUTTON_CHECK), "Button check is not presented"
        button_check.click()
        allure.attach(self.driver.get_screenshot_as_png(),
                      name="Screenshot", attachment_type=AttachmentType.PNG)


