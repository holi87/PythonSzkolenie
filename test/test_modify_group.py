from model.group import Group
from random import randrange
__author__ = "Grzegorz Holak"


def test_modify_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="nazwa"))

    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))

    group = Group(name="nowaNazwaGrupy", header="blablabla", footer="trubadur")
    group.group_id = old_groups[index].group_id

    app.group.modify_group_by_index(index, group)

    assert len(old_groups) == app.group.count()

    new_groups = app.group.get_group_list()
    old_groups[index] = group

    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_some_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="nazwa"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="nowaNazwaGrupy")
    group.group_id = old_groups[index].group_id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
