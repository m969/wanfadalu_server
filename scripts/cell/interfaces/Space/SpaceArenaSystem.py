# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class SpaceArenaSystem:
    def __init__(self):
        DEBUG_MSG("SpaceArenaSystem:__init__")
        arenaPosition = self.spaceData["擂台数据"]["擂台坐标"]
        self.createArena(arenaPosition)

    def createArena(self, arenaPosition):
        DEBUG_MSG("SpaceArenaSystem:createArena")
        self.arena = KBEngine.createEntity("Arena",
                              self.spaceID,
                              arenaPosition,
                              (0.0, 0.0, 0.0),
                              {
                                  'entityName': "ArenaView"
                              })

    def createArenaTrigger(self):
        DEBUG_MSG("SpaceArenaSystem:createArenaTrigger")


    def startShield(self):
        DEBUG_MSG("SpaceArenaSystem:startShield")

    def closeShield(self):
        DEBUG_MSG("SpaceArenaSystem:closeShield")
