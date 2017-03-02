from model.contact import Contact
__author__ = "Grzegorz Holak"


def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="jakies losowe", last_name="nazwisko siakie", email="email@maryna.xt"
                                   , mobile_phone="1241241"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    assert app.contact.count() == len(old_contacts) - 1
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
