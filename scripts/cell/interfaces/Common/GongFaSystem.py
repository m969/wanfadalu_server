# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from KTween.KTweenEnum import KTweenEnum
import PyDatas.gongFa_config_Table as gongFa_config_Table
import PyDatas.skill_config_Table as skill_config_Table
from GONGFA_LIST import TGongFaList
from GONGFA_LIST import TGongFa
from GONGFA_LIST import TSkill
from rx import Observable, Observer
from rx.subjects import Subject

local_gongFaMap = {}
for skillID, skillInfo in skill_config_Table.datas.items():
    gongFaID = skillInfo["gongFa"]
    if gongFaID not in local_gongFaMap:
        local_gongFaMap[gongFaID] = []
    local_gongFaMap[gongFaID].append(skillID)




class GongFaSystem:
    def __init__(self):
        DEBUG_MSG("GongFaSystem:__init__")
        self.gongFaIndexList = []
        for i in range(0, 9):
            self.gongFaIndexList.insert(0, i)
        for gongFaID, gongFa in self.gongFaList.items():
            self.gongFaIndexList.remove(gongFa["index"])
        # if not self.haveLearnedGongFa(1001):
        #     self.learnGongFa(1001)
        # if not self.haveLearnedGongFa(1002):
        #     self.learnGongFa(1002)
        # if not self.haveLearnedGongFa(1003):
        #     self.learnGongFa(1003)


    def learnGongFa(self, gongFaID):
        """
        学习功法
        """
        DEBUG_MSG("GaongFaSystem:learnGongFa")
        if self.haveLearnedGongFa(gongFaID):
            DEBUG_MSG("You have learned gongFa " + str(gongFaID))
        else:
            DEBUG_MSG("learn gongFa " + str(gongFaID))
            if gongFaID in gongFa_config_Table.datas.keys():
                temp_gangFa = {}
                temp_gangFa["index"] = self.gongFaIndexList.pop()
                temp_gangFa["skillList"] = {}
                for skillID in local_gongFaMap[gongFaID]:
                    aSkill = { 'skillLevel': 1 }
                    temp_gangFa["skillList"][skillID % 10] = aSkill
                self.gongFaList[gongFaID] = temp_gangFa
                self.gongFaList = self.gongFaList


    def haveLearnedGongFa(self, gongFaID):
        if gongFaID in self.gongFaList.keys():
            return True
        return False


    def haveLearnedSkill(self, gongFaID, skillName):
        if gongFaID in self.gongFaList.keys():
            if skillName in self.gongFaList[gongFaID]["skillList"].keys():
                return True
        return False
