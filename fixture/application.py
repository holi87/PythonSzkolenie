from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.basic import BasicHelper

__author__ = "Grzegorz Holak"


class Application:

    def __init__(self):
        self.wd = WebDriver()
        # delete because it is not need in this app
        # self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.basic = BasicHelper(self)

    def destroy(self):
        self.wd.quit()


