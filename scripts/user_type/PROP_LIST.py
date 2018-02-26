# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *




class TProp(dict):
    def __init__(self):
        dict.__init__(self)

    def asDict(self):
        fixedDict = {}
        fixedDict["propUUID"] = self["propUUID"]
        fixedDict["propData"] = self["propData"]
        return fixedDict

    def createFromDict(self, dictData):
        self["propUUID"] = dictData["propUUID"]
        self["propData"] = dictData["propData"]
        return self

class PROP_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dic):
        return TProp().createFromDict(dic)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, TProp)

prop_inst = PROP_PICKLER()




class TPropList(dict):
    def __init__(self):
        dict.__init__(self)

    def asDict(self):
        propList = []
        for propUUID, prop in self.items():
            propList.append(prop)
        fixedDict = {}
        fixedDict["values"] = propList
        return fixedDict

    def createFromDict(self, dictData):
        propList = dictData["values"]
        for prop in propList:
            self[prop["propUUID"]] = prop
        return self

class PROP_LIST_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dic):
        return TPropList().createFromDict(dic)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, TPropList)

prop_list_inst = PROP_LIST_PICKLER()
