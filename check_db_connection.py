from fixture.orm import ORMFixture
from model.group import Group
__author__ = "Grzegorz Holak"

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


try:
    l = db.get_contacts_not_in_group(Group(group_id='57'))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass  # db.destroy()
