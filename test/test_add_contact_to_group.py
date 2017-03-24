from model.contact import Contact
from model.group import Group
import random
__author__ = "Grzegorz Holak"


def test_add_contact_to_group(app, orm):
    # checks if there is any contact and any group and making ones if there is none
    if len(orm.get_contact_list()) == 0:
        app.contact.create_without_photo(Contact(first_name="imieDodane", last_name="NazwiskoDodane"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="nazwa"))
    groups_list = orm.get_group_list()
    group = random.choice(groups_list)
    contacts_list = orm.get_contacts_not_in_group(Group(group_id=group.group_id))
    contact = random.choice(contacts_list)
    app.contact.select_contact_by_id(contact.contact_id)
    app.group.select_group_to_add_contact_by_id(group.group_id)
    app.contact.add_contact_to_group()
    assert contact in orm.get_contacts_in_group(Group(group_id=group.group_id))
