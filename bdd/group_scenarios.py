from pytest_bdd import scenario
from .groups_steps import *
__author__ = "Grzegorz Holak"


@scenario('groups.feature', 'Add new group')
def test_add_new_group():
    pass


@scenario('groups.feature', 'Delete a group')
def test_delete_group():
    pass