# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import Math




class SpaceArenaSystem:
    def __init__(self):
        DEBUG_MSG("SpaceArenaSystem:__init__")
        if "擂台数据" in self.spaceData.keys():
            arenaDatas = self.spaceData["擂台数据"]
            arenaPosition = arenaDatas["擂台坐标"]
            arenaID = arenaDatas["擂台ID"]
            outPosition = arenaDatas["排异强制坐标"]
            self.createArena(arenaPosition, arenaID, outPosition)


    def createArena(self, arenaPosition, arenaID, outPosition):
        DEBUG_MSG("SpaceArenaSystem:createArena")
        params = {}
        params["entityName"] = "ArenaView"
        params["arenaID"] = arenaID
        self.arena = KBEngine.createEntity("Arena", self.spaceID, arenaPosition, (0.0, 0.0, 0.0), params)
        params = {}
        params["entityName"] = "ArenaNpcView"
        params["arenaID"] = arenaID
        npcPosition = (arenaPosition.x - 2, arenaPosition.y, arenaPosition.z - 2)
        self.arenaNpc = KBEngine.createEntity("Npc", self.spaceID, arenaPosition, (0.0, 0.0, 0.0), params)
        self.arena.arenaNpc = self.arenaNpc


    def createArenaTrigger(self):
        DEBUG_MSG("SpaceArenaSystem:createArenaTrigger")


    def startShield(self):
        DEBUG_MSG("SpaceArenaSystem:startShield")


    def closeShield(self):
        DEBUG_MSG("SpaceArenaSystem:closeShield")
