# -*- coding: utf-8 -*-
import KBEngine, time
from KBEDebug import *
from strategy.trigger_strategy.TriggerStrategy import TriggerStrategy


class DecelerateStrategy(TriggerStrategy):
    """
    减速策略
    """
    def __init__(self):
        TriggerStrategy.__init__(self)

    def initializeStrategy(self, strategyData):
        super().initializeStrategy(strategyData)
        self.damage = strategyData["伤害"]

    def execute(self, trigger=None, otherEntity=None):
        # DEBUG_MSG("topSpeed " + str(otherEntity.topSpeed))
        if otherEntity.canReceiveSkill is True:
            if otherEntity.canMove is not None:
                otherEntity.setAttr("topSpeed", otherEntity.topSpeed - 4)
            otherEntity.addSkillControlTimer(
                "DecelerateCancelTimer",
                3,
                0,
                "self.topSpeed += 4\n" +
                "DEBUG_MSG('DecelerateCancelTimer scriptString')",
                "onceOperation")
