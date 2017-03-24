from model.contact import Contact

__author__ = "Grzegorz Holak"


def test_contact_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create_without_photo(Contact(first_name="jakies losowe", last_name="nazwisko siakie",
                                                 home_phone="12411+1", mobile_phone="1241241",
                                                 email="email1@kda.as", email2="dasda@dad.ad", address="""line1
                                                                                                        line2"""))
    '''
    wziac liste kontaktow z home page
    wziac liste kontaktow z bazy danych
    asercja czy dlugosc list jest rowna
    i sprawdzenie kazdego kontaktu przez petle for i in range(dlugosc_listy)
    assercje co ponizej == contact_from_database[i].odpowiedniki
    
    '''
    contacts_from_home_page = app.contact.get_contact_list()
    print(contacts_from_home_page)
    contacts_from_db = db.get_contact_list()
    # testing first name
    assert contacts_from_home_page[i].first_name
    # testing last name
    assert contacts_from_home_page[i].last_name
    # testing id
    assert contacts_from_home_page[i].contact_id
