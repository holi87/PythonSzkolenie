from model.contact import Contact
# from random import randrange
__author__ = "Grzegorz Holak"


def test_contact_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create_without_photo(Contact(first_name="jakies losowe", last_name="nazwisko siakie",
                                                 home_phone="12411+1", mobile_phone="1241241",
                                                 email="email1@kda.as", email2="dasda@dad.ad", address="""line1
                                                                                                        line2"""))
    contacts_from_home_page = sorted(app.contact.get_contact_list(),  key=Contact.id_or_max)
    contacts_from_db = list(map(app.contact.clean, db.get_contact_list()))
    assert len(contacts_from_db) == len(contacts_from_home_page)  # first issue could be if lists won't be same length
    for i in range(len(contacts_from_db)):
        assert contacts_from_home_page[i].contact_id == contacts_from_db[i].contact_id
        assert contacts_from_home_page[i].first_name == contacts_from_db[i].first_name
        assert contacts_from_home_page[i].last_name == contacts_from_db[i].last_name
    # I did not make checks for address, emails and phones - it is just make merge function and take more
    # info from database in db fixture about phones, address and emails. But merge was made for edit page, so
    # there is no need to duplicate. But if it is necessary to do pass task - I will do it.

