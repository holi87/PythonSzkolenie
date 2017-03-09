from model.contact import Contact
from random import randrange

__author__ = "Grzegorz Holak"


def test_contact_on_home_page(app):
    # when there is no contact - make one for test
    if app.contact.count() == 0:
        app.contact.create_without_photo(Contact(first_name="jakies losowe", last_name="nazwisko siakie", home_phone="12411+1"
                                   , mobile_phone="1241241", email="email1@kda.as", email2="dasda@dad.ad"
                                   , address="""line1
                                   line2"""))
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    # testing phones
    assert contact_from_home_page.all_phones_from_home_page == app.\
        contact.merge_phones_like_on_home_page(contact_from_edit_page)
    # testing emails
    assert contact_from_home_page.all_emails_from_home_page == app.\
        contact.merge_emails_like_on_home_page(contact_from_edit_page)
    # testing address
    assert contact_from_home_page.address == contact_from_edit_page.address
    # testing first name
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    # testing last name
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
