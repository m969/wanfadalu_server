# -*- coding: utf-8 -*-
import KBEngine
import space_data
from KBEDebug import *
from interfaces.Common.EntityObject import EntityObject
from interfaces.Space.SpaceGateWaySystem import SpaceGateWaySystem
from interfaces.Space.SpaceMonsterSystem import SpaceMonsterSystem
from interfaces.Space.SpaceNpcSystem import SpaceNpcSystem
from interfaces.Space.SpaceArenaSystem import SpaceArenaSystem




class Space(KBEngine.Entity, EntityObject, SpaceMonsterSystem, SpaceNpcSystem, SpaceGateWaySystem, SpaceArenaSystem):
    """
    游戏场景，在这里代表野外大地图
    """
    def __init__(self):
        DEBUG_MSG("Space:cell:__init__ " + str(self.spaceID) + " " + str(self.id) + " " + self.spaceName)
        KBEngine.Entity.__init__(self)
        self.spaceData = space_data.data[self.spaceUID]     # 取出自身的场景数据
        self.respawnPoint = self.spaceData["重生点"]
        EntityObject.__init__(self)
        SpaceMonsterSystem.__init__(self)
        SpaceNpcSystem.__init__(self)
        SpaceGateWaySystem.__init__(self)
        SpaceArenaSystem.__init__(self)
        KBEngine.globalData["space_base_spaceID_%i" % self.spaceID] = self.base
        # KBEngine.globalData["space_cell_spaceID_%i" % self.spaceID] = self
        # KBEngine.globalData["space_cell_spaceUID_%i" % self.spaceUID] = self


    def onDestroy(self):
        """
        """
        del KBEngine.globalData["space_base_spaceID_%i" % self.spaceID]
        # del KBEngine.globalData["space_cell_spaceID_%i" % self.spaceID]
        # del KBEngine.globalData["space_cell_spaceUID_%i" % self.spaceUID]
        self.destroySpace()


    def onEnter(self, entityCellCall):
        """
        进入场景
        """
        DEBUG_MSG('Space::onEnter space[%d] entityID = %i.' % (self.spaceID, entityCellCall.id))
        entityCellCall.onEntityEnterSpace(self.spaceID, self.spaceUID)


    def onTimer(self, timerHandle, userData):
        SpaceMonsterSystem.onTimer(self, timerHandle, userData)


    def onLeave(self, entityID):
        """
        离开场景
        """
        DEBUG_MSG('Space::onLeave space entityID = %i.' % (entityID))
