from model.contact import Contact
from random import randrange

__author__ = "Grzegorz Holak"


def test_names_on_home_page(app):
    # when there is no contact - make one for test
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="jakies losowe", last_name="nazwisko siakie"))
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    # testing first name
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    # testing last name
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
