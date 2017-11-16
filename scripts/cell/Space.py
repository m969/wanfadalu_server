# -*- coding: utf-8 -*-
import KBEngine
import space_data
from KBEDebug import *
from interfaces.Common.EntityObject import EntityObject
from interfaces.Space.SpaceGateWaySystem import SpaceGateWaySystem
from interfaces.Space.SpaceMonsterSystem import SpaceMonsterSystem
from interfaces.Space.SpaceNpcSystem import SpaceNpcSystem
from interfaces.Space.SpaceResourceWarSystem import SpaceResourceWarSystem
from interfaces.Space.SpaceArenaSystem import SpaceArenaSystem


class Space(KBEngine.Entity, EntityObject, SpaceMonsterSystem, SpaceNpcSystem, SpaceResourceWarSystem, SpaceGateWaySystem, SpaceArenaSystem):
    """
    游戏场景，在这里代表野外大地图
    """
    def __init__(self):
        DEBUG_MSG("Space:cell:__init__ " + str(self.spaceID) + " " + str(self.id) + " " + self.spaceName)
        KBEngine.Entity.__init__(self)

        self.spaceData = space_data.data[self.cityName]     # 取出自身的场景数据
        self.respawnPoint = self.spaceData["重生点"]

        EntityObject.__init__(self)
        SpaceMonsterSystem.__init__(self)
        SpaceNpcSystem.__init__(self)
        SpaceResourceWarSystem.__init__(self)
        SpaceGateWaySystem.__init__(self)
        SpaceArenaSystem.__init__(self)

        KBEngine.globalData["space_%i" % self.spaceID] = self.base
        KBEngine.globalData["space_" + self.spaceName] = self.base
        KBEngine.globalData["space_cell_%i" % self.spaceID] = self
        KBEngine.globalData["space_cell_" + self.spaceName] = self

    def onDestroy(self):
        """
        KBEngine method.
        """
        del KBEngine.globalData["space_%i" % self.spaceID]
        del KBEngine.globalData["space_" + self.spaceName]
        del KBEngine.globalData["space_cell_%i" % self.spaceID]
        del KBEngine.globalData["space_cell_" + self.spaceName]
        self.destroySpace()

    def onEnter(self, entityMailbox):
        """
        defined method.
        进入场景
        """
        DEBUG_MSG('Space::onEnter space[%d] entityID = %i.' % (self.spaceID, entityMailbox.id))
        entityMailbox.cell.onAvatarEnterSpace(self.spaceID, space_data.data[self.cityName]["场景名称"])

    def onTimer(self, timerHandle, userData):
        SpaceMonsterSystem.onTimer(self, timerHandle, userData)

    def onLeave(self, entityID):
        """
        defined method.
        离开场景
        """
        DEBUG_MSG('Space::onLeave space entityID = %i.' % (entityID))
