'''
Created on 29 dec 2017

@author: Yoieh
'''
import sys

if sys.version_info[0] <= 2:
    from modules.universe_sql import SQLUniverseDatabase
    from modules.universe_sql import SQLUniverse
    from modules.universe_sql import SQLUniversePlot
    from modules.universe_sql import SQLGalaxy
    from modules.universe_sql import SQLSolarSystem
    from modules.universe_sql import SQLSolarSystemPlot
    from modules.universe_sql import SQLSpaceEntity
    from modules.universe_sql import SQLSpaceEntityPlot
    from modules.universe_sql import SQLspaceentityType
