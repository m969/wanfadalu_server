# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *




class TIdDbidMap(dict):
    def __init__(self):
        dict.__init__(self)

    def asDict(self):
        return self

    def createFromDict(self, dictData):
        self["id"] = dictData["id"]
        self["dbid"] = dictData["dbid"]
        return self

class ID_DBID_MAP_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dic):
        return TIdDbidMap().createFromDict(dic)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, TIdDbidMap)

id_dbid_map_inst = ID_DBID_MAP_PICKLER()




class TIdDbidMapList(dict):
    def __init__(self):
        dict.__init__(self)

    def asDict(self):
        mapList = []
        for id, mapInfo in self.items():
            mapList.append(mapInfo)
        fixedDict = {}
        fixedDict["values"] = mapList
        return fixedDict

    def createFromDict(self, dictData):
        mapList = dictData["values"]
        for mapInfo in mapList:
            self[mapInfo["id"]] = mapInfo
        return self

class ID_DBID_MAP_LIST_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dic):
        return TIdDbidMapList().createFromDict(dic)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, TIdDbidMapList)

id_dbid_map_list_inst = ID_DBID_MAP_LIST_PICKLER()
