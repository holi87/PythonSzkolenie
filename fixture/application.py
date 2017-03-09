from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.basic import BasicHelper

__author__ = "Grzegorz Holak"


class Application:

    def __init__(self, browser="firefox", base_url="http://localhost:8080/addressbook/"):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser: %s" % browser)
        # delete because it is not need in this app
        # self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.basic = BasicHelper(self)

    def destroy(self):
        self.wd.quit()
    # przeniesc spowrotem to + dorobic usera i haslo tak samo i wyslac commit.
    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and wd.find_elements_by_xpath('.//*/select[@name="group"]')):
            wd.get("http://localhost:8080/addressbook/")
