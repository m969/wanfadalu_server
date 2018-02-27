# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import avatar_skill_data
import trigger_strategy
from Skills import *
from triggerStrategies import *




class Shoot(Skill):
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
        params["entityName"] = "Shoot_Trigger"
        params["owner"] = self.spellCaster
        params["lifeSpans"] = 4.0
        params["triggerSize"] = 4
        params["triggerStrategy"] = self.triggerStrategy
        trigger = KBEngine.createEntity("Trigger", self.spellCaster.spaceID, self.spellCaster.position, (0.0, 0.0, 0.0), params)
        trigger.moveToPointSample(self.skillPoint, 80)
