from model.contact import Contact
from random import randrange

__author__ = "Grzegorz Holak"


def test_phones_on_home_page(app):
    # when there is no contact - make one for test
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="jakies losowe", last_name="nazwisko siakie", home_phone="12411+1"
                                   , mobile_phone="1241241"))
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == app.\
        contact.merge_phones_like_on_home_page(contact_from_edit_page)


# from video - not for task 14
# def test_phones_on_contact_view_page(app):
#     contact_from_view_page = app.contact.get_contact_from_view_page(0)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
#     assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
#     assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
#     assert contact_from_view_page.home_phone2 == contact_from_edit_page.home_phone2







