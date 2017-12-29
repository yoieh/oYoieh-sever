'''
Created on 13 nov 2013

Remodeled on 29 dec 2017

@author: Yoieh
'''

from universe_sql.universe_db import SQLUniverseDatabase

__version__ = '0.0.1'

class SQLSpaceEntity(object):
    """ Space Entitys """

    def __init__(self):
        self.sql_universe_database = SQLUniverseDatabase()
        self.spaceentity_name_db = None
        self.spaceentity_id_db = None
        self.spaceentity_db = None

    def create_spaceentitys(self):
        """ Creates space entitys table """
        try:
            self.sql_universe_database.cursor.execute(
                """CREATE TABLE spaceentitys (
                                  id_spaceentitys INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                                  name_spaceentity VARCHAR(100),
                                  maxy_spaceentity INT(100),
                                  maxx_spaceentity INT(100),
                                  id_spaceentitytype INT(100)
                                );"""
            )
            print "Created table: spaceentitys"
        except:
            pass

    def insert_spaceentity(self, name_spaceentity, max_y_spaceentity,
                           max_x_spaceentity, id_spaceentity_typs):
        """ Creates space entity """

        self.select_spaceentity_with_name(name_spaceentity)
        if self.spaceentity_name_db is None:
            self.sql_universe_database.cursor.execute(
                """INSERT INTO spaceentitys (name_spaceentity, maxy_spaceentity,
                maxx_spaceentity, id_spaceentitytype) VALUES (%s, %s, %s, %s)""",
                (str(name_spaceentity), str(max_y_spaceentity),
                 str(max_x_spaceentity), str(id_spaceentity_typs))
            )
            self.sql_universe_database.sql_connect.commit()
            print "New spaceentity Created Called: " + str(name_spaceentity)
        else:
            print "spaceentity do already exist"

    def select_spaceentity_with_id(self, id_spaceentity):
        """ Selects space entity with id_spaceentity """

        try:
            self.sql_universe_database.cursor.execute(
                "SELECT * FROM spaceentitys WHERE id_spaceentity='" + str(id_spaceentity) + "'")
            self.spaceentity_id_db = self.sql_universe_database.cursor.fetchone()
            print "Selected * from row with id: " + str(id_spaceentity)
            return self.spaceentity_id_db
        except:
            print "Row dose'nt exist with id: " + str(id_spaceentity)

    def select_spaceentity_with_name(self, name_spaceentity):
        """ Selects space entity with name_spaceentity """

        try:
            self.sql_universe_database.cursor.execute(
                "SELECT * FROM spaceentitys WHERE name_spaceentity='" + str(name_spaceentity) + "'")
            self.spaceentity_name_db = self.sql_universe_database.cursor.fetchone()
            print "Selected * from row with name: " + str(name_spaceentity)
            return self.spaceentity_name_db
        except:
            print "Row dose'nt exist with name: " + str(name_spaceentity)
            self.spaceentity_name_db = None
            return self.spaceentity_name_db

    def select_spaceentitys(self):
        """ Selects all space entitys """

        self.sql_universe_database.cursor.execute("SELECT * FROM spaceentitys")
        self.spaceentity_db = [
            element for element in self.sql_universe_database.cursor.fetchall()]
        return self.spaceentity_db
