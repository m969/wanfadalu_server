# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *




class SpaceArenaSystem:
    def __init__(self):
        DEBUG_MSG("SpaceArenaSystem:__init__")
        if "擂台数据" in self.spaceData.keys():
            arenaDatas = self.spaceData["擂台数据"]
            arenaPosition = arenaDatas["擂台坐标"]
            arenaID = arenaDatas["擂台ID"]
            centerPosition = arenaDatas["擂台中心坐标"]
            outPosition = arenaDatas["排异强制坐标"]
            self.createArena(arenaPosition, arenaID, outPosition, centerPosition)


    def createArena(self, arenaPosition, arenaID, outPosition, centerPosition):
        DEBUG_MSG("SpaceArenaSystem:createArena")
        self.arena = KBEngine.createEntity("Arena",
                              self.spaceID,
                              arenaPosition,
                              (0.0, 0.0, 0.0),
                              {
                                  'entityName': "ArenaView",
                                  'arenaID': arenaID,
                                  "outPosition": outPosition,
                                  'centerPosition': centerPosition
                              })


    def createArenaTrigger(self):
        DEBUG_MSG("SpaceArenaSystem:createArenaTrigger")


    def startShield(self):
        DEBUG_MSG("SpaceArenaSystem:startShield")


    def closeShield(self):
        DEBUG_MSG("SpaceArenaSystem:closeShield")
