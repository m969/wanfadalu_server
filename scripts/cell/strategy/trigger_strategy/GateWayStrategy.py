# -*- coding: utf-8 -*-
import KBEngine, time
from KBEDebug import *
from strategy.trigger_strategy.TriggerStrategy import TriggerStrategy




class GateWayStrategy(TriggerStrategy):
    """
    传送门策略
    """
    def __init__(self):
        TriggerStrategy.__init__(self)


    def initializeStrategy(self, strategyData):
        super().initializeStrategy(strategyData)
        triggerConfig = strategyData["triggerConfig"]
        self.targetSpaceUID = int(triggerConfig[0][0])
        self.gateWayEntrancePosition = triggerConfig[1]


    def execute(self, trigger=None, otherEntity=None):
        if otherEntity.getScriptName() is "Avatar":
            if otherEntity.teleporting == True:
                return
            otherEntity.teleporting = True
            KBEngine.globalData["SpacesManager"].teleportToSpace(self.targetSpaceUID, self.gateWayEntrancePosition, otherEntity.base)
