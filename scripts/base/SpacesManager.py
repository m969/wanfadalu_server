# -*- coding: utf-8 -*-
import KBEngine
import space_data
from KBEDebug import *
import datetime
import math
from interfaces.SpacesManager.CombatBulletinSystem import CombatBulletinSystem
from interfaces.SpacesManager.RankingListSystem import RankingListSystem


class SpacesManager(KBEngine.Base, CombatBulletinSystem, RankingListSystem):
    def __init__(self):
        DEBUG_MSG("SpacesManager:__init__")
        KBEngine.Base.__init__(self)
        CombatBulletinSystem.__init__(self)
        RankingListSystem.__init__(self)

        KBEngine.globalData["spacesManager"] = self
        # 根据场景配置表（space_data）来创建场景
        KBEngine.globalData["allAvatarBases"] = {}

        if self.muLingCunSpaceDBID:
            DEBUG_MSG("createBaseFromDBID muLingCunSpaceDBID")
            KBEngine.createBaseFromDBID("Space", self.muLingCunSpaceDBID, self._muLingCunSpaceCreateCallback)
        else:
            DEBUG_MSG("createBaseLocally muLingCunSpace")
            self.muLingCunSpace = KBEngine.createBaseLocally("Space", {"cityName": "木灵村", "spaceName": "MuLingCunSpace"})
            self.muLingCunSpace.writeToDB(self._onMuLingCunSpaceSaved)

        if self.yunLingZongSpaceDBID:
            DEBUG_MSG("createBaseFromDBID yunLingZongSpaceDBID")
            KBEngine.createBaseFromDBID("Space", self.yunLingZongSpaceDBID, self._yunLingZongSpaceCreateCallback)
        else:
            DEBUG_MSG("createBaseLocally yunLingZongSpace")
            self.yunLingZongSpace = KBEngine.createBaseLocally("Space", {"cityName": "云灵宗", "spaceName": "YunLingZongSpace"})
            self.yunLingZongSpace.writeToDB(self._onYunLingZongSpaceSaved)

    def _onMuLingCunSpaceSaved(self, success, space):
        self.muLingCunSpaceDBID = space.databaseID
        self.writeToDB(self._onSpacesManagerSaved, True)

    def _onYunLingZongSpaceSaved(self, success, space):
        self.yunLingZongSpaceDBID = space.databaseID
        self.writeToDB(self._onSpacesManagerSaved, True)

    def _onSpacesManagerSaved(self, success, spacesManager):
        DEBUG_MSG("SpacesManager:_onSpacesManagerSaved")
        DEBUG_MSG(spacesManager.databaseID)

    def _muLingCunSpaceCreateCallback(self, baseRef, dbid, wasActive):
        if baseRef:
            self.muLingCunSpace = baseRef
        else:
            DEBUG_MSG("_muLingCunSpaceCreateCallback baseRef is None")

    def _yunLingZongSpaceCreateCallback(self, baseRef, dbid, wasActive):
        if baseRef:
            self.yunLingZongSpace = baseRef
        else:
            DEBUG_MSG("_yunLingZongSpaceCreateCallback baseRef is None")

    def onTimer(self, timerHandle, userData):
        CombatBulletinSystem.onTimer(self, timerHandle, userData)

    def addNewAvatar(self, id, avatar):
        DEBUG_MSG("SpacesManager:addNewAvatar")
        KBEngine.globalData["allAvatarBases"][id] = avatar

    def delAvatar(self, id):
        DEBUG_MSG("SpacesManager:delAvatar")
        del KBEngine.globalData["allAvatarBases"][id]

    def loginToSpaceByName(self, spaceName, entityMailbox):
        """
        通过Space名称登录到Space
        :param spaceName:
        :param entityMailbox:
        :return:
        """
        DEBUG_MSG("SpacesManager:loginToSpaceByName")
        KBEngine.globalData["space_" + spaceName].loginSpace(entityMailbox)

    def teleportToSpaceByName(self, spaceName, gateWayEntrancePosition, entityMailbox):
        """
        通过Space名称传送到Space
        :param spaceName:
        :param entityMailbox:
        :return:
        """
        DEBUG_MSG("SpacesManager:teleportToSpaceByName")
        entityMailbox.cell.isGoingToTeleport(spaceName, gateWayEntrancePosition)

    def logoutSpace(self, avatarID, spaceID):
        """
        defined method.
        某个玩家请求登出这个space
        """
        space = KBEngine.globalData["space_%i" % spaceID]
        space.logoutSpace(avatarID)

    def publishBulletin(self, bulletinContent):
        DEBUG_MSG("SpacesManager:publishBulletin")
        for avatar in KBEngine.globalData["allAvatarBases"].values():
            avatar.publishBulletin(bulletinContent)
