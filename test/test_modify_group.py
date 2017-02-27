from model.group import Group
__author__ = "Grzegorz Holak"


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="nazwaxxx"))
    app.group.modify_first_group(Group(header="nowaNazwaHeader"))


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="nazwa"))
    app.group.modify_first_group(Group(name="nowaNazwaGrupy"))

