__author__ = "Grzegorz Holak"


class ContactHelper:

    def __init__(self, app):
        self.app = app

    # OK, now it looks much better - I am not doing same with group fixture as on videos it isn't, maybe later
    # it will be better.

    def create_without_photo(self, contact):
        wd = self.app.wd
        # go to contact creator
        wd.find_element_by_link_text("nowy wpis").click()
        self.fill_contact_form_without_photo(contact)
        # save contact
        wd.find_element_by_name("submit").click()
        # as return to home page
        self.app.open_home_page()

    def fill_contact_form_without_photo(self, contact):
        self.fill_name_info(contact)
        self.fill_company_info(contact)
        self.fill_address(contact)
        self.fill_phone_info(contact)
        self.fill_online_info(contact)
        self.fill_birthday(contact)
        self.fill_anniversary(contact)
        self.select_group()
        self.fill_additional_info(contact)

    def fill_address(self, contact):
        wd = self.app.wd
        self.app.change_field_value("address", contact.address)

    def fill_company_info(self, contact):
        wd = self.app.wd
        self.app.change_field_value("company", contact.company)
        self.app.change_field_value("title", contact.title)

    def fill_name_info(self, contact):
        wd = self.app.wd
        self.app.change_field_value("firstname", contact.first_name)
        self.app.change_field_value("middlename", contact.middle_name)
        self.app.change_field_value("lastname", contact.last_name)
        self.app.change_field_value("nickname", contact.nick)

    def fill_phone_info(self, contact):
        wd = self.app.wd
        self.app.change_field_value("home", contact.home_phone)
        self.app.change_field_value("mobile", contact.mobile_phone)
        self.app.change_field_value("work", contact.work_phone)
        self.app.change_field_value("fax", contact.fax)

    def fill_online_info(self, contact):
        wd = self.app.wd
        self.app.change_field_value("email", contact.email)
        self.app.change_field_value("email2", contact.email2)
        self.app.change_field_value("email3", contact.email3)
        self.app.change_field_value("homepage", contact.homepage)

    def select_group(self):
        # selecting group - commented to leave it as is
        # wd = self.app.wd
        # wd.find_element_by_xpath('//*[@name="new_group"]/option[0]').click()
        pass

    def fill_additional_info(self, contact):
        wd = self.app.wd
        self.app.change_field_value("address2", contact.address2)
        self.app.change_field_value("phone2", contact.home_phone2)
        self.app.change_field_value("notes", contact.notes)

    def fill_anniversary(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@name="aday"]/option[%d]' % contact.ann_day).click()
        wd.find_element_by_xpath('//*[@name="amonth"]/option[%d]' % contact.ann_month).click()
        self.app.change_field_value("ayear", contact.ann_year)

    def fill_birthday(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@name="bday"]/option[%d]' % contact.birthday_day).click()
        wd.find_element_by_xpath('//*[@name="bmonth"]/option[%d]' % contact.birthday_month).click()
        self.app.change_field_value("byear", contact.birthday_year)

    def delete_first_contact(self):
        wd = self.app.wd
        # no need to go into any page as contacts can be deleted from home page
        wd.find_element_by_name("selected[]").click()
        # now for me easier is use Xpath so make xpath for del button
        wd.find_element_by_xpath('//*[@value="Usuń"]').click()
        # as written in homework - i am using method switch to alert
        wd.switch_to_alert().accept()
        self.app.open_home_page()

    def modify_first_contact_without_photo(self, contact):
        wd = self.app.wd
        # go to first contact editor
        wd.find_element_by_xpath('//*[@src="icons/pencil.png"]').click()
        self.fill_contact_form_without_photo(contact)
        wd.find_element_by_name("update").click()
        # as return to home page
        self.app.open_home_page()

