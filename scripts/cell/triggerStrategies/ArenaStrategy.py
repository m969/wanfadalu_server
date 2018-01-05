# -*- coding: utf-8 -*-
import KBEngine, time
from KBEDebug import *
from triggerStrategies.TriggerStrategy import TriggerStrategy


class ArenaStrategy(TriggerStrategy):
    """
    擂台触发器策略
    """
    def __init__(self):
        TriggerStrategy.__init__(self)

    def initializeStrategy(self, strategyData):
        super().initializeStrategy(strategyData)

    def execute(self):
        super().execute()
        if self.otherEntity.arenaID != self.trigger.owner.id:
            if self.otherEntity.id != self.trigger.owner.id:
                self.otherEntity.position = self.trigger.owner.outPosition
