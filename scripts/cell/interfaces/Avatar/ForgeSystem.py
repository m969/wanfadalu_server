# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from KTween.KTweenEnum import KTweenEnum
import json
import PyDatas.forge_config_Table as forge_config_Table

local_materialTable = {}
for itemID, itemForgeInfo in forge_config_Table.datas.items():
    materialList = itemForgeInfo["materialList"]
    materialList.sort()
    materialList_json = json.dumps(materialList)
    if materialList_json not in local_materialTable:
        local_materialTable[materialList_json] = []
    local_materialTable[materialList_json].append(itemID)




class ForgeSystem:
    def __init__(self):
        DEBUG_MSG("ForgeSystem:__init__")


    def requestTargetItemList(self, exposed, itemUUIDList_json):
        DEBUG_MSG("ForgeSystem:requestTargetItemList")
        if exposed != self.id:
            return
        itemUUIDList = json.loads(itemUUIDList_json)
        itemIDList = []
        for index, itemUUID in enumerate(itemUUIDList):
            if itemUUID not in self.propList:
                return
            itemID = self.propList[itemUUID]["id"]
            itemIDList.append(itemID)
        itemIDList.sort()
        itemIDList_json = json.dumps(itemIDList)
        targetItemList = local_materialTable.get(itemIDList_json, [])
        targetItemList_json = json.dumps(targetItemList)
        self.client.OnTargetItemListReturn(targetItemList_json)


    def requestForge(self, exposed, itemUUIDList_json, targetItemID):
        DEBUG_MSG("ForgeSystem:requestForge")
        if exposed != self.id:
            return
        itemUUIDList = json.loads(itemUUIDList_json)
        itemIDList = []
        for index, itemUUID in enumerate(itemUUIDList):
            if itemUUID not in self.propList:
                return
            itemID = self.propList[itemUUID]["id"]
            itemIDList.append(itemID)
        materialList = forge_config_Table.datas[targetItemID]
        setList = list(set(itemIDList)^set(materialList))      #   求差集
        if setList != []:
            return
        self.addPropByID(targetItemID)
        for itemUUID in itemUUIDList:
            self.removeProp(itemUUID)
        self.client.OnRequestForgeResult(1)
