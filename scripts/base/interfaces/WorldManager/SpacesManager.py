# -*- coding: utf-8 -*-
import KBEngine
import space_data
from KBEDebug import *
import datetime
import math
from ID_DBID_MAP_LIST import TIdDbidMap
from ID_DBID_MAP_LIST import TIdDbidMapList




class SpacesManager:
    def __init__(self):
        DEBUG_MSG("SpacesManager:__init__")
        KBEngine.globalData["SpacesManager"] = self
        KBEngine.globalData["allAvatarBases"] = {}
        if not hasattr(self, "spaceDBIDList"):
            self.spaceDBIDList = TIdDbidMapList()
        self.spaceList = {}
        self.spaceCreateCounter = 0
        for spaceUID, spaceData in space_data.data.items():
            if spaceUID in self.spaceDBIDList.keys():
                KBEngine.createBaseFromDBID("Space", self.spaceDBIDList[spaceUID]["dbid"], self.__onSpaceCreateCallback)
            else:
                space = KBEngine.createBaseLocally("Space", {"spaceUID": spaceUID, "cityName": spaceData["cityName"], "spaceName": spaceData["spaceName"]})
                space.writeToDB(self.__onSpaceSaved)
                self.spaceList[spaceUID] = space


    def __onSpaceSaved(self, success, space):
        self.spaceDBIDList[space.spaceUID] = TIdDbidMap()
        self.spaceDBIDList[space.spaceUID]["id"] = space.spaceUID
        self.spaceDBIDList[space.spaceUID]["dbid"] = space.databaseID
        self.writeToDB(self.__onSpacesManagerSaved, True)


    def __onSpacesManagerSaved(self, success, spacesManager):
        DEBUG_MSG("SpacesManager:__onSpacesManagerSaved")


    def __onSpaceCreateCallback(self, baseRef, dbid, wasActive):
        if baseRef:
            self.spaceList[baseRef.spaceUID] = baseRef
        else:
            DEBUG_MSG("space baseRef is None")


    def onSpaceGetCell(self, spaceUID):
        DEBUG_MSG("SpacesManager:onSpaceGetCell")
        self.spaceCreateCounter = self.spaceCreateCounter + 1
        if self.spaceCreateCounter >= len(space_data.data):
            self.onAllSpacesGetCell()


    def addNewAvatar(self, id, avatar):
        DEBUG_MSG("SpacesManager:addNewAvatar")
        KBEngine.globalData["allAvatarBases"][id] = avatar


    def delAvatar(self, id):
        DEBUG_MSG("SpacesManager:delAvatar")
        del KBEngine.globalData["allAvatarBases"][id]


    def loginToSpace(self, spaceUID, entityMailbox):
        """
        登录到Space
        """
        DEBUG_MSG("SpacesManager:loginToSpace")
        KBEngine.globalData["space_base_spaceUID_%i" % spaceUID].loginSpace(entityMailbox)


    def teleportToSpace(self, spaceUID, gateWayEntrancePosition, entityMailbox):
        """
        传送到Space
        """
        DEBUG_MSG("SpacesManager:teleportToSpace")
        entityMailbox.cell.isGoingToTeleport(spaceUID, gateWayEntrancePosition)


    def loginToSpaceByName(self, spaceName, entityMailbox):
        """
        通过Space名称登录到Space
        """
        DEBUG_MSG("SpacesManager:loginToSpaceByName")
        KBEngine.globalData["space_base_%s" % spaceName].loginSpace(entityMailbox)


    def teleportToSpaceByName(self, spaceName, gateWayEntrancePosition, entityMailbox):
        """
        通过Space名称传送到Space
        """
        DEBUG_MSG("SpacesManager:teleportToSpaceByName")
        entityMailbox.cell.isGoingToTeleport(spaceName, gateWayEntrancePosition)


    def logoutSpace(self, avatarID, spaceID):
        """
        某个玩家请求登出这个space
        """
        space = KBEngine.globalData["space_%i" % spaceID]
        space.logoutSpace(avatarID)
