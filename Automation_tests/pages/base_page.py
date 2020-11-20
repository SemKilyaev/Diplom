import os
import pickle
from selenium.common.exceptions import NoSuchElementException
from links import Links

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.driver.implicitly_wait(timeout)
        self.links = Links()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def open(self):
        self.driver.get(self.url)

    def save_cookies(self, cookies_name):
        pickle.dump(self.driver.get_cookies(), open(
            os.getcwd() + "\\cookies\\" + cookies_name + ".pkl", "wb"))

    def load_cookies(self, link=None, cookies_name="None"):
        cookies = pickle.load(
            open(os.getcwd() + "\\cookies\\" + cookies_name + ".pkl", "rb"))
        self.driver.get(link)
        for cookie in cookies:
            if 'expiry' in cookie:
                del cookie['expiry']
            self.driver.add_cookie(cookie)
        self.driver.get(link)
