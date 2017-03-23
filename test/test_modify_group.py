from model.group import Group
import random
__author__ = "Grzegorz Holak"


def test_modify_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="nazwa"))

    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    mod_group = Group(name="nowaNazwaGrupy", header="blablabla", footer="trubadur")
    mod_group.group_id = group.group_id  # need to copy ID from group

    app.group.modify_group_by_id(group.group_id, mod_group)

    assert len(old_groups) == app.group.count()

    new_groups = db.get_group_list()

    # we have assertion for sorted by ID so I can remove and then add group to the list with same ID
    old_groups.remove(group)
    old_groups.append(mod_group)

    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        db_groups_list = map(app.group.clean, db.get_group_list())
        assert sorted(db_groups_list, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

#
# def test_modify_some_group_name(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="nazwa"))
#     old_groups = app.group.get_group_list()
#     index = randrange(len(old_groups))
#     group = Group(name="nowaNazwaGrupy")
#     group.group_id = old_groups[index].group_id
#     app.group.modify_group_by_index(index, group)
#     assert len(old_groups) == app.group.count()
#     new_groups = app.group.get_group_list()
#     old_groups[index] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
