import fixture.basic
__author__ = "Grzegorz Holak"


class GroupHelper(fixture.basic.BasicHelper):

    def __init__(self, app):
        super(GroupHelper, self).__init__(app)

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("grupy").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        wd.find_element_by_name("submit").click()
        self.open_groups_page()  # as return to groups page

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        self.open_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        # open group page
        self.open_groups_page()
        # init group modify
        self.select_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        # submit group creation
        wd.find_element_by_name("update").click()
        self.open_groups_page()  # as return to groups page

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))
