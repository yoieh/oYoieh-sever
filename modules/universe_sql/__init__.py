'''
Created on 29 dec 2017

@author: Yoieh
'''
import sys

if sys.version_info[0] <= 2:
    from universe_sql.universe_db import SQLUniverseDatabase
    from universe_sql.universe import SQLUniverse
    from universe_sql.universe_plot import SQLUniversePlot
    from universe_sql.galaxy import SQLGalaxy
    from universe_sql.solarsystem import SQLSolarSystem
    from universe_sql.solarsystem_plot import SQLSolarSystemPlot
    from universe_sql.spaceentity import SQLSpaceEntity
    from universe_sql.spaceentity_plot import SQLSpaceEntityPlot
    from universe_sql.spaceentity_type import SQLspaceentityType
