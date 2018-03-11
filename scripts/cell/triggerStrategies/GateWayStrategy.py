# -*- coding: utf-8 -*-
import KBEngine, time
from KBEDebug import *
from triggerStrategies.TriggerStrategy import TriggerStrategy




class GateWayStrategy(TriggerStrategy):
    """
    传送门策略
    """
    def __init__(self):
        TriggerStrategy.__init__(self)


    def initializeStrategy(self, strategyData):
        super().initializeStrategy(strategyData)
        self.targetSpaceUID = strategyData["spaceUID"]
        self.gateWayEntrancePosition = strategyData["enterPos"]


    def execute(self):
        super().execute()
        if self.otherEntity.getScriptName() is "Avatar":
            if not hasattr(self.otherEntity, "teleporting"):
                self.otherEntity.teleporting = False
            if self.otherEntity.teleporting == True:
                return
            self.otherEntity.teleporting = True
            KBEngine.globalData["SpacesManager"].teleportToSpace(self.targetSpaceUID, self.gateWayEntrancePosition, self.otherEntity.base)
