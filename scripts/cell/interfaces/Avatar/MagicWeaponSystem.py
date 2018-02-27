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
        freeIndexSet = []
        removeIndexSet = []
        for i in range(0, 9):
            freeIndexSet.append(i)
        freeIndexSet.reverse()
        propUUIDList = []
        for index, weaponMap in self.magicWeaponList.items():
            propUUIDList.append(weaponMap["propUUID"])
            if weaponMap["propUUID"] not in self.propList:
                removeIndexSet.append(index)
                continue
            freeIndexSet.remove(index)
        for index in removeIndexSet:
            del self.magicWeaponList[index]
        for propUUID, prop in self.propList.items():
            propData = json.loads(prop["propData"])
            if propData["type"] == 2:
                if propUUID not in propUUIDList:
                    weaponMap = TWeaponMap()
                    weaponMap["index"] = freeIndexSet.pop()
                    weaponMap["propUUID"] = prop["propUUID"]
                    self.magicWeaponList[weaponMap["index"]] = weaponMap


    def onGetMagicWeapon(self, magicWeaponTypeID, weaponData):
        DEBUG_MSG("MagicWeaponSystem:onGetMagicWeapon")
        #self.magicWeaponList[]
