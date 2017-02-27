
__author__ = "Grzegorz Holak"


def test_del_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(first_name="noweImie", last_name="noweNazwisko", mobile_phone="99999"
                                             , email="newemail@email.dt", birthday_day=27, birthday_month=11
                                             , birthday_year="1988", address="Gdzieś w Mińsku Mazowieckim"))
    app.session.logout()
