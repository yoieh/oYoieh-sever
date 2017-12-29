'''
Created on 13 nov 2013

@author: Yoieh
'''

import MySQLdb
from MySQLdb import *


class SQLUniversDatabase():
    def __init__(self):
        try:
            self.sqlConnect = MySQLdb.connect(
                'localhost', 'root', '', 'universdb')
            print "Connected to Database: universdb"
            self.cursor = self.sqlConnect.cursor()
            self.commit = self.sqlConnect.commit()
        except:
            print "No Database called: universdb"
            self.creatUniversDB()
            self.__init__()

    def creatUniversDB(self):
        sqlConnect = MySQLdb.connect('localhost', 'root', '')
        cursor = sqlConnect.cursor()
        cursor.execute('CREATE DATABASE UniversDB')


class SQLUnivers():
    def __init__(self):
        self.SQLUniversDatabase = SQLUniversDatabase()

    def createUnivers(self):
        try:
            self.SQLUniversDatabase.cursor.execute(
                """CREATE TABLE univers (
                                  id_univers INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                                  name_univers VARCHAR(100),
                                  maxy_univers INT(100),
                                  maxx_univers INT(100)
                                );"""
            )
            print "Created table: univers"
        except:
            pass

    def insertUnivers(self, nameUnivers, max_yUnivers, max_xUnivers):
        self.selectUniversWith_name(nameUnivers)
        if self.universNameDB == None:
            self.SQLUniversDatabase.cursor.execute(
                """INSERT INTO univers (name_univers , maxy_univers, maxx_univers)
                                      VALUES (%s, %s, %s)""",
                (str(nameUnivers), str(max_yUnivers), str(max_xUnivers))
            )
            self.SQLUniversDatabase.sqlConnect.commit()
            print "New Univers Created Called: " + str(nameUnivers)
        else:
            print "Univers do already exist"

    def selectUniversWith_id(self, idUnivers):
        try:
            self.SQLUniversDatabase.cursor.execute(
                "SELECT * FROM univers WHERE id_univers='" + str(idUnivers) + "'")
            self.universIdDB = self.SQLUniversDatabase.cursor.fetchone()
            return self.universIdDB
            print "Selected * from row with id: " + str(idUnivers)
        except:
            print "Row dose'nt exist with id: " + str(idUnivers)

    def selectUniversWith_name(self, nameUnivers):
        try:
            self.SQLUniversDatabase.cursor.execute(
                "SELECT * FROM univers WHERE name_univers='" + str(nameUnivers) + "'")
            self.universNameDB = self.SQLUniversDatabase.cursor.fetchone()
            return self.universNameDB
            print "Selected * from row with name: " + str(nameUnivers)
        except:
            print "Row dose'nt exist with name: " + str(nameUnivers)
            self.universNameDB = None
            return self.universNameDB

    def selectUnivers(self):
        self.SQLUniversDatabase.cursor.execute("SELECT * FROM univers")
        self.universDB = [
            element for element in self.SQLUniversDatabase.cursor.fetchall()]
        return self.universDB

    def updateUser(self):
        pass


class SQLUniversPlots():
    def __init__(self):
        self.SQLUniversDatabase = SQLUniversDatabase()

    def createUniversPlots(self, nameUnivers):
        try:
            self.SQLUniversDatabase.cursor.execute(
                """CREATE TABLE universplots_""" + str(nameUnivers) + """ (
                              id_galaxy INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                              id_univers INT(100),
                              y_univers INT(100),
                              x_univers INT(100),
                              nosise_univers INT(100)
                            );"""
            )
            print "Created table: universplots"
        except:
            pass

    def insertUniversPlots(self, nameUnivers, sql_Univers):
        for sql_row in sql_Univers:
            self.SQLUniversDatabase.cursor.executemany(
                """INSERT INTO universplots_""" + str(nameUnivers) + """(
                                          id_univers,
                                          y_univers,
                                          x_univers,
                                          nosise_univers)
                                            VALUES (%s, %s, %s, %s)""",

                (sql_row)
            )
            self.SQLUniversDatabase.sqlConnect.commit()

    def selectUniversPlotWith_id(self, idUniversplot, nameUnivers):
        try:
            self.SQLUniversDatabase.cursor.execute("SELECT * FROM universplots_'" + str(
                nameUnivers) + "' WHERE id_galaxy='" + str(idUniversplot) + "'")
            self.UniversPlotIdDB = self.SQLUniversDatabase.cursor.fetchone()
            return self.UniversPlotIdDB
            print "Selected * from row with id: " + str(idUniversplot)
        except:
            print "Row dose'nt exist with id: " + str(idUniversplot)

    def selectUniversPlots(self, nameUnivers):
        self.SQLUniversDatabase.cursor.execute(
            "SELECT * FROM universplots_" + str(nameUnivers))
        self.UniversPlotsDB = [
            element for element in self.SQLUniversDatabase.cursor.fetchall()]
        return self.UniversPlotsDB


class SQLGalaxys():
    def __init__(self):
        self.SQLUniversDatabase = SQLUniversDatabase()

    def createGalaxys(self):
        try:
            self.SQLUniversDatabase.cursor.execute(
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

    def insertGalaxy(self, nameGalaxy, max_yGalaxy, max_xGalaxy):
        self.selectGalaxyWith_name(nameGalaxy)
        if self.galaxyNameDB == None:
            self.SQLUniversDatabase.cursor.execute(
                """INSERT INTO galaxys (name_galaxy , maxy_galaxy, maxx_galaxy)
                                      VALUES (%s, %s, %s)""",
                (str(nameGalaxy), str(max_yGalaxy), str(max_xGalaxy))
            )
            self.SQLUniversDatabase.sqlConnect.commit()
            print "New Galaxy Created Called: " + str(nameGalaxy)
        else:
            print "Galaxy do already exist"

    def selectGalaxyWith_id(self, idGalaxy):
        try:
            self.SQLUniversDatabase.cursor.execute(
                "SELECT * FROM galaxys WHERE id_galaxy='" + str(idGalaxy) + "'")
            self.galaxyIdDB = self.SQLUniversDatabase.cursor.fetchone()
            return self.galaxyIdDB
            print "Selected * from row with id: " + str(idGalaxy)
        except:
            print "Row dose'nt exist with id: " + str(idGalaxy)

    def selectGalaxyWith_name(self, nameGalaxy):
        try:
            self.SQLUniversDatabase.cursor.execute(
                "SELECT * FROM galaxys WHERE name_galaxy='" + str(nameGalaxy) + "'")
            self.galaxyNameDB = self.SQLUniversDatabase.cursor.fetchone()
            return self.galaxyNameDB
            print "Selected * from row with name: " + str(nameGalaxy)
        except:
            print "Row dose'nt exist with name: " + str(nameGalaxy)
            self.galaxyNameDB = None
            return self.galaxyNameDB

    def selectGalaxys(self):
        self.SQLUniversDatabase.cursor.execute("SELECT * FROM galaxys")
        self.galaxysDB = [
            element for element in self.SQLUniversDatabase.cursor.fetchall()]
        return self.galaxysDB


class SQLGalaxyPlots():
    def __init__(self):
        self.SQLUniversDatabase = SQLUniversDatabase()

    def createGalaxyPlots(self, nameGalaxy):
        try:
            self.SQLUniversDatabase.cursor.execute(
                """CREATE TABLE galaxyplots_""" + str(nameGalaxy) + """ (
                              id_solarsystem INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                              id_galaxy INT(100),
                              y_galaxy INT(100),
                              x_galaxy INT(100),
                              nosise_galaxy INT(100)
                            );"""
            )
            print "Created table: galaxyplots"
        except:
            print "Couldn't created table: galaxyplots"

    def insertGalaxyPlots(self, nameGalaxy, sql_Galaxy):
        for sql_row in sql_Galaxy:
            self.SQLUniversDatabase.cursor.executemany(
                """INSERT INTO galaxyplots_""" + str(nameGalaxy) + """(
                                          id_galaxy,
                                          y_galaxy,
                                          x_galaxy,
                                          nosise_galaxy
                                          )
                                            VALUES (%s, %s, %s, %s)""",

                (sql_row)
            )
            self.SQLUniversDatabase.sqlConnect.commit()

    def selectGalaxyPlotWith_id(self, idGalaxyplot, nameGalaxy):
        try:
            self.SQLUniversDatabase.cursor.execute(
                "SELECT * FROM galaxyplots_" + str(nameGalaxy) + " WHERE id_galaxy=" + str(idGalaxyplot))
            self.GalaxyPlotIdDB = self.SQLUniversDatabase.cursor.fetchone()
            return self.GalaxyPlotIdDB
            print "Selected * from row with id: " + str(idGalaxyplot)
        except:
            print "Row dose'nt exist with id: " + str(idGalaxyplot)

    def selectGalaxyPlots(self, nameGalaxy):
        self.SQLUniversDatabase.cursor.execute(
            "SELECT * FROM galaxyplots_" + str(nameGalaxy))
        self.GalaxysPlotsDB = [
            element for element in self.SQLUniversDatabase.cursor.fetchall()]
        return self.GalaxysPlotsDB


class SQLSolarSystems():
    def __init__(self):
        self.SQLUniversDatabase = SQLUniversDatabase()

    def createSolarSystems(self):
        try:
            self.SQLUniversDatabase.cursor.execute(
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

    def insertSolarSystem(self, nameSolarSystem, max_ySolarSystem, max_xSolarSystem):
        self.selectSolarSystemWith_name(nameSolarSystem)
        if self.solarsystemNameDB == None:
            self.SQLUniversDatabase.cursor.execute(
                """INSERT INTO solarsystems (name_solarsystem , maxy_solarsystem, maxx_solarsystem)
                                      VALUES (%s, %s, %s)""",
                (str(nameSolarSystem), str(max_ySolarSystem), str(max_xSolarSystem))
            )
            self.SQLUniversDatabase.sqlConnect.commit()
            print "New Solarsystem Created Called: " + str(nameSolarSystem)
        else:
            print "Solarsystem do already exist"

    def selectSolarSystemWith_id(self, idSolarSystem):
        try:
            self.SQLUniversDatabase.cursor.execute(
                "SELECT * FROM solarsystems WHERE id_solarsystem=" + str(idSolarSystem))
            self.universIdDB = self.SQLUniversDatabase.cursor.fetchone()
            return self.SolarSystemIdDB
            print "Selected * from row with id: " + str(idSolarSystem)
        except:
            print "Row dose'nt exist with id: " + str(idSolarSystem)

    def selectSolarSystemWith_name(self, nameSolarSystem):
        try:
            self.SQLUniversDatabase.cursor.execute(
                "SELECT * FROM solarsystems WHERE name_solarsystem='" + str(nameSolarSystem) + "'")
            self.solarsystemNameDB = self.SQLUniversDatabase.cursor.fetchone()
            return self.solarsystemNameDB
            print "Selected * from row with name: " + str(nameSolarSystem)
        except:
            print "Row dose'nt exist with name: " + str(nameSolarSystem)
            self.solarsystemNameDB = None
            return self.solarsystemNameDB

    def selectSolarSystems(self):
        self.SQLUniversDatabase.cursor.execute("SELECT * FROM solarsystems")
        self.SolarSystemDB = [
            element for element in self.SQLUniversDatabase.cursor.fetchall()]
        return self.SolarSystemDB


class SQLSolarSystemPlots():
    def __init__(self):
        self.SQLUniversDatabase = SQLUniversDatabase()

    def createSolarSystemPlots(self, nameSolarSystem):
        try:
            self.SQLUniversDatabase.cursor.execute(
                """CREATE TABLE solarsystemplots_""" + str(nameSolarSystem) + """ (
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

    def insertSolarSystemPlots(self, nameSolarSystem, sql_SolarSystem):
        for sql_row in sql_SolarSystem:
            self.SQLUniversDatabase.cursor.executemany(
                """INSERT INTO solarsystemplots_""" + str(nameSolarSystem) + """(
                                          id_solarsystem,
                                          y_solarsystem,
                                          x_solarsystem,
                                          nosise_solarsystem
                                          )
                                            VALUES (%s, %s, %s, %s)""",

                (sql_row)
            )
            self.SQLUniversDatabase.sqlConnect.commit()

    def selectSolarSystemPlotWith_id(self, idSolarSystemplot, nameSolarSystem):
        try:
            self.SQLUniversDatabase.cursor.execute("SELECT * FROM solarsystemplots_" + str(
                nameSolarSystem) + " WHERE id_galaxy=" + str(idSolarSystemplot))
            self.SolarSystemPlotIdDB = self.SQLUniversDatabase.cursor.fetchone()
            return self.SolarSystemPlotIdDB
            print "Selected * from row with id: " + str(idSolarSystemplot)
        except:
            print "Row dose'nt exist with id: " + str(idSolarSystemplot)

    def selectSolarSystemPlots(self, nameSolarSystem):
        self.SQLUniversDatabase.cursor.execute(
            "SELECT * FROM solarsystemplots_" + str(nameSolarSystem))
        self.SolarSystemsPlotsDB = [
            element for element in self.SQLUniversDatabase.cursor.fetchall()]
        return self.SolarSystemsPlotsDB


class SQLSpaceEntitys():
    def __init__(self):
        self.SQLUniversDatabase = SQLUniversDatabase()

    def createSpaceEntitys(self):
        try:
            self.SQLUniversDatabase.cursor.execute(
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

    def insertSpaceEntity(self, nameSpaceEntity, max_ySpaceEntity, max_xSpaceEntity, idSpaceEntityTyps):
        self.selectSpaceEntityWith_name(nameSpaceEntity)
        if self.spaceentityNameDB == None:
            self.SQLUniversDatabase.cursor.execute(
                """INSERT INTO spaceentitys (name_spaceentity, maxy_spaceentity, maxx_spaceentity, id_spaceentitytype)
                                      VALUES (%s, %s, %s, %s)""",
                (str(nameSpaceEntity), str(max_ySpaceEntity),
                 str(max_xSpaceEntity), str(idSpaceEntityTyps))
            )
            self.SQLUniversDatabase.sqlConnect.commit()
            print "New spaceentity Created Called: " + str(nameSpaceEntity)
        else:
            print "spaceentity do already exist"

    def selectSpaceEntityWith_id(self, idSpaceEntity):
        try:
            self.SQLUniversDatabase.cursor.execute(
                "SELECT * FROM spaceentitys WHERE id_spaceentity='" + str(idSpaceEntity) + "'")
            self.apaceentityIdDB = self.SQLUniversDatabase.cursor.fetchone()
            return self.SpaceEntityIdDB
            print "Selected * from row with id: " + str(idSpaceEntity)
        except:
            print "Row dose'nt exist with id: " + str(idSpaceEntity)

    def selectSpaceEntityWith_name(self, nameSpaceEntity):
        try:
            self.SQLUniversDatabase.cursor.execute(
                "SELECT * FROM spaceentitys WHERE name_spaceentity='" + str(nameSpaceEntity) + "'")
            self.spaceentityNameDB = self.SQLUniversDatabase.cursor.fetchone()
            return self.spaceentityNameDB
            print "Selected * from row with name: " + str(nameSpaceEntity)
        except:
            print "Row dose'nt exist with name: " + str(nameSpaceEntity)
            self.spaceentityNameDB = None
            return self.spaceentityNameDB

    def selectSpaceEntitys(self):
        self.SQLUniversDatabase.cursor.execute("SELECT * FROM spaceentitys")
        self.SpaceEntityDB = [
            element for element in self.SQLUniversDatabase.cursor.fetchall()]
        return self.SpaceEntityDB


class SQLSpaceEntityPlots():
    def __init__(self):
        self.SQLUniversDatabase = SQLUniversDatabase()

    def createSpaceEntityPlots(self, nameSpaceEntity):
        try:
            self.SQLUniversDatabase.cursor.execute(
                """CREATE TABLE spaceentityplots_""" + nameSpaceEntity + """ (
                              id_plot INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                              id_spaceentity INT(100),
                              y_spaceentity INT(100),
                              x_spaceentity INT(100),
                              nosise_spaceentity INT(100),
                              name_spaceentity VARCHAR(100),
                              id_plottype INT(100)
                            );"""
            )
            print "Created table: spaceentityplots_" + nameSpaceEntity
        except:
            pass

    def insertSpaceEntityPlots(self, nameSpaceEntity, sql_SpaceEntity):
        for sql_row in sql_SpaceEntity:
            self.SQLUniversDatabase.cursor.executemany(
                """INSERT INTO spaceentityplots_""" + str(nameSpaceEntity) + """(
                                          id_spaceentity,
                                          y_spaceentity,
                                          x_spaceentity,
                                          nosise_spaceentity,
                                          id_plottype
                                          )
                                            VALUES (%s, %s, %s, %s, %s)""",

                (sql_row)
            )
            self.SQLUniversDatabase.sqlConnect.commit()

    def selectSpaceEntityPlotWith_id(self, idSpaceEntityplot, nameSpaceEntity):
        try:
            self.SQLUniversDatabase.cursor.execute("SELECT * FROM spaceentityplots_" + str(
                nameSpaceEntity) + " WHERE id_plot=" + str(idSpaceEntityplot))
            self.SpaceEntityDB = self.SQLUniversDatabase.cursor.fetchone()
            return self.SolarSystemPlotIdDB
            print "Selected * from row with id: " + str(idSpaceEntityplot)
        except:
            print "Row dose'nt exist with id: " + str(idSpaceEntityplot)

    def selectSpaceEntitysPlots(self, nameSpaceEntity):
        self.SQLUniversDatabase.cursor.execute(
            "SELECT * FROM spaceentityplots_" + str(nameSpaceEntity))
        self.SpaceEntitysPlotsDB = [
            element for element in self.SQLUniversDatabase.cursor.fetchall()]
        return self.SpaceEntitysPlotsDB


class SQLTilePlots():
    def __init__(self):
        self.SQLUniversDatabase = SQLUniversDatabase()

    def createTilePlots(self, nameSpaceEntity):
        try:
            self.SQLUniversDatabase.cursor.execute(
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

    def insertSpaceEntityPlots(self, nameSpaceEntity, sql_SpaceEntity):
        for sql_row in sql_SpaceEntity:
            self.SQLUniversDatabase.cursor.executemany(
                """INSERT INTO spaceentityplots_""" + str(nameSpaceEntity) + """(
                                          id_spaceentity,
                                          y_spaceentity,
                                          x_spaceentity,
                                          nosise_spaceentity
                                          )
                                            VALUES (%s, %s, %s, %s , )""",

                (sql_row)
            )
            self.SQLUniversDatabase.sqlConnect.commit()

    def selectTilePlotWith_id(self, idplot):
        try:
            self.SQLUniversDatabase.cursor.execute(
                "SELECT * FROM tileplots WHERE id_tile='" + str(idplot) + "'")
            self.TilePlotIdDB = self.SQLUniversDatabase.cursor.fetchone()
            return self.TilePlotIdDB
            print "Selected * from row with id: " + str(idplot)
        except:
            print "Row dose'nt exist with id: " + str(idplot)

    def selectTilesPlots(self):
        self.SQLUniversDatabase.cursor.execute("SELECT * FROM tileplots")
        self.TilesPlotsDB = [
            element for element in self.SQLUniversDatabase.cursor.fetchall()]
        return self.TilesPlotsDB


class SpaceEntityTyps():
    def __init__(self):
        self.SQLUniversDatabase = SQLUniversDatabase()

    def createSpaceEntityTyps(self, nameSpaceEntity):
        try:
            self.SQLUniversDatabase.cursor.execute(
                """CREATE TABLE spaceentitytyps (
                              id_spaceentitytyp INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                              name_spaceentitytyp VARCHAR(100),
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

    def insertSpaceEntityTyp(self, nameSpaceEntityTyp, max_ySpaceEntityTyp, max_xSpaceEntityTyp, min_ySpaceEntityTyp, min_xSpaceEntityTyp, id_resourcesSpaceEntityTyp):

        self.SQLUniversDatabase.cursor.execute(
            """INSERT INTO spaceentitytyps(
                            name_spaceentitytyp,
                            name_world,
                            max_y,
                            max_x,
                            min_x,
                            min_x,
                            id_resources
                            name_world,
                            )
                            VALUES (%s, %s, %s, %s, %s, %s, %s)""",
            (str(nameSpaceEntityTyp), str(max_ySpaceEntityTyp), str(
                min_ySpaceEntityTyp), str(min_xSpaceEntityTyp), str(id_resourcesSpaceEntityTyp))
        )
        self.SQLUniversDatabase.sqlConnect.commit()
        print "Inserted row: " + str(nameSpaceEntityTyp)

    def selectSpaceEntityTypWith_id(self, idSpaceEntityTyp):
        try:
            self.SQLUniversDatabase.cursor.execute(
                "SELECT * FROM spaceentitytyps WHERE id_tile='" + str(idSpaceEntityTyp) + "'")
            self.SpaceEntityIdDB = self.SQLUniversDatabase.cursor.fetchone()
            return self.SpaceEntityIdDB
            print "Selected * from row with id: " + str(self.SpaceEntityIdDB[0])
        except:
            print "Row dose'nt exist with id: " + str(idSpaceEntityTyp)

    def selectSpaceEntityTyps(self):
        self.SQLUniversDatabase.cursor.execute("SELECT * FROM spaceentitytyps")
        self.SpaceEntityTypsDB = [
            element for element in self.SQLUniversDatabase.cursor.fetchall()]
        return self.SpaceEntityTypsDB
