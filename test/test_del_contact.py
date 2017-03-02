from model.contact import Contact
__author__ = "Grzegorz Holak"


def test_del_first_contact(app):
    # make list for actual contacts
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="jakies losowe", last_name="nazwisko siakie", email="email@maryna.xt"
                                   , mobile_phone="1241241"))
    app.contact.delete_first_contact()
    # make new list for contact after deletion
    new_contacts = app.contact.get_contact_list()
    # first assets - length of lists, new should be shorter exactly by 1
    assert len(new_contacts) == len(old_contacts) - 1
    # cutting from old contact first element
    old_contacts[0:1] = []
    # comparing, now list should be exactly same (logical as made in model.contact override def
    assert old_contacts == new_contacts
