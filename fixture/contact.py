import fixture.basic
from model.contact import Contact
__author__ = "Grzegorz Holak"


class ContactHelper(fixture.basic.BasicHelper):

    def __init__(self, app):
        super(ContactHelper, self).__init__(app)

    def create_without_photo(self, contact):
        wd = self.app.wd
        # go to contact creator
        wd.find_element_by_link_text("nowy wpis").click()
        self.fill_contact_form_without_photo(contact)
        # save contact
        wd.find_element_by_name("submit").click()
        # as return to home page
        self.open_home_page()

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
        self.change_field_value("address", contact.address)

    def fill_company_info(self, contact):
        wd = self.app.wd
        self.change_field_value("company", contact.company)
        self.change_field_value("title", contact.title)

    def fill_name_info(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("nickname", contact.nick)

    def fill_phone_info(self, contact):
        wd = self.app.wd
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax)

    def fill_online_info(self, contact):
        wd = self.app.wd
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)

    def select_group(self):
        # selecting group - commented to leave it as is
        # wd = self.app.wd
        # wd.find_element_by_xpath('//*[@name="new_group"]/option[0]').click()
        pass

    def fill_additional_info(self, contact):
        wd = self.app.wd
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.home_phone2)
        self.change_field_value("notes", contact.notes)

    def fill_anniversary(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@name="aday"]/option[%d]' % contact.ann_day).click()
        wd.find_element_by_xpath('//*[@name="amonth"]/option[%d]' % contact.ann_month).click()
        self.change_field_value("ayear", contact.ann_year)

    def fill_birthday(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@name="bday"]/option[%d]' % contact.birthday_day).click()
        wd.find_element_by_xpath('//*[@name="bmonth"]/option[%d]' % contact.birthday_month).click()
        self.change_field_value("byear", contact.birthday_year)

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath('//*[@value="Usuń"]').click()
        wd.switch_to_alert().accept()
        self.open_home_page()

    def modify_first_contact_without_photo(self, contact):
        wd = self.app.wd
        # go to first contact editor
        wd.find_element_by_xpath('//*[@src="icons/pencil.png"]').click()
        self.fill_contact_form_without_photo(contact)
        wd.find_element_by_name("update").click()
        self.open_home_page()

    def count(self):
        wd = self.app.wd
        # just to be sure that we are on home page
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    # this function is really strange, I am not sure is it correct way for now.
    # I wanted make for each loop more user friendly - looping by elements of table, but it is not so easy.
    # Xpaths are from this "not perfect" ones, but no alternative.
    def get_contact_list(self):
        wd = self.app.wd
        self.open_home_page()
        contacts = []
        i = 2  # because first element is in row nr = 2
        for row in wd.find_elements_by_name("selected[]"):
            # i-th row td 2nd and 3rd
            first_name = wd.find_element_by_xpath("//*[@id='maintable']/tbody/tr[%d]/td[2]" % i).text
            last_name = wd.find_element_by_xpath("//*[@id='maintable']/tbody/tr[%d]/td[3]" % i).text
            contact_id = row.get_attribute("value")
            contacts.append(Contact(first_name=first_name, last_name=last_name, contact_id=contact_id))
            i += 1  # making iterator +1 for next row in loop
        return contacts
