__author__ = "Grzegorz Holak"


def test_delete_first_group(app):
    app.group.delete_first_group()
