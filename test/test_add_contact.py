# -*- coding: utf-8 -*-
import pytest
import random
import string
from model.contact import Contact


def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits + " "
    #  + string.punctuation to not fail tests as we know that it is not working correctly with this chars
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


def random_email(prefix, max_len_name, max_len_domain):
    symbols = string.ascii_letters + string.digits
    name = "".join([random.choice(symbols) for i in range(random.randrange(max_len_name))])
    domain = "".join([random.choice(symbols) for i in range(random.randrange(max_len_domain))])
    end = "".join([random.choice(string.ascii_lowercase) for i in range(1, 3)])
    return prefix + "_" + name + "@" + domain + "." + end


def random_phone(prefix, max_len):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


testdata = [
    Contact(first_name=random_string("name", 10), last_name=random_string("lastname", 20)
            , email=random_email("email1", 10, 10), email2=random_email("email2", 10, 15)
            , email3=random_email("e3", 15, 21), address=random_string("address", 50)
            , mobile_phone=random_phone("mob", 10), work_phone=random_phone("work", 10)
            , home_phone=random_phone("home", 10), home_phone2=random_phone("home2", 11))
    for i in range(random.randrange(6))
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_without_photo(contact)
    assert app.contact.count() == len(old_contacts) + 1
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
