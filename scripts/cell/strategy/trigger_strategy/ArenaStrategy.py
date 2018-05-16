# -*- coding: utf-8 -*-
import KBEngine, time
from KBEDebug import *
from strategy.trigger_strategy.TriggerStrategy import TriggerStrategy


class ArenaStrategy(TriggerStrategy):
    """
    擂台触发器策略
    """
    def __init__(self):
        TriggerStrategy.__init__(self)

    def initializeStrategy(self, strategyData):
        super().initializeStrategy(strategyData)

    def execute(self, trigger=None, otherEntity=None):
        if otherEntity.arenaID != trigger.owner.id:
            if otherEntity.id != trigger.owner.id:
                otherEntity.position = trigger.owner.arenaNpc.position
