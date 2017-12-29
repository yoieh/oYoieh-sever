'''
Created on 13 nov 2013

Remodeled on 29 dec 2017

@author: Yoieh
'''

from universe_sql.universe_db import SQLUniverseDatabase

__version__ = '0.0.1'

class SQLSpaceEntityPlot(object):
    """ Space entity plots """

    def __init__(self):
        self.sql_universe_database = SQLUniverseDatabase()
        self.spaceentity_db = None
        self.spaceentitys_plots_db = None

    def create_spaceentity_plots(self, name_spaceentity):
        """ Creates space entity plots name_spaceentity """

        try:
            self.sql_universe_database.cursor.execute(
                """CREATE TABLE spaceentityplots_""" + name_spaceentity + """ (
                              id_plot INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                              id_spaceentity INT(100),
                              y_spaceentity INT(100),
                              x_spaceentity INT(100),
                              nosise_spaceentity INT(100),
                              name_spaceentity VARCHAR(100),
                              id_plottype INT(100)
                            );"""
            )
            print "Created table: spaceentityplots_" + name_spaceentity
        except:
            pass

    def insert_spaceentity_plots(self, name_spaceentity, sql_spaceentity):
        """ Creates space entity plots """

        for sql_row in sql_spaceentity:
            self.sql_universe_database.cursor.executemany(
                """INSERT INTO spaceentityplots_""" + str(name_spaceentity) + """(
                                          id_spaceentity,
                                          y_spaceentity,
                                          x_spaceentity,
                                          nosise_spaceentity,
                                          id_plottype
                                          )
                                            VALUES (%s, %s, %s, %s, %s)""",

                (sql_row)
            )
            self.sql_universe_database.sql_connect.commit()

    def select_spaceentity_plot_with_id(self, id_spaceentityplot, name_spaceentity):
        """ Selects space entity plot with id_spaceentityplot and name_spaceentity """

        try:
            self.sql_universe_database.cursor.execute("SELECT * FROM spaceentityplots_" + str(
                name_spaceentity) + " WHERE id_plot=" + str(id_spaceentityplot))
            self.spaceentity_db = self.sql_universe_database.cursor.fetchone()
            print "Selected * from row with id: " + str(id_spaceentityplot)
            return self.spaceentity_db
        except:
            print "Row dose'nt exist with id: " + str(id_spaceentityplot)

    def select_spaceentitys_plots(self, name_spaceentity):
        """ Selects all spalce emtity plots """

        self.sql_universe_database.cursor.execute(
            "SELECT * FROM spaceentityplots_" + str(name_spaceentity))
        self.spaceentitys_plots_db = [
            element for element in self.sql_universe_database.cursor.fetchall()]
        return self.spaceentitys_plots_db
