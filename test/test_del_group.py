from model.group import Group
import random
__author__ = "Grzegorz Holak"


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="nazwa"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.group_id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == app.group.count()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        db_groups_list = map(app.group.clean, db.get_group_list())
        assert sorted(db_groups_list, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

