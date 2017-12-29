'''
Created on 13 nov 2013

Remodeled on 29 dec 2017

@author: Yoieh
'''

from universe_sql.universe_db import SQLUniverseDatabase

__version__ = '0.0.1'

class SQLspaceentityType(object):
    """ Space Entity Type """
    def __init__(self):
        self.sql_universe_database = SQLUniverseDatabase()
        self.spaceentity_id_db = None
        self.spaceentity_typs_db = None

    def create_spaceentity_typs(self):
        """" Creates Space Entity Typs table """
        try:
            self.sql_universe_database.cursor.execute(
                """CREATE TABLE spaceentity_typs (
                              id_spaceentity_typ INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                              name_spaceentity_typ VARCHAR(100),
                              max_y INT(100),
                              max_x INT(100),
                              min_x INT(100),
                              min_x INT(100),
                              id_resources INT(100)
                            );"""
            )
            print "Created table: createTilePlots"
        except:
            pass

    def insert_spaceentity_typ(self, name_spaceentity_typ, name_world,
                               max_y_spaceentity_typ, max_x_spaceentity_typ,
                               min_y_spaceentity_typ, min_x_spaceentity_typ,
                               id_resourcesspaceentity_typ):
        """ Creates space entity type """

        self.sql_universe_database.cursor.execute(
            """INSERT INTO spaceentity_typs(
                            name_spaceentity_typ,
                            name_world,
                            max_y,
                            max_x,
                            min_x,
                            min_x,
                            id_resources
                            )
                            VALUES (%s, %s, %s, %s, %s, %s, %s)""",
            (str(name_spaceentity_typ), str(name_world),
             str(max_y_spaceentity_typ), str(max_x_spaceentity_typ),
             str(min_y_spaceentity_typ), str(min_x_spaceentity_typ),
             str(id_resourcesspaceentity_typ))
        )
        self.sql_universe_database.sql_connect.commit()
        print "Inserted row: " + str(name_spaceentity_typ)

    def select_spaceentity_typ_with_id(self, id_spaceentity_typ):
        """ Selects space entity typ with id_spaceentity_typ """
        try:
            self.sql_universe_database.cursor.execute(
                "SELECT * FROM spaceentity_typs WHERE id_tile='" + str(id_spaceentity_typ) + "'")
            self.spaceentity_id_db = self.sql_universe_database.cursor.fetchone()
            return self.spaceentity_id_db
            print "Selected * from row with id: " + str(self.spaceentity_id_db[0])
        except:
            print "Row dose'nt exist with id: " + str(id_spaceentity_typ)

    def selectspaceentity_typs(self):
        """ Select all space entity typs """

        self.sql_universe_database.cursor.execute(
            "SELECT * FROM spaceentity_typs")
        self.spaceentity_typs_db = [
            element for element in self.sql_universe_database.cursor.fetchall()]
        return self.spaceentity_typs_db
