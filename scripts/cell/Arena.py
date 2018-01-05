# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.Common.EntityObject import EntityObject
from triggerStrategies import *


class Arena(KBEngine.Entity, EntityObject):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        EntityObject.__init__(self)
        DEBUG_MSG("Arena:__init__")
        self.arenaTrigger = None
        self.avatarList = []
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
        if self.avatarList.__len__() >= 2:
            return
        if evt["avatar"] in self.avatarList:
            DEBUG_MSG("avatar has in arena")
            return
        self.avatarList.append(evt["avatar"])
        evt["avatar"].onEnterArena(self)

    def requestExitArena(self, evt):
        DEBUG_MSG("Arena:requestExitArena")
        if not evt["avatar"] in self.avatarList:
            DEBUG_MSG("avatar has not in arena")
            return
        self.avatarList.remove(evt["avatar"])
        evt["avatar"].onExitArena(self)
