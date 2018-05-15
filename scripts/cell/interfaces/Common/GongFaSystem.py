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
import json




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
        self.keyPriority = ["113", "119", "101", "97", "115", "100", "122", "120", "99"]
        if self.skillKeyOptions == "None":
            temp_skillKeyOptions = {
                "113": 0,
                "119": 0,
                "101": 0,
                "97": 0,
                "115": 0,
                "100": 0,
                "122": 0,
                "120": 0,
                "99": 0
            }
            self.skillKeyOptions = json.dumps(temp_skillKeyOptions)


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
                temp_skillKeyOptions = json.loads(self.skillKeyOptions)
                DEBUG_MSG("temp_skillKeyOptions " + str(temp_skillKeyOptions))
                temp_gangFa = {}
                temp_gangFa["index"] = self.gongFaIndexList.pop()
                temp_gangFa["skillList"] = {}
                for skillID in local_gongFaMap[gongFaID]:
                    aSkill = { 'skillLevel': 1 }
                    temp_gangFa["skillList"][skillID % 10] = aSkill
                    for key in self.keyPriority:
                        if temp_skillKeyOptions[key] == 0:
                            temp_skillKeyOptions[key] = skillID
                            break
                self.skillKeyOptions = json.dumps(temp_skillKeyOptions)
                self.gongFaList[gongFaID] = temp_gangFa
                self.gongFaList = self.gongFaList


    def wasteGongFa(self, gongFaID):
        """
        废弃功法
        """
        DEBUG_MSG("GaongFaSystem:wasteGongFa")
        if not self.haveLearnedGongFa(gongFaID):
            DEBUG_MSG("You have not learned gongFa " + str(gongFaID))
        else:
            DEBUG_MSG("waste gongFa " + str(gongFaID))
            temp_skillKeyOptions = json.loads(self.skillKeyOptions)
            temp_gangFa = self.gongFaList[gongFaID]
            self.gongFaIndexList.insert(0, temp_gangFa["index"])
            for skillID in local_gongFaMap[gongFaID]:
                for keyCode, _skillID in temp_skillKeyOptions.items():
                    if skillID == _skillID:
                        temp_skillKeyOptions[keyCode] = 0
                        break
            self.skillKeyOptions = json.dumps(temp_skillKeyOptions)
            del self.gongFaList[gongFaID]
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
