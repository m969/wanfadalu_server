# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from strategy.skill_strategy import *
from strategy.trigger_strategy import *




class ArrowExplode(Skill):
    def __init__(self, spellCaster, argsString, gongFaID, skillIndex):
        Skill.__init__(self, spellCaster, argsString, gongFaID, skillIndex)
        args = argsString.split(":")
        self.skillPoint = (float(args[0]), float(args[1]), float(args[2]))


    def startSing(self):
        self.spellCaster.moveToPoint(self.skillPoint, 0.01, 0.1, {}, True, True)
        return super().startSing()


    def cast(self):
        damage = int(self.skillSpAmount * self.skillQuality)
        self.strategyData = {"伤害": damage}
        super().cast()
        params = {}
        params["entityName"] = "ArrowExplode_Trigger"
        params["owner"] = self.spellCaster
        params["lifeSpans"] = 4.0
        params["triggerSize"] = 4.0
        params["triggerStrategy"] = self.triggerStrategy
        trigger = KBEngine.createEntity("Trigger", self.spellCaster.spaceID, self.spellCaster.position, (0.0, 0.0, 0.0), params)
        trigger.moveToPointSample(self.skillPoint, 80)
