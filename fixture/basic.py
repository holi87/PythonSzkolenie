import re
__author__ = "Grzegorz Holak"


class BasicHelper:

    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def is_valid(self):
        try:
            self.app.wd.current_url()
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and wd.find_elements_by_xpath('.//*/select[@name="group"]')):
            wd.get("http://localhost:8080/addressbook/")

    def clear(self, s):
        return re.sub("[() -]", "", s)
