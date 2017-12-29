'''
Created on 13 nov 2013

Remodeled on 29 dec 2017

@author: Yoieh
'''

from universe_sql.universe_db import SQLUniverseDatabase

__version__ = '0.0.1'


class SQLUniversePlot(object):
    """ universe plots """

    def __init__(self):
        self.sql_universe_database = SQLUniverseDatabase()
        self.universe_plot_id_db = None
        self.universe_plots_db = None

    def create_universe_plots(self, name_universe):
        """ Creates universe plots table from name_universe """
        try:
            self.sql_universe_database.cursor.execute(
                """CREATE TABLE universeplots_""" + str(name_universe) + """ (
                              id_galaxy INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                              id_universe INT(100),
                              y_universe INT(100),
                              x_universe INT(100),
                              nosise_universe INT(100)
                            );"""
            )
            print "Created table: universeplots"
        except:
            pass

    def insert_universe_plots(self, name_universe, sql_universe):
        """ Creates universee plots from name_universe"""

        for sql_row in sql_universe:
            self.sql_universe_database.cursor.executemany(
                """INSERT INTO universeplots_""" + str(name_universe) + """(
                                          id_universe,
                                          y_universe,
                                          x_universe,
                                          nosise_universe)
                                            VALUES (%s, %s, %s, %s)""",

                (sql_row)
            )
            self.sql_universe_database.sql_connect.commit()

    def select_universe_plot_with_id(self, id_universe_plot, name_universe):
        """ Selects universee plot with id_universe_plot and name_universe"""

        try:
            self.sql_universe_database.cursor.execute("SELECT * FROM universeplots_'" + str(
                name_universe) + "' WHERE id_galaxy='" + str(id_universe_plot) + "'")
            self.universe_plot_id_db = self.sql_universe_database.cursor.fetchone()
            print "Selected * from row with id: " + str(id_universe_plot)
            return self.universe_plot_id_db
        except:
            print "Row dose'nt exist with id: " + str(id_universe_plot)

    def select_universe_plots(self, name_universe):
        """ Selects all universe plots """

        self.sql_universe_database.cursor.execute(
            "SELECT * FROM universeplots_" + str(name_universe))
        self.universe_plots_db = [
            element for element in self.sql_universe_database.cursor.fetchall()]
        return self.universe_plots_db
