# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import PyDatas.space_config_Table as space_config_Table




class TeleportSystem:
    def __init__(self):
        # DEBUG_MSG("TeleportSystem:__init__")
        KBEngine.globalData["space_base_spaceID_%i" % self.spaceID].cell.onEnter(self)
        self.teleporting = False


    def onTimer(self, timerHandle, userData):
        pass


    def isGoingToTeleport(self, spaceUID, gateWayEntrancePosition):
        DEBUG_MSG("TeleportSystem:isGoingToTeleport")
        self.client.onMainAvatarLeaveSpace()
        self.newSpaceUID = spaceUID
        self.newSpacePosition = gateWayEntrancePosition


    def teleportToSpace(self, spaceCellMailbox, position, direction):
        """
        baseapp返回teleportSpace的回调
        """
        DEBUG_MSG("TeleportSystem:teleportToSpace")
        self.getCurrentSpaceBase().onLeave(self.id)
        self.teleport(spaceCellMailbox, position, direction)


    def onTeleportSuccess(self, nearbyEntity):
        DEBUG_MSG("TeleportSystem:onTeleportSuccess")
        self.teleporting = False
        self.onEntityEnterSpace(self.spaceID, self.newSpaceUID)
        self.base.onTeleportSuccess(self.newSpaceUID)
        self.client.Teleport(self.newSpacePosition)


    def onLeaveSpaceClientInputInValid(self, exposed):
        DEBUG_MSG("TeleportSystem:onLeaveSpaceClientInputInValid")
        KBEngine.globalData["space_base_spaceUID_" + str(self.newSpaceUID)].requestTeleport(self.base, self.newSpacePosition)


    def onEntityEnterSpace(self, spaceID, spaceUID):
        DEBUG_MSG("TeleportSystem:onEntityEnterSpace")
        self.client.onMainAvatarEnterSpace(spaceID, space_config_Table.datas[spaceUID]["spaceName"])
