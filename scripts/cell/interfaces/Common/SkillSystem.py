# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from strategy.skill_strategy import *
import avatar_skill_data
import gongfa_data
from GONGFA_LIST import TGongFaList
from GONGFA_LIST import TSkill
from interfaces.Common.GongFaSystem import GongFaSystem
from rx import Observable, Observer




class SkillSystem(GongFaSystem):
    def __init__(self):
        DEBUG_MSG("SkillSystem:__init__")
        GongFaSystem.__init__(self)
        self.canCastSkill = True
        self.canReceiveSkill = True
        self.nameToTimerIdsDict = {}
        self.timerIdToNameDict = {}
        self.lastUserData = 100


    def requestCastSkill(self, exposed, gongFaID, skillIndex, argsString):
        DEBUG_MSG("SkillSystem:requestCastSkill")
        if exposed != self.id:
            return
        if self.canCastSkill is False:
            return
        if self.haveLearnedSkill(gongFaID, skillIndex) is False:
            DEBUG_MSG("Error! You have not learned the skill.")
            return
        mySkillData = self.gongFaList[gongFaID][skillIndex]
        skillData = gongfa_data.data[gongFaID]["skillList"][skillIndex]              # 技能信息
        skillMinSp = skillData["levelSpLimit"][mySkillData["skillLevel"]]     # 使用这个技能最少需要的灵力值
        if self.MSP < skillMinSp:
            return
        exec("self.skill = " + skillData["class"] + "(self, argsString, gongFaID, skillIndex)")
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
            self.allClients.OnSkillStartCast(str(self.skill.gongFaID) + ":" + str(self.skill.skillIndex), self.skill.argsString, self.skill.startCast())
            castTime = self.skill.startCast()
            self.addTimer(castTime, 0, 99)
            self.delTimer(timerHandle)
        if userData == 99:      # 施法定时器
            self.skill.cast()
            self.canMove = True
            self.allClients.OnSkillEndCast(str(self.skill.gongFaID) + ":" + str(self.skill.skillIndex), self.skill.argsString)
            self.delTimer(timerHandle)
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


    def endIceFrozen(self):
        DEBUG_MSG("SkillSystem:endIceFrozen")
        self.allClients.EndIceFrozen()
