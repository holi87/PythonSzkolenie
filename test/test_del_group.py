from model.group import Group
__author__ = "Grzegorz Holak"


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="nazwa"))
    app.group.delete_first_group()
