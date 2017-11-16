# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import avatar_skill_data
import trigger_strategy
from Skills import *
from triggerStrategies import *


class SkillQ(Skill):
    def __init__(self, spellCaster, argsString, gongFaName, skillName):
        Skill.__init__(self, spellCaster, argsString, gongFaName, skillName)
        args = argsString.split(":")
        self.skillPoint = (float(args[0]), float(args[1]), float(args[2]))

    def startSing(self):
        self.spellCaster.moveToPoint(self.skillPoint, 0.01, 0.1, {}, True, True)
        return super().startSing()

    def cast(self):
        damage = int(self.skillSpAmount * self.skillQuality)
        self.strategyData = {"伤害": damage}
        super().cast()
        trigger = KBEngine.createEntity("Trigger",
                                        self.spellCaster.spaceID,
                                        self.spellCaster.position,
                                        self.spellCaster.direction,
                                        {
                                            'entityName': "SkillQ_Trigger",
                                            'owner': self.spellCaster,
                                            "campName": self.spellCaster.getAttr("campName"),
                                            'triggerID': 1,
                                            'triggerSize': 4,
                                            'triggerStrategy': self.triggerStrategy
                                        })
        trigger.moveToPointSample(self.skillPoint, 80)
