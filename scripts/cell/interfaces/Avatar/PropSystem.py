# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from PROP_LIST import TProp
from PROP_LIST import TPropList
from STORE_PROP_LIST import TStoreProp
from STORE_PROP_LIST import TStorePropList
import json
import PyDatas.prop_config_Table as prop_config_Table
import PyDatas.store_config_Table as store_config_Table




class PropSystem:
    def __init__(self):
        DEBUG_MSG("PropSystem:__init__")
        self.freePropIndexSet = []
        for i in range(0, 16):
            self.freePropIndexSet.insert(0, i)
        for propUUID, prop in self.propList.items():
            self.freePropIndexSet.remove(prop["index"])
        DEBUG_MSG(self.freePropIndexSet)
        if len(self.propList) == 0:
            self.addPropByID(1001)
            self.addPropByID(1002)
            self.addPropByID(1003)
            self.addPropByID(1004)


    def newPropByID(self, propID):
        DEBUG_MSG("PropSystem:newPropByID")
        propData = prop_config_Table.datas[propID]
        propData = json.dumps(propData)
        return self.newPropByData(propData)


    def newPropByData(self, propData):
        DEBUG_MSG("PropSystem:newPropByData")
        prop = TProp()
        prop["propUUID"] = KBEngine.genUUID64()
        prop["index"] = self.freePropIndexSet.pop()
        prop["propData"] = propData
        return prop


    def addPropByID(self, propID):
        DEBUG_MSG("PropSystem:addPropByID")
        prop = self.newPropByID(propID)
        self.addProp(prop)


    def addProp(self, prop):
        DEBUG_MSG("PropSystem:addProp")
        self.propList[prop["propUUID"]] = prop
        self.onAddProp(prop)


    def onAddProp(self, prop):
        DEBUG_MSG("PropSystem:onAddProp")


    def removeProp(self, propUUID):
        DEBUG_MSG("PropSystem:removeProp")
        del self.propList[propUUID]
        self.onRemoveProp(propUUID)


    def onRemoveProp(self, propUUID):
        DEBUG_MSG("PropSystem:onRemoveProp")


    def requestPullStorePropList(self, exposed, storeNpcID):
        DEBUG_MSG("PropSystem:requestPullStorePropList")
        if exposed != self.id:
            return
        storePropList = TStorePropList()
        storePropList.extend(store_config_Table.datas[storeNpcID]["propList"])
        self.client.OnPullStorePropListReturn(store_config_Table.datas[storeNpcID]["propList"])


    def requestBuyProp(self, storeNpcID, propIndex):
        DEBUG_MSG("PropSystem:requestBuyProp")
        storeNpc = KBEngine.entities.get(storeNpcID)
        if not storeNpc:
            return
        storePropList = store_config_Table.datas[storeNpcID]["propList"]
        if propIndex not in storePropList:
            return
        self.buyProp(storePropList[propIndex][0], storePropList[propIndex][1])


    def buyProp(self, propID, lingshiNum):
        DEBUG_MSG("PropSystem:buyProp")
        if lingshiNum > self.lingshiAmount:
            return
        self.lingshiAmount = self.lingshiAmount - lingshiNum
        self.addPropByID(propID)
