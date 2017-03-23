from model.group import Group
import random
__author__ = "Grzegorz Holak"


def test_delete_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="nazwa"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    # print(group)
    app.group.delete_group_by_id(group.group_id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == app.group.count()
    # print(old_groups)
    old_groups.remove(group)
    # print(old_groups)
    # print(new_groups)
    assert old_groups == new_groups

