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
        self.keyPriority = ["97", "115", "100", "102", "103", "104", "106", "107", "108"]
        if self.gongFaKeyOptions == "None":
            temp_gongFaKeyOptions = {
                "97": 0,
                "115": 0,
                "100": 0,
                "102": 0,
                "103": 0,
                "104": 0,
                "106": 0,
                "107": 0,
                "108": 0
            }
            self.gongFaKeyOptions = json.dumps(temp_gongFaKeyOptions)


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
                temp_gongFaKeyOptions = json.loads(self.gongFaKeyOptions)
                DEBUG_MSG("temp_gongFaKeyOptions " + str(temp_gongFaKeyOptions))
                for key in self.keyPriority:
                    if temp_gongFaKeyOptions[key] == 0:
                        temp_gongFaKeyOptions[key] = gongFaID
                        break
                self.gongFaKeyOptions = json.dumps(temp_gongFaKeyOptions)
                temp_gangFa = {}
                temp_gangFa["index"] = self.gongFaIndexList.pop()
                temp_gangFa["skillList"] = {}
                for skillID in local_gongFaMap[gongFaID]:
                    aSkill = { 'skillLevel': 1 }
                    temp_gangFa["skillList"][skillID % 10] = aSkill
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
            temp_gongFaKeyOptions = json.loads(self.gongFaKeyOptions)
            temp_gangFa = self.gongFaList[gongFaID]
            self.gongFaIndexList.insert(0, temp_gangFa["index"])
            for keyCode, _gongFaID in temp_gongFaKeyOptions.items():
                if gongFaID == _gongFaID:
                    temp_gongFaKeyOptions[keyCode] = 0
                    break
            self.gongFaKeyOptions = json.dumps(temp_gongFaKeyOptions)
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
