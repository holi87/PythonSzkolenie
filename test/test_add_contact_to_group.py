from model.contact import Contact
import random
__author__ = "Grzegorz Holak"


def test_add_contact_to_group(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_without_photo(Contact(first_name="imieDodane", last_name="NazwiskoDodane"))

    if check_ui:
        pass

    """
    wejscie na strone glowna
    zaznaczenie kontaktu
    wybranie z listy wyboru grupy do ktorej chcemy dodac
    sprawdzenie z bazy danych czy kontakt jest w tej grupie
    jesli nie jest to dodajemy go poprzez klikniecie w przycisk dodaj do
    jesli jest to nic nie robimy
    sprawdzenie w bazie danych czy kontakt jest w tej grupie 
    """

    pass
