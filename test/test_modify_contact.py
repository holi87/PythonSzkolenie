from model.contact import Contact
__author__ = "Grzegorz Holak"


def test_modify_first_contact(app):
    app.contact.modify_first_contact_without_photo(Contact(first_name="noweImie", last_name="noweNazwisko"
                                                           , mobile_phone="99999", email="newemail@email.pl"
                                                           , birthday_day=27, birthday_month=11, birthday_year="1988"
                                                           , address="Gdzieś w Mińsku Mazowieckim"))
