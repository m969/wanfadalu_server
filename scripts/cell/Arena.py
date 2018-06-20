# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.Common.EntityObject import EntityObject
from strategy.trigger_strategy import *
# from rx import Observable, Observer
# from rx.subjects import Subject




class Arena(KBEngine.Entity, EntityObject):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        EntityObject.__init__(self)
        DEBUG_MSG("Arena:__init__")
        self.contestEnd = True
        self.arenaTrigger = None
        self.contestantList = {}
        # self.subscribtionList = []
        # self.onEvent("requestEnterArena").filter(lambda evt: evt['arenaID'] == self.arenaID).subscribe(on_next=self.requestEnterArena)
        # self.onEvent("requestExitArena").filter(lambda evt: evt['arenaID'] == self.arenaID).subscribe(on_next=self.requestExitArena)


    def createArenaTrigger(self):
        DEBUG_MSG("Arena:createArenaTrigger")
        # self.triggerStrategy = ArenaStrategy()
        # self.triggerStrategy.initializeStrategy({})
        # if self.arenaTrigger is None:
        #     params = {
        #         "entityName": "ArenaTrigger",
        #         "owner": self,
        #         "triggerSize": 50,
        #         "triggerStrategy": self.triggerStrategy,
        #     }
        #     self.arenaTrigger = KBEngine.createEntity("Trigger", self.spaceID, self.position, (0.0, 0.0, 0.0), params)  # 创建擂台触发器
        # else:
        #     self.arenaTrigger.position = self.position


    def startShield(self):
        DEBUG_MSG("Arena:startShield")


    def closeShield(self):
        DEBUG_MSG("Arena:closeShield")


    def requestEnterArena(self, avatar):
        DEBUG_MSG("Arena:requestEnterArena")
        if self.arenaTrigger is None:
            self.createArenaTrigger()
        if self.contestantList.__len__() >= 2:
            return
        requestAvatar = avatar
        DEBUG_MSG(requestAvatar.dbid)
        DEBUG_MSG(self.contestantList.keys())
        if requestAvatar.dbid in self.contestantList.keys():
            DEBUG_MSG("avatar has in arena")
            return
        self.contestantList[requestAvatar.dbid] = requestAvatar
        requestAvatar.onEnterArena(self)
        requestAvatar.lingshiAmount = requestAvatar.lingshiAmount - 10
        self.lingshiAward = self.lingshiAward + 10
        # subscribtion = self.onEvent("avatarDeadEvent").filter(lambda et: et["avatarID"] == requestAvatar.id).subscribe(on_next=self.onAvatarDead)
        # self.subscribtionList.append(subscribtion)
        if len(self.contestantList) == 2:
            self.contestEnd = False


    def requestExitArena(self, avatar):
        DEBUG_MSG("Arena:requestExitArena")
        requestAvatar = avatar
        if not requestAvatar.dbid in self.contestantList:
            DEBUG_MSG("avatar has not in arena")
            return
        if len(self.contestantList) is 2:
            self.setMatchResult(requestAvatar.dbid)
        if requestAvatar.dbid in self.contestantList:
            del self.contestantList[requestAvatar.dbid]
        requestAvatar.onExitArena(self)


    def onAvatarDead(self, avatar):
        DEBUG_MSG("Arena:onAvatarDead")
        deadAvatar = avatar
        if self.contestEnd == False:
            self.contestEnd = True
            self.setMatchResult(deadAvatar.dbid)


    def setMatchResult(self, loserDBID):
        DEBUG_MSG("Arena:setMatchResult")
        winnerDBID = 0
        DEBUG_MSG(self.contestantList)
        for dbid in list(self.contestantList.keys()):
            if dbid == loserDBID:
                loserDBID = dbid
            else:
                winnerDBID = dbid
        loseAvatar = self.contestantList[loserDBID]
        winAvatar = self.contestantList[winnerDBID]
        loseAvatar.onMatchEnd(iswin=False)
        loseAvatar.onExitArena(self)
        winAvatar.onMatchEnd(iswin=True)
        winAvatar.onExitArena(self)
        winAvatar.lingshiAmount = winAvatar.lingshiAmount + self.lingshiAward
        matchResult = {
            "winnerInfo": {},
            "loserInfo": {}
        }
        matchResult["winnerInfo"] = {
            "dbid": winnerDBID,
            "name": winAvatar.entityName
        }
        matchResult["loserInfo"] = {
            "dbid": loserDBID,
            "name": loseAvatar.entityName
        }
        KBEngine.globalData["SpacesManager"].addNewMatchResult(matchResult)
        self.endMatch()


    def endMatch(self):
        DEBUG_MSG("Arena:endMatch")
        self.lingshiAward = 0
        self.contestantList = {}
        # for subscribtion in self.subscribtionList:
        #     subscribtion.dispose()
        # self.subscribtionList = []
