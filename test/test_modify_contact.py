from model.contact import Contact
from random import randrange
__author__ = "Grzegorz Holak"


def test_modify_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="imieDodane", last_name="NazwiskoDodane"))

    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))

    contact = Contact(first_name="imie", last_name="nazwisko", mobile_phone="321", home_phone2="31"
                      , work_phone="53", home_phone="111")
    contact.contact_id = old_contacts[index].contact_id

    app.contact.modify_contact_without_photo_by_index(index, contact)

    assert len(old_contacts) == app.contact.count()

    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_some_contact_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="imieDodane", last_name="NazwiskoDodane"))

    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))

    contact = Contact(first_name="HAAAALO", last_name=None)
    contact.contact_id = old_contacts[index].contact_id
    contact.last_name = old_contacts[index].last_name  # because in object contact last_name is None, same like for id

    app.contact.modify_contact_without_photo_by_index(index, contact)

    assert len(old_contacts) == app.contact.count()

    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
