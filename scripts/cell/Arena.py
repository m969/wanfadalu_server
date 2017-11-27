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
        # self.onEvent("requestEnterArena", lambda evt: DEBUG_MSG("Arena onEvent " + str(evt["eventName"])))
        self.onEvent("requestEnterArena", self.requestEnterArena)
        self.avatarList = []

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
        self.createArenaTrigger()
        self.avatarList.append(evt["avatar"])
