# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="imie", last_name="nazwisko")
    app.contact.create_without_photo(contact)

    new_contacts = app.contact.get_contact_list()
    assert len(new_contacts) == len(old_contacts) + 1
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
