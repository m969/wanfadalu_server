# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from PROP_LIST import TProp
from PROP_LIST import TPropList
import json
import uuid
import PyDatas.prop_config_Table as prop_config_Table




class PropSystem:
    def __init__(self):
        DEBUG_MSG("PropSystem:__init__")
        if len(self.propList) == 0:
            self.addPropByID(1001)
            self.addPropByID(1002)
            self.addPropByID(1003)
            self.addPropByID(1004)
        DEBUG_MSG(self.propList)


    def newPropByID(self, propID):
        DEBUG_MSG("PropSystem:newPropByID")
        propData = prop_config_Table.datas[propID]
        propData = json.dumps(propData)
        return self.newPropByData(propData)


    def newPropByData(self, propData):
        DEBUG_MSG("PropSystem:newPropByData")
        prop = TProp()
        prop["propUUID"] = str(uuid.uuid1())
        prop["propData"] = propData
        return prop


    def addPropByID(self, propID):
        DEBUG_MSG("PropSystem:addPropByID")
        prop = self.newPropByID(propID)
        self.addProp(prop)


    def addProp(self, prop):
        DEBUG_MSG("PropSystem:addProp")
        self.propList[prop["propUUID"]] = prop
        self.propList = self.propList


    def removeProp(self, propUUID):
        DEBUG_MSG("PropSystem:removeProp")
        del self.propList[propUUID]
