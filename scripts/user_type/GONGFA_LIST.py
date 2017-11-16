# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class TSkill(dict):
    def __init__(self):
        dict.__init__(self)

    def asDict(self):
        # DEBUG_MSG("TSkill:asDict")
        # DEBUG_MSG(self)
        return self

    def createFromDict(self, dictData):
        # DEBUG_MSG("TSkill:createFromDict")
        # DEBUG_MSG(dictData)

        self["skill_name"] = dictData["skill_name"]
        self["skill_level"] = dictData["skill_level"]
        # self["gongFa_name"] = dictData["gongFa_name"]

        # DEBUG_MSG(self)
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
        # DEBUG_MSG("TGongFa:asDict")
        # DEBUG_MSG(self)

        fixedDict = {}
        fixedDict["values"] = self["values"]
        fixedDict["gongFa_name"] = self["gongFa_name"]
        return fixedDict

    def createFromDict(self, dictData):
        # DEBUG_MSG("TGongFa:createFromDict")
        # DEBUG_MSG(dictData)

        self["values"] = dictData["values"]
        self["gongFa_name"] = dictData["gongFa_name"]

        # DEBUG_MSG(self)
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
        :return:
        """
        # DEBUG_MSG("TGongFaList:asDict")
        # DEBUG_MSG(self)

        gongFaList = []
        for gongFaName, gongFa in self.items():
            temp_gongFa = TGongFa()
            temp_gongFa["values"] = []
            for skill_name, skillInfo in gongFa.items():
                temp_skillInfo = TSkill()
                temp_skillInfo["skill_name"] = skill_name
                temp_skillInfo["skill_level"] = skillInfo["skill_level"]
                temp_gongFa["values"].append(temp_skillInfo)
                temp_gongFa["gongFa_name"] = gongFaName
            gongFaList.append(temp_gongFa)
        fixedDict = {}
        fixedDict["values"] = gongFaList
        return fixedDict

    def createFromDict(self, dictData):
        """
        从数据库取出固定字典并转换为脚本内存格式
        :param dictData:
        :return:
        """
        # DEBUG_MSG("TGongFaList:createFromDict")
        # DEBUG_MSG(dictData)

        gongFaList = dictData["values"]
        for gongFa in gongFaList:
            temp_gongFa = {}
            for skillInfo in gongFa["values"]:
                # temp_gongFa[skillInfo["skill_name"]] = skillInfo["skill_level"]
                temp_skillInfo = {}
                temp_skillInfo["skill_level"] = skillInfo["skill_level"]
                temp_gongFa[skillInfo["skill_name"]] = temp_skillInfo
            self[gongFa["gongFa_name"]] = temp_gongFa

        # DEBUG_MSG(self)
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