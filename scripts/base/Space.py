# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import monster_data
import npc_data
import space_data
from interfaces.Common.EntityObject import EntityObject
from interfaces.Space.SpaceGateWaySystem import SpaceGateWaySystem
from interfaces.Space.SpaceMonsterSystem import SpaceMonsterSystem
from interfaces.Space.SpaceNpcSystem import SpaceNpcSystem
from interfaces.Space.SpaceResourceWarSystem import SpaceResourceWarSystem
from interfaces.Space.SpaceArenaSystem import SpaceArenaSystem




class Space(KBEngine.Base, EntityObject, SpaceMonsterSystem, SpaceNpcSystem, SpaceResourceWarSystem, SpaceGateWaySystem, SpaceArenaSystem):
    def __init__(self):
        DEBUG_MSG("Space:__init__")
        KBEngine.Base.__init__(self)
        EntityObject.__init__(self)
        if not hasattr(self, "spaceUID"):
            self.spaceUID = self.cellData["spaceUID"]
        self.spaceData = space_data.data[self.spaceUID]
        SpaceMonsterSystem.__init__(self)
        SpaceNpcSystem.__init__(self)
        SpaceResourceWarSystem.__init__(self)
        SpaceGateWaySystem.__init__(self)
        SpaceArenaSystem.__init__(self)
        if not hasattr(self, "spaceName"):
            self.spaceName = self.cellData["spaceName"]
        if not hasattr(self, "cityName"):
            self.cityName = self.cellData["cityName"]
        self.createInNewSpace(None)


    def onGetCell(self):
        DEBUG_MSG("Space:onGetCell")


    def loginSpace(self, entityMailbox):
        DEBUG_MSG("Space:loginSpace")
        if self.cell is None:
            WARNING_MSG("space cell is None")
            return
        entityMailbox.createCell(self.cell)
        self.onEnter(entityMailbox)


    def logoutSpace(self, entityID):
        self.onLeave(entityID)


    def requestTeleport(self, entityMailbox):
        DEBUG_MSG("Space:requestTeleport")
        entityMailbox.cell.teleportToSpace(self.cell, self.spaceData["触发器数据"]["传送门入口点"], (0.0, 0.0, 0.0))


    def onEnter(self, entityMailbox):
        DEBUG_MSG("Space:onEnter")
        self.cell.onEnter(entityMailbox)


    def onLeave(self, entityID):
        if self.cell is not None:
            self.cell.onLeave(entityID)
