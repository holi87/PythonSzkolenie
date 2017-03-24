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
    # checks if there is any contact in this group, if not making one with adding to this group on creation
    if len(orm.get_contacts_in_group(Group(group_id=group.group_id))) == 0:
        app.contact.create_with_selected_group(Contact(first_name="imieDodane", last_name="NazwiskoDodane"),
                                               group_id=group.group_id)

    app.group.select_group_by_id_to_display_contacts(group.group_id)

    contacts_list = orm.get_contacts_in_group(Group(group_id=group.group_id))
    contact = random.choice(contacts_list)
    app.contact.select_contact_by_id(contact.contact_id)
    app.group.del_selected_contact_from_group()

    assert contact not in orm.get_contacts_in_group(Group(group_id=group.group_id))
