'''
Created on 13 nov 2013

Remodeled on 29 dec 2017

@author: Yoieh
'''

from universe_sql.universe_db import SQLUniverseDatabase

__version__ = '0.0.1'

class SQLSolarSystemPlot(object):
    """ Solarsystem plot """

    def __init__(self):
        self.sql_universe_database = SQLUniverseDatabase()
        self.solarsystem_plot_id_db = None
        self.solarsystems_plots_db = None

    def create_solarsystem_plots(self, name_solarsystem):
        """ Creates solarsystem plots table """

        try:
            self.sql_universe_database.cursor.execute(
                """CREATE TABLE solarsystemplots_""" + str(name_solarsystem) + """ (
                              id_spaceentity INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                              id_solarsystem INT(100),
                              y_solarsystem INT(100),
                              x_solarsystem INT(100),
                              nosise_solarsystem INT(100)
                            );"""
            )
            print "Created table: solarsystemplots"
        except:
            print "Couldn't created table: solarsystemplots"

    def insert_solarsystem_plots(self, name_solarsystem, sql_solarsystem):
        """ Creates solarsystem plots with name_solarsystem """

        for sql_row in sql_solarsystem:
            self.sql_universe_database.cursor.executemany(
                """INSERT INTO solarsystemplots_""" + str(name_solarsystem) + """(
                                          id_solarsystem,
                                          y_solarsystem,
                                          x_solarsystem,
                                          nosise_solarsystem
                                          )
                                            VALUES (%s, %s, %s, %s)""",

                (sql_row)
            )
            self.sql_universe_database.sql_connect.commit()

    def select_solarsystem_plotwith_id(self, id_solarsystem_plot, name_solarsystem):
        """ Selects solarsytem polts with id_solarsystem_plot, name_solarsystem"""

        try:
            self.sql_universe_database.cursor.execute("SELECT * FROM solarsystemplots_" + str(
                name_solarsystem) + " WHERE id_galaxy=" + str(id_solarsystem_plot))
            self.solarsystem_plot_id_db = self.sql_universe_database.cursor.fetchone()
            print "Selected * from row with id: " + str(id_solarsystem_plot)
            return self.solarsystem_plot_id_db
        except:
            print "Row dose'nt exist with id: " + str(id_solarsystem_plot)

    def select_solarsystem_plots(self, name_solarsystem):
        """ Selects solarsytem plots with name_solarsystem """

        self.sql_universe_database.cursor.execute(
            "SELECT * FROM solarsystemplots_" + str(name_solarsystem))
        self.solarsystems_plots_db = [
            element for element in self.sql_universe_database.cursor.fetchall()]
        return self.solarsystems_plots_db