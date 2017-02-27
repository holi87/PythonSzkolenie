from model.group import Group
__author__ = "Grzegorz Holak"


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="nowaNazwaHeader"))


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="nowaNazwaGrupy"))

