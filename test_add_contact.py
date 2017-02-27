# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact_without_photo(Contact(first_name="imie", last_name="nazwisko", mobile_phone="12123"
                                                 , email="email@email.dt", birthday_day=1, birthday_month=1))
    app.logout()

