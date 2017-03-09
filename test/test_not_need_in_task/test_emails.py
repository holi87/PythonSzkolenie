from model.contact import Contact
from random import randrange
__author__ = "Grzegorz Holak"


def test_emails_on_home_page(app):
    # when there is no contact - make one for test
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="jakies losowe", last_name="nazwisko siakie", email="tata@tat.kl"
                                   , email2="trutu@kl.tw"))
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_emails_from_home_page == app.\
        contact.merge_emails_like_on_home_page(contact_from_edit_page)
