# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *




class TSkill(dict):
    def __init__(self):
        dict.__init__(self)

    def asDict(self):
        return self

    def createFromDict(self, dictData):
        self["skillIndex"] = dictData["skillIndex"]
        self["skillLevel"] = dictData["skillLevel"]
        return self

class SKILL_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dic):
        return TSkill().createFromDict(dic)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, TSkill)

skill_inst = SKILL_PICKLER()




class TGongFa(dict):
    def __init__(self):
        dict.__init__(self)

    def asDict(self):
        fixedDict = {}
        fixedDict["values"] = self["values"]
        fixedDict["index"] = self["index"]
        fixedDict["gongFaID"] = self["gongFaID"]
        return fixedDict

    def createFromDict(self, dictData):
        self["values"] = dictData["values"]
        self["index"] = dictData["index"]
        self["gongFaID"] = dictData["gongFaID"]
        return self

class GONGFA_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dic):
        return TGongFa().createFromDict(dic)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, TGongFa)

gongfa_inst = GONGFA_PICKLER()




class TGongFaList(dict):
    def __init__(self):
        dict.__init__(self)

    def asDict(self):
        """
        转换为固定字典格式存到数据库
        """
        # DEBUG_MSG("asDict " + str(self))
        gongFaList = []
        for gongFaID, gongFa in self.items():
            temp_gongFa = TGongFa()
            temp_gongFa["values"] = []
            for skillIndex, skillInfo in gongFa["skillList"].items():
                temp_skillInfo = TSkill()
                temp_skillInfo["skillIndex"] = skillIndex
                temp_skillInfo["skillLevel"] = skillInfo["skillLevel"]
                temp_gongFa["values"].append(temp_skillInfo)
            temp_gongFa["gongFaID"] = gongFaID
            temp_gongFa["index"] = gongFa["index"]
            gongFaList.append(temp_gongFa)
        fixedDict = {}
        fixedDict["values"] = gongFaList
        return fixedDict

    def createFromDict(self, dictData):
        """
        从数据库取出固定字典并转换为脚本内存格式
        """
        # DEBUG_MSG("createFromDict " + str(dictData))
        gongFaList = dictData["values"]
        for gongFa in gongFaList:
            temp_gongFa = {}
            temp_gongFa["skillList"] = {}
            for skillInfo in gongFa["values"]:
                temp_skillInfo = {}
                temp_skillInfo["skillLevel"] = skillInfo["skillLevel"]
                temp_gongFa["skillList"][skillInfo["skillIndex"]] = temp_skillInfo
            temp_gongFa["index"] = gongFa["index"]
            temp_gongFa["gongFaID"] = gongFa["gongFaID"]
            self[gongFa["gongFaID"]] = temp_gongFa
        return self

class GONGFA_LIST_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dic):
        return TGongFaList().createFromDict(dic)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, TGongFaList)

gongfa_list_inst = GONGFA_LIST_PICKLER()
