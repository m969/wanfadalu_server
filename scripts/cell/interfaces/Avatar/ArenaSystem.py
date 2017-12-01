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
        # KBEngine.entities[arenaID].requestEnterArena(self)
        self.publish({ "eventName": "requestEnterArena", "arenaID": arenaID, "avatar": self })

    def onEnterArena(self, arena):
        DEBUG_MSG("ArenaSystem:onEnterArena")
        self.position = arena.outPosition
