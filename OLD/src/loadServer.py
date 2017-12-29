'''
Created on 15 nov 2013

@author: Yoieh
'''
import UniversSQL
import installServer
import time


class loadServer():
    def load(self):
        # Univers
        sqlTable = UniversSQL.SQLUnivers()
        sqlTablePlots = UniversSQL.SQLUniversPlots()
        sqlTableSelect = sqlTable.selectUnivers()
        mapDB = sqlTableSelect
        for o in xrange(0, len(mapDB)):
            print mapDB[o][1]
            sqlTablePlotsSelect = sqlTablePlots.selectUniversPlots(mapDB[o][1])
            mapPlotsDB = sqlTablePlotsSelect

            self.loadMaps(o, sqlTable, sqlTablePlots, mapDB, mapPlotsDB)

        # Galaxys
        sqlTable = UniversSQL.SQLGalaxys()
        sqlTablePlots = UniversSQL.SQLGalaxyPlots()
        mapDB = sqlTable.selectGalaxys()
        for o in xrange(0, len(mapDB)):
            print mapDB[o][1]
            mapPlotsDB = sqlTablePlots.selectGalaxyPlots(mapDB[o][1])

            self.loadMaps(o, sqlTable, sqlTablePlots, mapDB, mapPlotsDB)

        # SolarSystems
        sqlTable = UniversSQL.SQLSolarSystems()
        sqlTablePlots = UniversSQL.SQLSolarSystemPlots()
        mapDB = sqlTable.selectSolarSystems()
        for o in xrange(0, len(mapDB)):
            print mapDB[o][1]
            mapPlotsDB = sqlTablePlots.selectSolarSystemPlots(mapDB[o][1])

            self.loadMaps(o, sqlTable, sqlTablePlots, mapDB, mapPlotsDB)

        # SolarSystems
#        sqlTable = UniversSQL.SQLSpaceEntitys()
#        sqlTablePlots = UniversSQL.SQLSpaceEntityPlots()
#        mapDB = sqlTable.selectSpaceEntitys()
#        for o in xrange(0, len(mapDB)):
#            print mapDB[o][1]
#            mapPlotsDB = sqlTablePlots.selectSpaceEntitysPlots(mapDB[o][1])
#
#            self.loadMaps(o, sqlTable, sqlTablePlots, mapDB, mapPlotsDB)

    def loadMaps(self, o, sqlTable, sqlTablePlots, mapDB, mapPlotsDB):
        widthDB = mapDB[o][2]
        hightDB = mapDB[o][3]
        print widthDB
        print hightDB

        chunkList = [mapPlotsDB[i:i + 16]
                     for i in xrange(0, len(mapPlotsDB), 16)]

        mapList = self.createChunk(widthDB, hightDB, plotsList)
        print mapList[15][15]

    def createChunk(self, width, hight, plotsList):
        if width > hight:
            Test = 2
            yyMin = 0
            yyMax = 16
            xxMin = 0
            xxMax = 16
        elif width == hight:
            Test = 1
            yyMin = 0
            yyMax = 16
            xxMin = 0
            xxMax = 16
        else:
            print 'No symetry between width and hight'
        list_y = []
        for i in xrange(1):
            for y in xrange(0, 256 / 16):
                list_x = []
                for x in xrange(0, 256 / 16):
                    list_yy = []
                    for yy in xrange(yyMin, yyMax):
                        list_xx = []
                        for xx in xrange(xxMin, xxMax):
                            # print str(y)+' '+str(x)+' '+str(yy)+' '+str(xx)
                            # print plotsList[yy][xx]
                            list_xx.append(plotsList[yy][xx])
                        list_yy.append(list_xx)
                    list_x.append(list_yy)
                xxMin = xxMin + 16
                xxMax = xxMax + 16
                list_y.append(list_x)
            xxMin = 0
            xxMax = 16
            yyMin = yyMin + 16
            yyMin = yyMax + 16

        self.chunkList = list_y
        return self.chunkList
        #    print "new------------------------------------------------------------------------->"


#installServer = installServer.installServer()
# installServer.install()
#loadServer = loadServer()
# loadServer.load()
