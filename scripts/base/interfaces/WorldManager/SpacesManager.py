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
        for spaceUID, spaceData in space_data.data.items():
            if spaceUID in self.spaceDBIDList.keys():
                KBEngine.createBaseFromDBID("Space", self.spaceDBIDList[spaceUID]["dbid"], self.__onSpaceCreateCallback)
            else:
                space = KBEngine.createBaseLocally("Space", {"spaceUID": spaceUID, "cityName": spaceData["cityName"], "spaceName": spaceData["spaceName"]})
                space.writeToDB(self.__onSpaceSaved)
                self.spaceList[spaceUID] = space
        # if self.muLingCunSpaceDBID:
        #     DEBUG_MSG("createBaseFromDBID muLingCunSpaceDBID")
        #     KBEngine.createBaseFromDBID("Space", self.muLingCunSpaceDBID, self._muLingCunSpaceCreateCallback)
        # else:
        #     DEBUG_MSG("createBaseLocally muLingCunSpace")
        #     self.muLingCunSpace = KBEngine.createBaseLocally("Space", {"cityName": "木灵村", "spaceName": "MuLingCunSpace"})
        #     self.muLingCunSpace.writeToDB(self._onMuLingCunSpaceSaved)
        # if self.yunLingZongSpaceDBID:
        #     DEBUG_MSG("createBaseFromDBID yunLingZongSpaceDBID")
        #     KBEngine.createBaseFromDBID("Space", self.yunLingZongSpaceDBID, self._yunLingZongSpaceCreateCallback)
        # else:
        #     DEBUG_MSG("createBaseLocally yunLingZongSpace")
        #     self.yunLingZongSpace = KBEngine.createBaseLocally("Space", {"cityName": "云灵宗", "spaceName": "YunLingZongSpace"})
        #     self.yunLingZongSpace.writeToDB(self._onYunLingZongSpaceSaved)


    def __onSpaceSaved(self, success, space):
        self.spaceDBIDList[space.spaceUID] = TIdDbidMap()
        self.spaceDBIDList[space.spaceUID]["id"] = space.spaceUID
        self.spaceDBIDList[space.spaceUID]["dbid"] = space.databaseID
        self.writeToDB(self._onSpacesManagerSaved, True)


    # def _onMuLingCunSpaceSaved(self, success, space):
    #     self.muLingCunSpaceDBID = space.databaseID
    #     self.writeToDB(self._onSpacesManagerSaved, True)


    # def _onYunLingZongSpaceSaved(self, success, space):
    #     self.yunLingZongSpaceDBID = space.databaseID
    #     self.writeToDB(self._onSpacesManagerSaved, True)


    def _onSpacesManagerSaved(self, success, spacesManager):
        DEBUG_MSG("SpacesManager:_onSpacesManagerSaved")
        DEBUG_MSG(spacesManager.databaseID)


    def __onSpaceCreateCallback(self, baseRef, dbid, wasActive):
        if baseRef:
            self.spaceList[baseRef.spaceUID] = baseRef
        else:
            DEBUG_MSG("space baseRef is None")


    # def _muLingCunSpaceCreateCallback(self, baseRef, dbid, wasActive):
    #     if baseRef:
    #         self.muLingCunSpace = baseRef
    #     else:
    #         DEBUG_MSG("_muLingCunSpaceCreateCallback baseRef is None")


    # def _yunLingZongSpaceCreateCallback(self, baseRef, dbid, wasActive):
    #     if baseRef:
    #         self.yunLingZongSpace = baseRef
    #     else:
    #         DEBUG_MSG("_yunLingZongSpaceCreateCallback baseRef is None")


    def addNewAvatar(self, id, avatar):
        DEBUG_MSG("SpacesManager:addNewAvatar")
        KBEngine.globalData["allAvatarBases"][id] = avatar


    def delAvatar(self, id):
        DEBUG_MSG("SpacesManager:delAvatar")
        del KBEngine.globalData["allAvatarBases"][id]


    def loginToSpaceByName(self, spaceName, entityMailbox):
        """
        通过Space名称登录到Space
        """
        DEBUG_MSG("SpacesManager:loginToSpaceByName")
        KBEngine.globalData["space_" + spaceName].loginSpace(entityMailbox)


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


    def publishBulletin(self, bulletinContent):
        DEBUG_MSG("SpacesManager:publishBulletin")
        for avatar in KBEngine.globalData["allAvatarBases"].values():
            avatar.publishBulletin(bulletinContent)
