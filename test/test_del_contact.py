from model.contact import Contact
__author__ = "Grzegorz Holak"


def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="jakies losowe", last_name="nazwisko siakie", email="email@maryna.xt"
                                   , mobile_phone="1241241"))
    app.contact.delete_first_contact()
