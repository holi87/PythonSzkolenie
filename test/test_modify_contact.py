from model.contact import Contact
__author__ = "Grzegorz Holak"


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="jakies losowe", last_name="nazwisko siakie", email="email@maryna.xt"
                                   , mobile_phone="1241241"))
    app.contact.modify_first_contact_without_photo(Contact(first_name="noweImie", last_name="noweNazwisko"
                                                           , mobile_phone="99999", email="newemail@email.pl"
                                                           , birthday_day=27, birthday_month=11, birthday_year="1988"
                                                           , address="Gdzieś w Mińsku Mazowieckim"))


def test_modify_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="jakies losowe", last_name="nazwisko siakie", email="email@maryna.xt"
                                   , mobile_phone="1241241"))
    app.contact.modify_first_contact_without_photo(Contact(first_name="noweImie", last_name=None
                                                           , mobile_phone=None, email=None))
