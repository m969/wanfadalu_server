# -*- coding: utf-8 -*-
import KBEngine, time
from KBEDebug import *
from triggerStrategies.TriggerStrategy import TriggerStrategy
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


    def execute(self):
        super().execute()
        if isinstance(self.otherEntity, HealthSystem):
            if self.otherEntity.canDamage is True:
                if self.otherEntity.campName != self.trigger.owner.campName:
                    self.otherEntity.receiveDamage(self.trigger.owner, self.damage)
                    self.trigger.destroy()
