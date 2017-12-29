'''
Created on 13 nov 2013

Remodeled on 29 dec 2017

@author: Yoieh
'''

from MySQLdb import connect

__version__ = '0.0.1'

class SQLUniverseDatabase(object):
    """ universee database """

    def __init__(self):
        try:
            self.sql_connect = connect(
                'localhost', 'root', '', 'universedb')
            print "Connected to Database: universedb"
            self.cursor = self.sql_connect.cursor()
            self.commit = self.sql_connect.commit()
        except:
            print "No Database called: universedb"
            self.creat_universe_db()
            self.__init__(self)

    def creat_universe_db(self):
        """ createds universe db """
        sql_connect = connect('localhost', 'root', '')
        cursor = sql_connect.cursor()
        cursor.execute('CREATE DATABASE universeDB')
