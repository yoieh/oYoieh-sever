'''
Created on 13 nov 2013

Remodeled on 29 dec 2017

@author: Yoieh
'''

from universe_sql.universe_db import SQLUniverseDatabase

__version__ = '0.0.1'

class SQLUniverse(object):
    """ Universe """

    def __init__(self):
        self.sql_universe_database = SQLUniverseDatabase()
        self.universe_id_db = None
        self.universe_name_db = None
        self.universe_db = None

    def create_universe(self):
        """ Creates universe table """
        try:
            self.sql_universe_database.cursor.execute(
                """CREATE TABLE universe (
                                  id_universe INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                                  name_universe VARCHAR(100),
                                  maxy_universe INT(100),
                                  maxx_universe INT(100)
                                );"""
            )
            print "Created table: universe"
        except:
            pass

    def insert_universe(self, name_universe, max_y_universe, max_x_universe):
        """ Creates universe """

        self.select_universe_with_name(name_universe)
        if self.universe_name_db is None:
            self.sql_universe_database.cursor.execute(
                """INSERT INTO universe (name_universe , maxy_universe, maxx_universe)
                                      VALUES (%s, %s, %s)""",
                (str(name_universe), str(max_y_universe), str(max_x_universe))
            )
            self.sql_universe_database.sql_connect.commit()
            print "New universe Created Called: " + str(name_universe)
        else:
            print "universe do already exist"

    def select_universe_with_id(self, id_universe):
        """ Selects universe with id_universe """

        try:
            self.sql_universe_database.cursor.execute(
                "SELECT * FROM universe WHERE id_universe='" + str(id_universe) + "'")
            self.universe_id_db = self.sql_universe_database.cursor.fetchone()
            print "Selected * from row with id: " + str(id_universe)
            return self.universe_id_db
        except:
            print "Row dose'nt exist with id: " + str(id_universe)

    def select_universe_with_name(self, name_universe):
        """ Selects universe with name_universe """

        try:
            self.sql_universe_database.cursor.execute(
                "SELECT * FROM universe WHERE name_universe='" + str(name_universe) + "'")
            self.universe_name_db = self.sql_universe_database.cursor.fetchone()
            print "Selected * from row with name: " + str(name_universe)
            return self.universe_name_db
        except:
            print "Row dose'nt exist with name: " + str(name_universe)
            self.universe_name_db = None
            return self.universe_name_db

    def select_universe(self):
        """ Selects all universes """

        self.sql_universe_database.cursor.execute("SELECT * FROM universe")
        self.universe_db = [
            element for element in self.sql_universe_database.cursor.fetchall()]
        return self.universe_db

    def update_universe(self):
        """ Noting """
        pass
        