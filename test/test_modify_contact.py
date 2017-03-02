from model.contact import Contact
__author__ = "Grzegorz Holak"


def test_modify_first_contact(app):
    old_contacts = app.contact.get_contact_list()

    contact = Contact(first_name="jakies losowe", last_name="nazwisko siakie")
    contact.contact_id = old_contacts[0].contact_id

    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="imieDodane", last_name="NazwiskoDodane"))
    app.contact.modify_first_contact_without_photo(contact)
    new_contacts = app.contact.get_contact_list()

    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_first_name(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="jakies losowe", last_name=None)
    contact.contact_id = old_contacts[0].contact_id
    contact.last_name = old_contacts[0].last_name  # because in object contact last_name is None, same like for id

    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="imieDodane", last_name="NazwiskoDodane"))
    app.contact.modify_first_contact_without_photo(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
