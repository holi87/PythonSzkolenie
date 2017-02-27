from model.group import Group
__author__ = "Grzegorz Holak"


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="nowaNazwaGrupy", header="nowaNazwaHeader"
                                       , footer="nowaNazwaFooter"))
    app.session.logout()
