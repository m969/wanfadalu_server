# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from PROP_LIST import TProp
from PROP_LIST import TPropList
import json
import uuid
import PyDatas.prop_config_Table as prop_config_Table
import PyDatas.store_config_Table as store_config_Table




class PropSystem:
    def __init__(self):
        DEBUG_MSG("PropSystem:__init__")
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
        self.onAddProp(prop)


    def onAddProp(self, prop):
        DEBUG_MSG("PropSystem:onAddProp")


    def removeProp(self, propUUID):
        DEBUG_MSG("PropSystem:removeProp")
        del self.propList[propUUID]


    def requestPullStorePropList(self, storeNpcID):
        DEBUG_MSG("PropSystem:requestPullStorePropList")
        self.client.onPullStorePropListReturn(store_config_Table.datas[storeNpcID]["propList"])


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
