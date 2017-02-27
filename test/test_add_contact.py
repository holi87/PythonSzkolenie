# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_without_photo(Contact(first_name="imie", last_name="nazwisko", mobile_phone="12123"
                                             , email="email@email.dt", birthday_day=1, birthday_month=1))
    app.session.logout()

