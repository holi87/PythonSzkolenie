from model.contact import Contact
import random
__author__ = "Grzegorz Holak"


def test_del_first_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_without_photo(Contact(first_name="jakies losowe", last_name="nazwisko siakie",
                                                 email="email@maryna.xt", mobile_phone="1241241"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.contact_id)
    assert app.contact.count() == len(old_contacts) - 1
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        db_contacts_list = map(app.contact.clean, db.get_contact_list())
        assert sorted(db_contacts_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)
