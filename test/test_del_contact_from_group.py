from model.contact import Contact
from model.group import Group
import random
__author__ = "Grzegorz Holak"


def test_del_contact_from_group(app, orm):
    # checks if there is any group
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="nazwa"))
    groups_list = orm.get_group_list()
    group = random.choice(groups_list)
    print(orm.get_contacts_in_group(Group(group_id=group.group_id)))
    print(group.group_id)
    if len(orm.get_contacts_in_group(Group(group_id=group.group_id))) == 0:
        app.contact.create_with_selected_group(Contact(first_name="imieDodane", last_name="NazwiskoDodane"),
                                               group_id=group.group_id)
        print(orm.get_contacts_in_group(Group(group_id=group.group_id)))
    #app.group.select_group_to_display_contacts_by_id(group.group_id)  # todo


    """
    wejscie na strone glowna
    
    zaznaczenie grupy z ktorej chcemy usunac kontakt
    sprawdzenie w bazie czy kontakt jest w bazie (nie potrzebne de facto bo nie wybierzemy jak go nie ma)
    wybranie kontaktu do usuniecia
    
    klikniecie usun z nazwa_grupy
    
    sprawdzenie w bazie czy kontakt juz jest poza baza
    
    """
    pass
