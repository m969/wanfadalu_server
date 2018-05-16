# -*- coding: utf-8 -*-
import KBEngine, time
from KBEDebug import *
from strategy.trigger_strategy.TriggerStrategy import TriggerStrategy


class ImprisonStrategy(TriggerStrategy):
    """
    禁锢策略
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
            if otherEntity.canMove is not None:
                otherEntity.moveToPointSample(otherEntity.position, 20)
                otherEntity.canMove = False
            if otherEntity.canCastSkill is not None:
                otherEntity.canCastSkill = False
            otherEntity.addSkillControlTimer(
                "ImprisonCancelTimer",
                3,
                0,
                "self.canMove = True\n" +
                "self.canCastSkill = True\n" +
                "DEBUG_MSG('ImprisonCancelTimer scriptString')",
                "onceOperation")
