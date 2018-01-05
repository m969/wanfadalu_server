# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from KTween.KTweenEnum import KTweenEnum


class ArenaSystem:
    def __init__(self):
        DEBUG_MSG("ArenaSystem:__init__")

    def requestEnterArena(self, exposed, arenaID):
        DEBUG_MSG("ArenaSystem:requestEnterArena")
        if exposed != self.id:
            return
        self.publish({"eventName": "requestEnterArena", "arenaID": arenaID, "avatar": self})

    def onEnterArena(self, arena):
        DEBUG_MSG("ArenaSystem:onEnterArena")
        # DEBUG_MSG(self.position)
        # self.controlledBy = None
        self.position = arena.centerPosition
        # self.controlledBy = self.base
        # DEBUG_MSG(self.position)
        self.arenaID = arena.arenaID

    def requestExitArena(self, exposed):
        DEBUG_MSG("ArenaSystem:requestExitArena")
        if exposed != self.id:
            return
        self.publish({"eventName": "requestExitArena", "arenaID": self.arenaID, "avatar": self})

    def onExitArena(self, arena):
        DEBUG_MSG("ArenaSystem:onExitArena")
        # DEBUG_MSG(self.position)
        # self.controlledBy = None
        self.position = arena.outPosition
        # self.controlledBy = self.base
        # DEBUG_MSG(self.position)
