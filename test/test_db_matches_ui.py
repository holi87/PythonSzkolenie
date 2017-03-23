from model.group import Group
from timeit import timeit
__author__ = "Grzegorz Holak"


def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    # print(timeit(lambda: app.group.get_group_list(), number=1))

    def clean(group):
        return Group(group_id=group.group_id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())
    # print(timeit(lambda: map(clean, db.get_group_list()), number=1000))
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
