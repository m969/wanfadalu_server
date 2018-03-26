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


    def execute(self):
        super().execute()
        # DEBUG_MSG("self.otherEntity " + str(self.otherEntity))
        # DEBUG_MSG("self.trigger " + str(self.trigger))
        # DEBUG_MSG("self.trigger.owner " + str(self.trigger.owner))
        if self.otherEntity.id == self.trigger.owner.id:
            return
        if not hasattr(self.otherEntity, "canDamage"):
            return
        if self.otherEntity.canDamage is True:
            self.otherEntity.receiveDamage(self.trigger.owner, self.damage)
            # self.trigger.destroy()
