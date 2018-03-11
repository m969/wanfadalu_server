# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *




class TStoreProp(list):
    def __init__(self):
        list.__init__(self)

    def asDict(self):
        fixedDict = []
        fixedDict["propID"] = self[0]
        fixedDict["propPrice"] = self[1]
        return fixedDict

    def createFromDict(self, dictData):
        self[0] = dictData["propID"]
        self[1] = dictData["propPrice"]
        return self

class PROP_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dic):
        return TStoreProp().createFromDict(dic)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, TStoreProp)

store_prop_inst = PROP_PICKLER()




class TStorePropList(list):
    def __init__(self):
        list.__init__(self)

    def asDict(self):
        # propList = []
        # for prop in self:
        #     propList.append(prop)
        fixedDict = {}
        fixedDict["values"] = self
        return fixedDict

    def createFromDict(self, dictData):
        # propList = dictData["values"]
        # for prop in propList:
        #     self[prop["propUUID"]] = prop
        return dictData["values"]

class PROP_LIST_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dic):
        return TStorePropList().createFromDict(dic)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, TStorePropList)

store_prop_list_inst = PROP_LIST_PICKLER()
