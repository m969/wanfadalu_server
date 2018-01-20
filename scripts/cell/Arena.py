# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.Common.EntityObject import EntityObject
from triggerStrategies import *
from rx import Observable, Observer
from rx.subjects import Subject


class Arena(KBEngine.Entity, EntityObject):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        EntityObject.__init__(self)
        DEBUG_MSG("Arena:__init__")
        self.arenaTrigger = None
        self.contestantList = {}
        self.onEvent("requestEnterArena").filter(lambda evt: evt['arenaID'] == self.arenaID).subscribe(on_next=self.requestEnterArena)
        self.onEvent("requestExitArena").filter(lambda evt: evt['arenaID'] == self.arenaID).subscribe(on_next=self.requestExitArena)

    def createArenaTrigger(self):
        DEBUG_MSG("Arena:createArenaTrigger")
        self.triggerStrategy = ArenaStrategy()
        self.triggerStrategy.initializeStrategy({})
        if self.arenaTrigger is None:
            self.arenaTrigger = KBEngine.createEntity("Trigger",
                                                     self.spaceID,
                                                     self.position,
                                                     (0.0, 0.0, 0.0),
                                                     {
                                                         "entityName": "ArenaTrigger",
                                                         "owner": self,
                                                         "triggerSize": 50,
                                                         "triggerStrategy": self.triggerStrategy,
                                                     })  # 创建擂台触发器
        else:
            self.arenaTrigger.setAttr("position", self.position)

    def startShield(self):
        DEBUG_MSG("Arena:startShield")

    def closeShield(self):
        DEBUG_MSG("Arena:closeShield")

    def requestEnterArena(self, evt):
        DEBUG_MSG("Arena:requestEnterArena")
        if self.arenaTrigger is None:
            self.createArenaTrigger()
        if self.contestantList.__len__() >= 2:
            return
        if evt["avatar"].getDatabaseID() in self.contestantList.keys():
            DEBUG_MSG("avatar has in arena")
            return
        self.contestantList.__setitem__(evt["avatar"].getDatabaseID(), evt["avatar"])
        evt["avatar"].onEnterArena(self)
        self.onEvent("avatarDeadEvent").filter(lambda et: et["avatarID"] == evt["avatar"].id).subscribe(on_next=self.onAvatarDead)

    def requestExitArena(self, evt):
        DEBUG_MSG("Arena:requestExitArena")
        if not evt["avatar"].getDatabaseID() in self.contestantList.keys():
            DEBUG_MSG("avatar has not in arena")
            return
        self.contestantList.__delitem__(evt["avatar"].getDatabaseID())
        evt["avatar"].onExitArena(self)

    def onAvatarDead(self, evt):
        DEBUG_MSG("Arena:onAvatarDead")
        self.setMatchResult(evt["avatar"].getDatabaseID())

    def setMatchResult(self, loserDBID):
        DEBUG_MSG("Arena:setMatchResult")
        for dbid in self.contestantList.keys():
            if dbid == loserDBID:
                loserDBID = dbid
            else:
                winnerDBID = dbid
        self.contestantList[loserDBID].onMatchEnd(iswin=False)
        self.contestantList[winnerDBID].onMatchEnd(iswin=True)
        matchResult = {}
        matchResult["winnerInfo"] = {}
        matchResult["loserInfo"] = {}
        matchResult["winnerInfo"]["dbid"] = winnerDBID
        matchResult["loserInfo"]["dbid"] = loserDBID
        KBEngine.globalData["spacesManager"].addNewMatchResult(matchResult)

    def endMatch(self):
        DEBUG_MSG("Arena:endMatch")
