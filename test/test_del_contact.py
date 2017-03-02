from model.contact import Contact
from random import randrange
__author__ = "Grzegorz Holak"


def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="jakies losowe", last_name="nazwisko siakie", email="email@maryna.xt"
                                   , mobile_phone="1241241"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert app.contact.count() == len(old_contacts) - 1
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts
