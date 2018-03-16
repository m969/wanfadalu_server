# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from KTween.KTweenEnum import KTweenEnum
import json
import PyDatas.forge_config_Table as forge_config_Table

local_materialTable = {}
for itemID, materialList in forge_config_Table.datas.items():
    materialList.sort()
    materialList_json = json.dumps(materialList)
    if materialList_json not in local_materialTable:
        local_materialTable[materialList_json] = []
    local_materialTable[materialList_json].append(itemID)




class ForgeSystem:
    def __init__(self):
        DEBUG_MSG("ForgeSystem:__init__")


    def requestTargetItemList(self, itemUUIDList_json):
        DEBUG_MSG("ForgeSystem:requestTargetItemList")
        itemUUIDList = json.loads(itemUUIDList_json)
        itemIDList = []
        for index, itemUUID in enumerate(itemUUIDList):
            if itemUUID not in self.propList:
                return
            itemID = self.propList[itemUUID]["id"]
            itemIDList.append(itemID)
        itemIDList.sort()
        itemIDList_json = json.dumps(itemIDList)
        materialList = local_materialTable.get(itemIDList_json, [])
        self.client.OnTargetItemListReturn(materialList)


    def requestForge(self, itemUUIDList_json, targetItemID):
        DEBUG_MSG("ForgeSystem:requestForge")
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
