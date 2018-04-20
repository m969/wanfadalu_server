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
        self.arenaID = arena.arenaID
        self.position = arena.position
        self.client.OnEnterArena(arena.position)


    def requestExitArena(self, exposed):
        DEBUG_MSG("ArenaSystem:requestExitArena")
        if exposed != self.id:
            return
        self.publish({"eventName": "requestExitArena", "arenaID": self.arenaID, "avatar": self})


    def onExitArena(self, arena):
        DEBUG_MSG("ArenaSystem:onExitArena")
        self.position = arena.arenaNpc.position
        self.client.OnExitArena(arena.arenaNpc.position)


    def onMatchEnd(self, iswin):
        DEBUG_MSG("ArenaSystem:onMatchEnd")
        self.client.OnMatchEnd(iswin)
        if iswin:
            self.onMatchWin()
        else:
            self.onMatchLose()


    def onMatchLose(self):
        DEBUG_MSG("ArenaSystem:onMatchLose")


    def onMatchWin(self):
        DEBUG_MSG("ArenaSystem:onMatchWin")
