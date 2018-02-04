# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *




class TeleportSystem:
    def __init__(self):
        DEBUG_MSG("TeleportSystem:__init__")


    def onTimer(self, timerHandle, userData):
        pass


    def isGoingToTeleport(self, spaceName, gateWayEntrancePosition):
        DEBUG_MSG("TeleportSystem:isGoingToTeleport")
        self.client.onMainAvatarLeaveSpace()
        self.newSpaceName = spaceName
        self.newSpacePosition = gateWayEntrancePosition


    def teleportToSpace(self, spaceCellMailbox, position, direction):
        """
        baseapp返回teleportSpace的回调
        """
        DEBUG_MSG("TeleportSystem:teleportToSpace")
        self.getCurrentSpaceBase().onLeave(self.id)
        self.teleport(spaceCellMailbox, position, direction)
        #self.base.onTeleportSuccess(self.newSpaceName)
        #self.counter = 0
        #self.resetPositionTimerHandle = self.addTimer(0.1, 0.2, 41)  # 重置角色坐标计数器
        #self.onAvatarEnterSpace(spaceCellMailbox.spaceID, spaceCellMailbox.spaceName)


    def onTeleportSuccess(self, nearbyEntity):
        DEBUG_MSG("TeleportSystem:onTeleportSuccess")
        #self.base.onTeleportSuccess(self.newSpaceName)
        #self.teleport(None, self.newSpacePosition, (0.0, 0.0, 0.0))
        self.teleporting = False
        self.onAvatarEnterSpace(self.spaceID, self.newSpaceName)
        self.client.Teleport(self.newSpacePosition)


    def onLeaveSpaceClientInputInValid(self, exposed):
        DEBUG_MSG("TeleportSystem:onLeaveSpaceClientInputInValid")
        KBEngine.globalData["space_" + self.newSpaceName].requestTeleport(self.base)


    def onAvatarEnterSpace(self, spaceID, spaceName):
        DEBUG_MSG("TeleportSystem:onAvatarEnterSpace")
        self.client.onMainAvatarEnterSpace(spaceID, spaceName)
