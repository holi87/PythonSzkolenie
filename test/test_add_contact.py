# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_without_photo(Contact(first_name="imie", last_name="nazwisko", mobile_phone="12123"
                                             , email="email@email.dt", birthday_day=1, birthday_month=1))
    app.session.logout()

