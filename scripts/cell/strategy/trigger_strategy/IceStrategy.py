# -*- coding: utf-8 -*-
import KBEngine, time
from KBEDebug import *
from strategy.trigger_strategy.TriggerStrategy import TriggerStrategy


class IceStrategy(TriggerStrategy):
    """
    冰霜策略
    """
    def __init__(self):
        TriggerStrategy.__init__(self)

    def initializeStrategy(self, strategyData):
        super().initializeStrategy(strategyData)
        self.damage = strategyData["伤害"]

    def execute(self, trigger=None, otherEntity=None):
        if otherEntity.id == trigger.owner.id:
            return
        if not hasattr(otherEntity, "canDamage"):
            return
        if otherEntity.canReceiveSkill is True:
            otherEntity.isIceFreezing = True
            otherEntity.addSkillControlTimer(
                "IceCancelTimer",
                3,
                0,
                "self.isIceFreezing = False\n" +
                "DEBUG_MSG('IceCancelTimer scriptString')",
                "onceOperation")
