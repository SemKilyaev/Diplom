import pytest
import allure
from links import Links
from pages.main_page import MainPage
from data import Data


@pytest.mark.usefixtures("driver")
@allure.parent_suite("TODO list")
@allure.suite("TODO list test")
class Test_TODO_list:

    def setup(self):
        self.links = Links()
        self.main_page = MainPage(self.driver)
        self.data = Data()
        self.driver.get(self.links.landing)

    @allure.testcase('TODO list registration')
    @pytest.mark.smoke
    @pytest.mark.reg
    def test_registration(self):
        with allure.step("Open register page"):
            self.main_page.go_to_register_page()
        with allure.step("Enter username"):
            self.main_page.enter_username(self.data.NAME)
        with allure.step("Enter email"):
            self.main_page.enter_email(self.data.EMAIL)
        with allure.step("Enter password"):
            self.main_page.enter_password(self.data.PASSWORD)
        with allure.step("Confirm password"):
            self.main_page.enter_password_confirm(self.data.PASSWORD)
        with allure.step("Click register"):
            self.main_page.click_button_register()
        with allure.step("Check register"):
            self.main_page.check_register()

    @allure.testcase('TODO list login')
    @pytest.mark.smoke
    @pytest.mark.login
    def test_login(self):
        with allure.step("Enter login"):
            self.main_page.input_login(self.data.NAME)
        with allure.step("Enter password"):
            self.main_page.input_password_login(self.data.PASSWORD)
        with allure.step("Click button login"):
            self.main_page.click_button_login()
            self.main_page.save_cookies('todolist')
        with allure.step("Check Login"):
            self.main_page.check_login_after()

    @allure.testcase('TODO list add task')
    @pytest.mark.smoke
    @pytest.mark.add_tasks
    def test_add_tasks(self):
        with allure.step("Login"):
            self.main_page.load_cookies(self.links.login, "todolist")
        with allure.step("Enter datetime"):
            self.main_page.input_datetime(self.data.DATETIME)
        with allure.step("Enter task"):
            self.main_page.input_task(self.data.TASK1)
        with allure.step("Click button add"):
            self.main_page.click_button_add()
        with allure.step("Check add"):
            self.main_page.check_task()

    @allure.testcase('TODO list delete complited task')
    @pytest.mark.smoke
    @pytest.mark.delete_tasks
    def test_delete_tasks(self):
        with allure.step("Login"):
            self.main_page.load_cookies(self.links.login, "todolist")
        with allure.step("Enter datetime"):
            self.main_page.input_datetime(self.data.DATETIME_FALSE)
        with allure.step("Enter task"):
            self.main_page.input_task(self.data.TASK_FOR_DELETE)
        with allure.step("Click button add"):
            self.main_page.click_button_add()
        with allure.step("Check add"):
            self.main_page.check_task_before_delete()
        with allure.step("Click task"):
            self.main_page.click_task()
        with allure.step("Click delete completed"):
            self.main_page.click_delete_completed_task()
        with allure.step("Check task"):
            self.main_page.check_task_after_delete()

    @allure.testcase('TODO list delete all tasks')
    @pytest.mark.smoke
    @pytest.mark.delete_all
    def test_delete_all_tasks(self):
        with allure.step("Login"):
            self.main_page.load_cookies(self.links.login, "todolist")
        with allure.step("Enter datetime"):
            self.main_page.input_datetime(self.data.DATETIME_FALSE)
        with allure.step("Enter task1"):
            self.main_page.input_task(self.data.TASK_FOR_DELETE)
        with allure.step("Click button add"):
            self.main_page.click_button_add()
        with allure.step("Check add"):
            self.main_page.check_task_before_delete()
        with allure.step("Enter datetime"):
            self.main_page.input_datetime(self.data.DATETIME)
        with allure.step("Enter task2"):
            self.main_page.input_task(self.data.TASK1)
        with allure.step("Click button add"):
            self.main_page.click_button_add()
        with allure.step("Check add"):
            self.main_page.check_task()
        with allure.step("Click delete all"):
            self.main_page.click_delete_all_tasks()
        with allure.step("Check tasks"):
            self.main_page.check_tasks_after_delete_all()

    @allure.testcase('TODO list weather add and delete city')
    @pytest.mark.smoke
    @pytest.mark.weather_add_del
    def test_weather_add_delete_city(self):
        with allure.step("Login"):
            self.main_page.load_cookies(self.links.login, "todolist")
        with allure.step("Click Weather"):
            self.main_page.click_link_weather()
        with allure.step("Add city"):
            self.main_page.input_city(self.data.CITY)
        with allure.step("Click confirm"):
            self.main_page.click_button_confirm()
        with allure.step("Check city"):
            self.main_page.check_temperature()
            
            self.main_page.check_city()
        with allure.step("Delete city"):
            self.main_page.click_button_delete_city()
        with allure.step("Check city after delete"):
            self.main_page.check_temperature_after_delete()
            self.main_page.check_city_after_delete()

    @allure.testcase('TODO list weather add wrong city')
    @pytest.mark.smoke
    @pytest.mark.weather_false_city
    def test_weather_input_false_city(self):
        with allure.step("Login"):
            self.main_page.load_cookies(self.links.login, "todolist")
        with allure.step("Click Weather"):
            self.main_page.click_link_weather()
        with allure.step("Add city"):
            self.main_page.input_city(self.data.FALSE_CITY)
        with allure.step("Click confirm"):
            self.main_page.click_button_confirm()
        with allure.step("Check Error"):
            self.main_page.check_error_city()

    @allure.testcase('TODO list button home')
    @pytest.mark.smoke
    @pytest.mark.btn_home
    def test_button_home(self):
        with allure.step("Login"):
            self.main_page.load_cookies(self.links.login, "todolist")
        with allure.step("Click Weather"):
            self.main_page.click_link_weather()
        with allure.step("Click Home"):
            self.main_page.click_button_home()
        with allure.step("Check Home page"):
            self.main_page.check_link_weather()

    @allure.testcase('TODO list button check')
    @pytest.mark.smoke
    @pytest.mark.check
    def test_add_tasks(self):
        with allure.step("Login"):
            self.main_page.load_cookies(self.links.login, "todolist")
        with allure.step("Enter datetime"):
            self.main_page.input_datetime(self.data.DATETIME_FALSE)
        with allure.step("Enter task"):
            self.main_page.input_task(self.data.TASK1)
        with allure.step("Click button add"):
            self.main_page.click_button_add()
        with allure.step("Click button check"):
            self.main_page.click_button_check()

    @allure.testcase('TODO list logout')
    @pytest.mark.smoke
    @pytest.mark.logout
    def test_button_logout(self):
        with allure.step("Login"):
            self.main_page.load_cookies(self.links.login, "todolist")
        with allure.step("Logout"):
            self.main_page.click_logout()
        with allure.step("Check page login"):
            self.main_page.check_login()

