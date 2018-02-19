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
        params["triggerID"] = 1
        params["triggerSize"] = 4
        params["triggerStrategy"] = self.triggerStrategy
        DEBUG_MSG(self.spellCaster.spaceID)
        DEBUG_MSG(self.spellCaster.position)
        DEBUG_MSG(self.spellCaster.direction)
        DEBUG_MSG(params)
        trigger = KBEngine.createEntity("Trigger", self.spellCaster.spaceID, self.spellCaster.position, self.spellCaster.direction, params)
        # trigger.moveToPointSample(self.skillPoint, 80)
