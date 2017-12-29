'''
Created on 13 nov 2013

Remodeled on 29 dec 2017

@author: Yoieh
'''

from universe_sql.universe_db import SQLUniverseDatabase

__version__ = '0.0.1'

class SQLGalaxy(object):
    """ Galaxys """

    def __init__(self):
        self.sql_universe_database = SQLUniverseDatabase()
        self.galaxy_id_db = None
        self.galaxys_db = None
        self.galaxy_name_db = None

    def create_galaxys(self):
        """ Creates galaxys table """
        try:
            self.sql_universe_database.cursor.execute(
                """CREATE TABLE galaxys (
                                  id_galaxy INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                                  name_galaxy VARCHAR(100),
                                  maxy_galaxy INT(100),
                                  maxx_galaxy INT(100)
                                );"""
            )
            print "Created table: galaxys"
        except:
            print "Table do already exist: galaxys"

    def insert_galaxy(self, name_galaxy, max_y_galaxy, max_x_galaxy):
        """ Creates universee from name_galaxy, max_y_galaxy and max_x_galaxy"""

        self.select_galaxy_with_name(name_galaxy)
        if self.galaxy_name_db is None:
            self.sql_universe_database.cursor.execute(
                """INSERT INTO galaxys (name_galaxy , maxy_galaxy, maxx_galaxy)
                                      VALUES (%s, %s, %s)""",
                (str(name_galaxy), str(max_y_galaxy), str(max_x_galaxy))
            )
            self.sql_universe_database.sql_connect.commit()
            print "New Galaxy Created Called: " + str(name_galaxy)
        else:
            print "Galaxy do already exist"

    def select_galaxy_with_id(self, id_galaxy):
        """ Selects galaxy with id_galaxy """

        try:
            self.sql_universe_database.cursor.execute(
                "SELECT * FROM galaxys WHERE id_galaxy='" + str(id_galaxy) + "'")
            self.galaxy_id_db = self.sql_universe_database.cursor.fetchone()
            print "Selected * from row with id: " + str(id_galaxy)
            return self.galaxy_id_db
        except:
            print "Row dose'nt exist with id: " + str(id_galaxy)

    def select_galaxy_with_name(self, name_galaxy):
        """ Selects galaxy with name_galaxy """

        try:
            self.sql_universe_database.cursor.execute(
                "SELECT * FROM galaxys WHERE name_galaxy='" + str(name_galaxy) + "'")
            self.galaxy_name_db = self.sql_universe_database.cursor.fetchone()
            print "Selected * from row with name: " + str(name_galaxy)
            return self.galaxy_name_db
        except:
            print "Row dose'nt exist with name: " + str(name_galaxy)
            self.galaxy_name_db = None
            return self.galaxy_name_db

    def select_galaxys(self):
        """ Selects all galaxys """
        self.sql_universe_database.cursor.execute("SELECT * FROM galaxys")
        self.galaxys_db = [
            element for element in self.sql_universe_database.cursor.fetchall()]
        return self.galaxys_db
