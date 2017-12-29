'''
Created on 18 nov 2013

@author: Yoieh
'''


class ResourcesTyps():
    def __init__(self, resourcesTyp):
        self.resourcesTyp = resourcesTyp

    def gas(self):
        self.densityMax, self.densityMin = 1

    def liquid(self):
        self.densityMax = 2
        self.densityMin = 5

    def dust(self):
        self.densityMax = 9
        self.densityMin = 6

    def solid(self):
        self.densityMax, self.densityMin = 10

    def ResourcesTypsChoise(self):
        if self.resourcesTyp == 'liquid':
            self.liquid(self.resourcesTyp)
        elif self.resourcesTyp == 'dust':
            self.dust(self.resourcesTyp)
        elif self.resourcesTyp == 'solid':
            self.solid(self.resourcesTyp)
        elif self.resourcesTyp == 'gas':
            self.gass(self.resourcesTyp)
