'''
Created on 19 nov 2013

@author: Yoieh
'''

import UniversSQL
from random import randint


class installServer():
    def install(self):
        hight = 16 * 16
        width = 16 * 16

        nameUnivers = 'Test'
        hightUnivers = hight
        widthUnivers = width

        # Install Univers
        self.SQLUnivers = UniversSQL.SQLUnivers()
        self.SQLUnivers.createUnivers()
        self.SQLUnivers.insertUnivers(nameUnivers, hightUnivers, widthUnivers)

        # Install Plots for Univers
        self.SQLUniversPlots = UniversSQL.SQLUniversPlots()
        self.SQLUniversPlots.createUniversPlots(nameUnivers)
        self.SQLUnivers.selectUniversWith_name(nameUnivers)
        idUnivers = self.SQLUnivers.universNameDB[0]
        nameUnivers = self.SQLUnivers.universNameDB[1]
        hightUnivers = self.SQLUnivers.universNameDB[2]
        widthUnivers = self.SQLUnivers.universNameDB[3]
        sql_Univers = []
        for y in xrange(0, hightUnivers):
            sql_row = []
            for x in xrange(0, widthUnivers):
                colum = []
                colum.append(str(idUnivers))
                colum.append(str(y))
                colum.append(str(x))
                colum.append(str(0))
                sql_row.append(colum)
            sql_Univers.append(sql_row)
        self.SQLUniversPlots.insertUniversPlots(nameUnivers, sql_Univers)

        nameGalaxy = 'Y_' + str(randint(0, hightUnivers)) + \
            'X_' + str(randint(0, widthUnivers))
        hightGalaxy = hight
        widthGalaxy = width

        # Install Galaxy
        self.SQLGalaxys = UniversSQL.SQLGalaxys()
        self.SQLGalaxys.createGalaxys()
        self.SQLGalaxys.insertGalaxy(nameGalaxy, hightGalaxy, widthGalaxy)

        # Install Plots for Galaxy
        self.SQLGalaxyPlots = UniversSQL.SQLGalaxyPlots()
        self.SQLGalaxyPlots.createGalaxyPlots(nameGalaxy)
        self.SQLGalaxys.selectGalaxyWith_name(nameGalaxy)
        idGalaxy = self.SQLGalaxys.galaxyNameDB[0]
        nameGalaxy = self.SQLGalaxys.galaxyNameDB[1]
        hightGalaxy = self.SQLGalaxys.galaxyNameDB[2]
        widthGalaxy = self.SQLGalaxys.galaxyNameDB[3]
        sql_Galaxy = []
        for y in xrange(0, hightGalaxy):
            sql_row = []
            for x in xrange(0, widthGalaxy):
                colum = []
                colum.append(str(idGalaxy))
                colum.append(str(y))
                colum.append(str(x))
                colum.append(str(0))
                sql_row.append(colum)
            sql_Galaxy.append(sql_row)
        self.SQLGalaxyPlots.insertGalaxyPlots(nameGalaxy, sql_Galaxy)

        nameSolarSystem = 'Y_' + \
            str(randint(0, hightGalaxy)) + 'X_' + str(randint(0, widthGalaxy))
        hightSolarSystem = hight
        widthSolarSystem = width

        # Install SolarSystem
        self.SQLSolarSystems = UniversSQL.SQLSolarSystems()
        self.SQLSolarSystems.createSolarSystems()
        self.SQLSolarSystems.insertSolarSystem(
            nameSolarSystem, hightSolarSystem, widthSolarSystem)

        # Install Plots for SolarSystem
        self.SQLSolarSystemPlots = UniversSQL.SQLSolarSystemPlots()
        self.SQLSolarSystemPlots.createSolarSystemPlots(nameSolarSystem)
        self.SQLSolarSystems.selectSolarSystemWith_name(nameSolarSystem)
        idSolarSystem = self.SQLSolarSystems.solarsystemNameDB[0]
        nameSolarSystem = self.SQLSolarSystems.solarsystemNameDB[1]
        hightSolarSystem = self.SQLSolarSystems.solarsystemNameDB[2]
        widthSolarSystem = self.SQLSolarSystems.solarsystemNameDB[3]
        sql_SolarSystem = []
        for y in xrange(0, hightSolarSystem):
            sql_row = []
            for x in xrange(0, widthSolarSystem):
                colum = []
                colum.append(str(idSolarSystem))
                colum.append(str(y))
                colum.append(str(x))
                colum.append(str(0))
                sql_row.append(colum)
            sql_SolarSystem.append(sql_row)
        self.SQLSolarSystemPlots.insertSolarSystemPlots(
            nameSolarSystem, sql_SolarSystem)

        nameSpaceEntity = 'Y_' + \
            str(randint(0, hightGalaxy)) + 'X_' + str(randint(0, widthGalaxy))
        hightSpaceEntity = (16 * 16)
        widthSpaceEntity = ((16 * 16) * 2)
        idSpaceEntityTyps = '0'

        # Install SolarSystem
        self.SQLSpaceEntitys = UniversSQL.SQLSpaceEntitys()
        self.SQLSpaceEntitys.createSpaceEntitys()
        self.SQLSpaceEntitys.insertSpaceEntity(
            nameSpaceEntity, hightSpaceEntity, widthSpaceEntity, idSpaceEntityTyps)

        # Install Plots for SolarSystem
        self.SQLSpaceEntityPlots = UniversSQL.SQLSpaceEntityPlots()
        self.SQLSpaceEntityPlots.createSpaceEntityPlots(nameSpaceEntity)
        self.SQLSpaceEntitys.selectSpaceEntityWith_name(nameSpaceEntity)
        idSpaceEntity = self.SQLSpaceEntitys.spaceentityNameDB[0]
        nameSpaceEntity = self.SQLSpaceEntitys.spaceentityNameDB[1]
        hightSpaceEntity = self.SQLSpaceEntitys.spaceentityNameDB[2]
        idSpaceEntityTyps = self.SQLSpaceEntitys.spaceentityNameDB[3]
        sql_SpaceEntity = []
        for y in xrange(0, hightSpaceEntity):
            sql_row = []
            for x in xrange(0, widthSpaceEntity):
                colum = []
                colum.append(str(idSpaceEntity))
                colum.append(str(y))
                colum.append(str(x))
                colum.append(str(0))
                colum.append(str(idSpaceEntityTyps))
                sql_row.append(colum)
            sql_SpaceEntity.append(sql_row)
        self.SQLSpaceEntityPlots.insertSpaceEntityPlots(
            nameSpaceEntity, sql_SpaceEntity)
