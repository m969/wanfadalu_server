# -*- coding: utf-8 -*-
import KBEngine, time
from KBEDebug import *
from strategy.trigger_strategy.TriggerStrategy import TriggerStrategy
from interfaces.Common.HealthSystem import HealthSystem




class OnceDamageStrategy(TriggerStrategy):
    """
    一次伤害策略
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
        if otherEntity.canDamage is True:
            otherEntity.receiveDamage(trigger.owner, self.damage)
            if not trigger.isDestroyed:
                trigger.destroySelf()
