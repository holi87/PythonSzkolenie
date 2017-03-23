import pymysql.cursors
from model.group import Group
__author__ = "Grzegorz Holak"


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit(True)

    def get_group_list(self):
        lista = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (g_id, name, header, footer) = row
                lista.append(Group(group_id=str(g_id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return lista

    def destroy(self):
        self.connection.close()
