'''
Created on 13 nov 2013

Remodeled on 29 dec 2017

@author: Yoieh
'''

from universe_sql.universe_db import SQLUniverseDatabase

__version__ = '0.0.1'

class SQLSolarSystem(object):
    """ Solar system """

    def __init__(self):
        self.sql_universe_database = SQLUniverseDatabase()
        self.solarsystem_id_db = None
        self.solarsystem_name_db = None
        self.solarsystem_db = None

    def create_solarsystems(self):
        """ Creates solarsystem table """
        try:
            self.sql_universe_database.cursor.execute(
                """CREATE TABLE solarsystems (
                                  id_solarsystem INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                                  name_solarsystem VARCHAR(100),
                                  maxy_solarsystem INT(100),
                                  maxx_solarsystem INT(100)
                                );"""
            )
            print "Created table: solarsystems"
        except:
            pass

    def insert_solarsystem(self, name_solarsystem, max_y_solarsystem, max_x_solarsystem):
        """ Creates solasustem with name_solarsystem,
            max_y_solarsystem and max_x_solarsystem """

        self.select_solarsystem_with_name(name_solarsystem)
        if self.solarsystem_name_db is None:
            self.sql_universe_database.cursor.execute(
                """INSERT INTO solarsystems (name_solarsystem , maxy_solarsystem, maxx_solarsystem)
                                      VALUES (%s, %s, %s)""",
                (str(name_solarsystem), str(max_y_solarsystem), str(max_x_solarsystem))
            )
            self.sql_universe_database.sql_connect.commit()
            print "New Solarsystem Created Called: " + str(name_solarsystem)
        else:
            print "Solarsystem do already exist"

    def select_solarsystem_with_id(self, id_solarsystem):
        """ Selects solarsystem with id_solarsystem """

        try:
            self.sql_universe_database.cursor.execute(
                "SELECT * FROM solarsystems WHERE id_solarsystem=" + str(id_solarsystem))
            self.solarsystem_id_db = self.sql_universe_database.cursor.fetchone()
            print "Selected * from row with id: " + str(id_solarsystem)
            return self.solarsystem_id_db
        except:
            print "Row dose'nt exist with id: " + str(id_solarsystem)

    def select_solarsystem_with_name(self, name_solarsystem):
        """ Selects solarsystem with name_solarsystem """

        try:
            self.sql_universe_database.cursor.execute(
                "SELECT * FROM solarsystems WHERE name_solarsystem='" +
                str(name_solarsystem) + "'")
            self.solarsystem_name_db = self.sql_universe_database.cursor.fetchone()
            print "Selected * from row with name: " + str(name_solarsystem)
            return self.solarsystem_name_db
        except:
            print "Row dose'nt exist with name: " + str(name_solarsystem)
            self.solarsystem_name_db = None
            return self.solarsystem_name_db

    def select_solar_systems(self):
        """ Selects all solarsytems """
        self.sql_universe_database.cursor.execute("SELECT * FROM solarsystems")
        self.solarsystem_db = [
            element for element in self.sql_universe_database.cursor.fetchall()]
        return self.solarsystem_db
