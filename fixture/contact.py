__author__ = "Grzegorz Holak"


class ContactHelper:

    def __init__(self, app):
        self.app = app

    # should make it better to read but have no idea how now - before task 7.
    # maybe should I make methods for important think and less important
    # like contact_name (first, middle, last, email, phone)
    # rest ? I have no idea.
    def create_without_photo(self, contact):
        wd = self.app.wd
        # go to contact creator
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
        # these xpaths are not good enough - need to correct it later
        wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%d]" % contact.birthday_day).click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%d]" % contact.birthday_month).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birthday_year)
        # these xpaths are not good enough - need to correct it later

        wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[%d]" % contact.ann_month).click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[%d]" % contact.ann_day).click()
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
        # as return to home page
        self.app.open_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        # no need to go into any page as contacts can be deleted from home page
        wd.find_element_by_name("selected[]").click()
        # now for me easier is use Xpath so make xpath for del button
        wd.find_element_by_xpath('//*[@value="Usuń"]').click()
        # as written in homework - i am using method switch to alert
        wd.switch_to_alert().accept()
        self.app.open_home_page()

    def modify_first_contact(self):
        pass
