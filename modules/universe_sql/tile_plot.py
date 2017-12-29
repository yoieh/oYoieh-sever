'''
Created on 13 nov 2013

Remodeled on 29 dec 2017

@author: Yoieh
'''

from universe_sql.universe_db import SQLUniverseDatabase

__version__ = '0.0.1'

class SQLTilePlot(object):
    """ Tile plot """

    def __init__(self):
        self.sql_universe_database = SQLUniverseDatabase()
        self.tile_plot_id_db = None
        self.tiles_plots_db = None

    def create_tile_plots(self):
        """ Creates tile plots table """
        try:
            self.sql_universe_database.cursor.execute(
                """CREATE TABLE tileplots (
                              id_tile INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                              id_plot INT(100),
                              y_tile INT(100),
                              x_tile INT(100),
                              nosise_tile INT(100)
                              id_tileentity INT(100)
                            );"""
            )
            print "Created table: createTilePlots"
        except:
            pass

    def insert_stile_plots(self, name_tile_plot, sql_tile_plot):
        """ Creates tile plots """

        for sql_row in sql_tile_plot:
            self.sql_universe_database.cursor.executemany(
                """INSERT INTO tileplots""" + str(name_tile_plot) + """(
                                          id_plot,
                                          y_tile,
                                          x_tile,
                                          nosise_tile,
                                          id_tileentity
                                          )
                                            VALUES (%s, %s, %s, %s , %s)""",

                (sql_row)
            )
            self.sql_universe_database.sql_connect.commit()

    def select_tile_plot_with_id(self, id_plot):
        """ Selects tile plot """

        try:
            self.sql_universe_database.cursor.execute(
                "SELECT * FROM tileplots WHERE id_tile='" + str(id_plot) + "'")
            self.tile_plot_id_db = self.sql_universe_database.cursor.fetchone()
            print "Selected * from row with id: " + str(id_plot)
            return self.tile_plot_id_db
        except:
            print "Row dose'nt exist with id: " + str(id_plot)

    def select_tiles_plots(self):
        """ Selects all tile plots """

        self.sql_universe_database.cursor.execute("SELECT * FROM tileplots")
        self.tiles_plots_db = [
            element for element in self.sql_universe_database.cursor.fetchall()]
        return self.tiles_plots_db
