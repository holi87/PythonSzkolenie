import fixture.basic
import re
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
        self.app.open_home_page()
        self.contact_cache = None

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

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath('//*[@value="Usuń"]').click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, c_id):
        wd = self.app.wd
        self.select_contact_by_id(c_id)
        wd.find_element_by_xpath('//*[@value="Usuń"]').click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        self.contact_cache = None

    def select_contact_by_id(self, c_id):
        wd = self.app.wd
        wd.find_element_by_css_selector('input[value="%s"]' % c_id).click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def modify_contact_without_photo_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form_without_photo(contact)
        wd.find_element_by_name("update").click()
        self.app.open_home_page()
        self.contact_cache = None

    def modify_first_contact_without_photo(self, contact):
        self.modify_contact_without_photo_by_index(0, contact)

    def count(self):
        wd = self.app.wd
        # just to be sure that we are on home page
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                last_name = cells[1].text
                first_name = cells[2].text
                all_phones = cells[5].text
                address = cells[3].text
                all_mails = cells[4].text
                contact_id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                self.contact_cache.append(Contact(first_name=first_name, last_name=last_name, contact_id=contact_id
                                                  , all_phones_from_home_page=all_phones, address=address
                                                  , all_emails_from_home_page=all_mails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        contact_id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(first_name=firstname, last_name=lastname, contact_id=contact_id, mobile_phone=mobilephone
                       , home_phone=homephone, work_phone=workphone, home_phone2=secondaryphone, address=address
                       , email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        home_phone2 = re.search("P: (.*)", text).group(1)
        return Contact(first_name=None, last_name=None, mobile_phone=mobile_phone, home_phone=home_phone
                       , work_phone=work_phone, home_phone2=home_phone2)

    def merge_phones_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != ""
                                , (map(lambda x: self.clear(x), filter(lambda x: x is not None
                                                                  , [contact.home_phone, contact.mobile_phone
                                                                      , contact.work_phone, contact.home_phone2])))))

    def merge_emails_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != ""
                                , (map(lambda x: self.clear(x), filter(lambda x: x is not None
                                                                  , [contact.email, contact.email2, contact.email3])))))

    def merge_adress_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != ""
                                , (map(lambda x: self.clear(x), filter(lambda x: x is not None
                                                                  , [contact.home_phone, contact.mobile_phone
                                                                      , contact.work_phone, contact.home_phone2])))))

    def clean(self, contact):
        return Contact(contact_id=contact.contact_id, first_name=contact.first_name.strip(),
                       last_name=contact.last_name.strip())