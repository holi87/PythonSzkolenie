from model.group import Group
__author__ = "Grzegorz Holak"


# def test_modify_group_header(app):
#     old_groups = app.group.get_group_list()
#     if app.group.count() == 0:
#         app.group.create(Group(name="nazwaxxx"))
#     app.group.modify_first_group(Group(header="nowaNazwaHeader"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)


def test_modify_group_name(app):
    old_groups = app.group.get_group_list()

    group = Group(name="nowaNazwaGrupy")
    group.group_id = old_groups[0].group_id

    if app.group.count() == 0:
        app.group.create(Group(name="nazwa"))
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
