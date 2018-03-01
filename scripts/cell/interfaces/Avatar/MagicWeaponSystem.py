# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from KTween.KTweenEnum import KTweenEnum
from WEAPON_MAP_LIST import TWeaponMap
from WEAPON_MAP_LIST import TWeaponMapList
import json




class MagicWeaponSystem:
    def __init__(self):
        DEBUG_MSG("MagicWeaponSystem:__init__")
        propUUIDList = self.getPropUUIDList()
        for propUUID, prop in self.propList.items():
            propData = json.loads(prop["propData"])
            if propData["type"] == 2:
                if propUUID not in propUUIDList:
                    self.onGetMagicWeapon(propUUID, propData)


    def calculateFreeIndexSet(self):
        DEBUG_MSG("MagicWeaponSystem:calculateFreeIndexSet")
        freeIndexSet = []
        removeIndexSet = []
        for i in range(0, 9):
            freeIndexSet.append(i)
        freeIndexSet.reverse()
        for index, weaponMap in self.magicWeaponList.items():
            if weaponMap["propUUID"] not in self.propList:
                removeIndexSet.append(index)
                continue
            freeIndexSet.remove(index)
        for index in removeIndexSet:
            del self.magicWeaponList[index]
        return freeIndexSet


    def getPropUUIDList(self):
        DEBUG_MSG("MagicWeaponSystem:getPropUUIDList")
        propUUIDList = []
        for index, weaponMap in self.magicWeaponList.items():
            propUUIDList.append(weaponMap["propUUID"])
        return propUUIDList


    def onAddProp(self, prop):
        DEBUG_MSG("MagicWeaponSystem:onAddProp")
        propData = json.loads(prop["propData"])
        if propData["type"] == 2:
            self.onGetMagicWeapon(prop["propUUID"], propData)


    def onGetMagicWeapon(self, propUUID, weaponData):
        DEBUG_MSG("MagicWeaponSystem:onGetMagicWeapon")
        weaponMap = TWeaponMap()
        freeIndexSet = self.calculateFreeIndexSet()
        weaponMap["index"] = freeIndexSet.pop()
        weaponMap["propUUID"] = propUUID
        self.magicWeaponList[weaponMap["index"]] = weaponMap
