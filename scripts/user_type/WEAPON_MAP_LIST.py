# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *




class TWeaponMap(dict):
    def __init__(self):
        dict.__init__(self)

    def asDict(self):
        fixedDict = {}
        fixedDict["index"] = self["index"]
        fixedDict["propUUID"] = self["propUUID"]
        return fixedDict

    def createFromDict(self, dictData):
        self["index"] = dictData["index"]
        self["propUUID"] = dictData["propUUID"]
        return self

class WEAPON_MAP_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dic):
        return TWeaponMap().createFromDict(dic)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, TWeaponMap)

weapon_map_inst = WEAPON_MAP_PICKLER()




class TWeaponMapList(dict):
    def __init__(self):
        dict.__init__(self)

    def asDict(self):
        values = []
        for key, value in self.items():
            values.append(value)
        fixedDict = {}
        fixedDict["values"] = values
        return fixedDict

    def createFromDict(self, dictData):
        values = dictData["values"]
        for value in values:
            self[value["index"]] = value
        return self

class WEAPON_MAP_LIST_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dic):
        return TWeaponMapList().createFromDict(dic)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, TWeaponMapList)

weapon_map_list_inst = WEAPON_MAP_LIST_PICKLER()
