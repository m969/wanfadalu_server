# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import Math
import avatar_skill_data
from strategy.skill_strategy import *
from strategy.trigger_strategy import *




class SkillE(Skill):
    def __init__(self, spellCaster, argsString, gongFaID, skillIndex):
        Skill.__init__(self, spellCaster, argsString, gongFaID, skillIndex)
        args = argsString.split(":")
        self.skillPoint = Math.Vector3(float(args[0]), float(args[1]), float(args[2]))


    def startSing(self):
        self.spellCaster.moveToPoint(self.skillPoint, 0.01, 0.1, {}, True, True)
        return super().startSing()


    def cast(self):
        damage = int(self.skillSpAmount * self.skillQuality)
        self.strategyData = {"伤害": damage}
        super().cast()
        midPoint = self.midPoint(self.spellCaster.position, self.skillPoint)
        pointList = [self.spellCaster.position, midPoint, self.skillPoint]
        for point in pointList:
            trigger = KBEngine.createEntity("Trigger",
                                            self.spellCaster.spaceID,
                                            point,
                                            (0.0, 0.0, 0.0),
                                            {
                                                'entityName': "SkillE_Trigger",
                                                'owner': self.spellCaster,
                                                'campName': self.spellCaster.campName,
                                                'lifeSpans': 2.0,
                                                'triggerID': 2,
                                                'triggerSize': 4,
                                                'triggerStrategy': self.triggerStrategy
                                            })


    def midPoint(self, point1, point2):
        x = (point1.x + point2.x) / 2
        y = (point1.y + point2.y) / 2
        z = (point1.z + point2.z) / 2
        midPoint = (x, y, z)
        return midPoint
