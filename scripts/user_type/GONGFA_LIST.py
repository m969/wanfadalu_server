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
        fixedDict["gongFaID"] = self["gongFaID"]
        return fixedDict

    def createFromDict(self, dictData):
        self["values"] = dictData["values"]
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
        gongFaList = []
        for gongFaName, gongFa in self.items():
            temp_gongFa = TGongFa()
            temp_gongFa["values"] = []
            for skillIndex, skillInfo in gongFa.items():
                temp_skillInfo = TSkill()
                temp_skillInfo["skillIndex"] = skillIndex
                temp_skillInfo["skillLevel"] = skillInfo["skillLevel"]
                temp_gongFa["values"].append(temp_skillInfo)
                temp_gongFa["gongFaID"] = gongFaName
            gongFaList.append(temp_gongFa)
        fixedDict = {}
        fixedDict["values"] = gongFaList
        return fixedDict

    def createFromDict(self, dictData):
        """
        从数据库取出固定字典并转换为脚本内存格式
        """
        gongFaList = dictData["values"]
        for gongFa in gongFaList:
            temp_gongFa = {}
            for skillInfo in gongFa["values"]:
                temp_skillInfo = {}
                temp_skillInfo["skillLevel"] = skillInfo["skillLevel"]
                temp_gongFa[skillInfo["skillIndex"]] = temp_skillInfo
            self[gongFa["gongFaID"]] = temp_gongFa
        return self

class GONGFA_LIST_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dic):
        """
        // 此接口被C++底层调用
        // 引擎将数据交给脚本层管理，脚本层可以将这个字典重定义为任意类型
        // dct中的数据为 {"k1" : 0, "k2" : 0}, 它就是一个字典，包含了2个固定的key
        // 且值一定是符合alias.xml中定义的类型
        // XXX_TYPE().createFromDict接口调用后，返回的是一个list([0, 0])
        // createObjFromDict被调用后，返回的数据将直接赋值到脚本中的变量
        """
        return TGongFaList().createFromDict(dic)

    def getDictFromObj(self, obj):
        """
        // 此接口被C++底层调用
        // 底层需要从脚本层中获取数据，脚本层此时应该将数据结构还原为固定字典
        // list([0, 0]) => {"k1" : 0, "k2" : 0}
        """
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, TGongFaList)

gongfa_list_inst = GONGFA_LIST_PICKLER()
