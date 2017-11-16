# -*- coding: utf-8 -*-
from triggerStrategies.TriggerStrategy import *
from Skills import *
import avatar_skill_data
import gongfa_data
from GONGFA_LIST import TGongFaList
from GONGFA_LIST import TSkill
from interfaces.Common.GongFaSystem import GongFaSystem
from rx import Observable, Observer


def push_five_strings(observer):
    observer.on_next("Alpha")
    observer.on_next("Beta")
    observer.on_next("Gamma")
    observer.on_next("Delta")
    observer.on_next("Epsilon")
    observer.on_completed()


class PrintObserver(Observer):

    def on_next(self, value):
        DEBUG_MSG("Received {0}".format(value))

    def on_completed(self):
        DEBUG_MSG("Done!")

    def on_error(self, error):
        DEBUG_MSG("Error Occurred: {0}".format(error))

class SkillSystem(GongFaSystem):
    def __init__(self):
        DEBUG_MSG("SkillSystem:__init__")
        GongFaSystem.__init__(self)
        self.canCastSkill = True
        self.canReceiveSkill = True
        self.nameToTimerIdsDict = {}
        self.timerIdToNameDict = {}
        self.lastUserData = 100

        source = Observable.create(push_five_strings)
        source.subscribe(PrintObserver())

        self.onEvent("testEvent", lambda evt: DEBUG_MSG("onEvent " + str(evt["eventName"])))
        self.publish({
            "eventName": "testEvent",
            "arg1": "arg"
            })

    def requestCastSkill(self, exposed, skillName, argsString):
        if exposed != self.id:
            return
        if self.canCastSkill is False:
            return

        strList = skillName.split(":")

        if self.haveLearnedSkill(strList[0], strList[1]) is False:
            DEBUG_MSG("you have not learned the skill")
            return

        mySkillData = self.gongFaList[strList[0]][strList[1]]

        skillData = gongfa_data.data[strList[0]][strList[1]]              # 技能信息
        skillMinSp = skillData["levelSpLimit"][mySkillData["skill_level"]]     # 使用这个技能最少需要的灵力值
        if self.MSP < skillMinSp:
            return

        exec("self.skill = " + skillData["class"] + "(self, argsString, strList[0], strList[1])")
        self.canMove = False
        self.moveToPointSample(self.position, 20)
        singTime = self.skill.startSing()
        self.allClients.OnSkillStartSing(singTime)
        self.addTimer(singTime, 0, 98)

    def addSkillControlTimer(self, timerType, firstTime, repeatOffset, scriptString, operationType):
        DEBUG_MSG("SkillSystem:addSkillControlTimer")

        if len(self.timerIdToNameDict) == 0:
            self.lastUserData = 100
        timerId = self.addTimer(firstTime, repeatOffset, self.lastUserData + 1)

        self.timerIdToNameDict[timerId] = timerType

        if timerType in self.nameToTimerIdsDict.keys():
            timerIdList = self.nameToTimerIdsDict[timerType]["timerIdList"]
            if timerIdList is not None:
                timerIdList.append(timerId)
                self.nameToTimerIdsDict[timerType]["timerIdList"] = timerIdList
        else:
            self.nameToTimerIdsDict[timerType] = \
                {
                    "timerIdList": [timerId],
                    "scriptString": scriptString,
                    "operationType": operationType
                }

    def onTimer(self, timerHandle, userData):
        if userData == 98:      # 吟唱定时器
            self.allClients.OnSkillStartCast(self.skill.gongFaName + ":" + str(self.skill.skillName), self.skill.argsString, self.skill.startCast())
            castTime = self.skill.startCast()
            self.addTimer(castTime, 0, 99)
            self.delTimer(timerHandle)
            pass
        if userData == 99:      # 施法定时器
            self.skill.cast()
            self.canMove = True
            self.allClients.OnSkillEndCast(self.skill.gongFaName + ":" + str(self.skill.skillName), self.skill.argsString)
            self.delTimer(timerHandle)
            pass

        # 持续状态效果、瞬时性效果

        if userData > 100:
            timerType = self.timerIdToNameDict[timerHandle]

            exec(self.nameToTimerIdsDict[timerType]["scriptString"])

            timerIdList = self.nameToTimerIdsDict[timerType]["timerIdList"]
            timerIdList.remove(timerHandle)
            if len(timerIdList) == 0:
                del self.nameToTimerIdsDict[timerType]
            else:
                self.nameToTimerIdsDict[timerType]["timerIdList"] = timerIdList

            del self.timerIdToNameDict[timerHandle]
            self.delTimer(timerHandle)

    def startIceFrozen(self):
        DEBUG_MSG("SkillSystem:startIceFrozen")
        self.allClients.StartIceFrozen()
        pass

    def endIceFrozen(self):
        DEBUG_MSG("SkillSystem:endIceFrozen")
        self.allClients.EndIceFrozen()
        pass
