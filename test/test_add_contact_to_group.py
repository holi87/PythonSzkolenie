from model.contact import Contact
from model.group import Group
import random
__author__ = "Grzegorz Holak"


def test_add_contact_to_group(app, orm):
    # checks if there is any group
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="nazwa"))
    groups_list = orm.get_group_list()
    group = random.choice(groups_list)

    # checks if there is any contact out of group (not matter if there is no contact at all or all are in group)
    if len(orm.get_contacts_not_in_group(Group(group_id=group.group_id))) == 0:
        app.contact.create_without_photo(Contact(first_name="imieDodane", last_name="NazwiskoDodane"))

    contacts_list = orm.get_contacts_not_in_group(Group(group_id=group.group_id))
    contact = random.choice(contacts_list)

    app.contact.select_contact_by_id(contact.contact_id)
    app.group.select_group_to_add_contact_by_id(group.group_id)
    app.contact.add_contact_to_group()
    # checks in db if this contact was added to group
    assert contact in orm.get_contacts_in_group(Group(group_id=group.group_id))
