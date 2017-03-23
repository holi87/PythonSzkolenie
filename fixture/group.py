import fixture.basic
from model.group import Group


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
        self.group_cache = None

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("delete").click()
        self.open_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, g_id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(g_id)
        wd.find_element_by_name("delete").click()
        self.open_groups_page()
        self.group_cache = None

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, g_id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % g_id).click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_data):
        self.modify_group_by_index(0, new_group_data)

    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        # open group page
        self.open_groups_page()
        # init group modify
        self.select_group_by_index(index)
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        # submit group creation
        wd.find_element_by_name("update").click()
        self.open_groups_page()  # as return to groups page
        self.group_cache = None

    def modify_group_by_id(self, g_id, new_group_data):
        wd = self.app.wd
        # open group page
        self.open_groups_page()
        # init group modify
        self.select_group_by_id(g_id)
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        # submit group creation
        wd.find_element_by_name("update").click()
        self.open_groups_page()  # as return to groups page
        self.group_cache = None

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                group_id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, group_id=group_id))
        return list(self.group_cache)

    def clean(self, group):
        return Group(group_id=group.group_id, name=group.name.strip())
