# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from KTween.KTweenEnum import KTweenEnum
import gongfa_data
from GONGFA_LIST import TGongFaList
from GONGFA_LIST import TGongFa
from GONGFA_LIST import TSkill


class GongFaSystem:
    def __init__(self):
        DEBUG_MSG("GongFaSystem:__init__")
        if not self.haveLearnedGongFa("PrimaryArrowGongFa"):
            self.learnGongFa("PrimaryArrowGongFa")
        if not self.haveLearnedGongFa("基础冰系法术"):
            self.learnGongFa("基础冰系法术")
        if not self.haveLearnedGongFa("基础土系法术"):
            self.learnGongFa("基础土系法术")

    def learnGongFa(self, gongFaName):
        # 学习功法
        DEBUG_MSG("GaongFaSystem:learnGongFa")
        if self.haveLearnedGongFa(gongFaName):
            DEBUG_MSG("You have learned this gongFa")
        else:
            DEBUG_MSG("learned this gongFa")
            if gongFaName in gongfa_data.data.keys():
                temp_gangFa = {}
                for skill_name, skill_data in gongfa_data.data[gongFaName].items():
                    aSkill = { 'skill_level': 1 }
                    temp_gangFa[skill_name] = aSkill
                self.gongFaList[gongFaName] = temp_gangFa

    def haveLearnedGongFa(self, gongFaName):
        if gongFaName in self.gongFaList.keys():
            return True
        return False

    def haveLearnedSkill(self, gongFaName, skillName):
        if gongFaName in self.gongFaList.keys():
            if skillName in self.gongFaList[gongFaName].keys():
                return True
        return False
