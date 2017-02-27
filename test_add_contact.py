# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Contact

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.create_new_contact_without_photo(wd, Contact(first_name="imie", last_name="nazwisko", mobile_phone="12123"
                                                          , email="email@email.dt", birthday_day="19"
                                                          , birthday_month='1'))
        self.open_home_page(wd) # as return to home page
        self.logout(wd)

    def open_home_page(self, wd):
        wd.get("http://localhost:8080/addressbook/")

    def login(self, wd, username="admin", password="secret"):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def create_new_contact_without_photo(self, wd, contact):

        wd.find_element_by_link_text("nowy wpis").click()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nick)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        # phone numbers -> I made mobile without default blank
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        # emails second and third with default as blank, cause we can but not need to fill it
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # these xpaths are not good enough - need to correct it later - and this part not working.
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option['%s']" % contact.birthday_day)\
                .is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option['%s']" % contact.birthday_day).click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option['%s']" % contact.birthday_month)\
                .is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option['%s']" % contact.birthday_month)\
                .click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birthday_year)
        # these xpaths are not good enough - need to correct it later - this part not working
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option['%s']" % contact.ann_month)\
                .is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option['%s']" % contact.ann_month).click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option['%s']" % contact.ann_day)\
                .is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option['%s']" % contact.ann_day).click()
        # selecting group - commented to leave it as is
        # if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[0]").is_selected():
        #     wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[0]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ann_year)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.home_phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # these xpaths are not good enough - need to correct it later
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Wyloguj się").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
