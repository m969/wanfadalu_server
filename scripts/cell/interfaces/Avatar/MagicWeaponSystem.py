# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from KTween.KTweenEnum import KTweenEnum
# from PROP_LIST import TProp
from PROP_LIST import TPropList
import json
import PyDatas.prop_config_Table as prop_config_Table
import PyDatas.store_config_Table as store_config_Table
import copy




class MagicWeaponSystem:
    def __init__(self):
        DEBUG_MSG("MagicWeaponSystem:__init__")
        self.freeIndexSet = []
        for i in range(0, 9):
            self.freeIndexSet.insert(0, i)
        for propUUID, prop in self.magicWeaponList.items():
            self.freeIndexSet.remove(prop["index"])
        DEBUG_MSG(self.freeIndexSet)


    def onAddProp(self, prop):
        DEBUG_MSG("MagicWeaponSystem:onAddProp")
        propData = json.loads(prop["propData"])
        if propData["type"] == 2:
            self.addMagicWeapon(prop)


    def onRemoveProp(self, propUUID):
        DEBUG_MSG("MagicWeaponSystem:onRemoveProp")
        self.removeMagicWeapon(propUUID)


    def addMagicWeapon(self, prop):
        DEBUG_MSG("MagicWeaponSystem:addMagicWeapon")
        # weaponProp = TProp()
        weaponProp = copy.deepcopy(prop)
        weaponProp["index"] = self.freeIndexSet.pop()
        # weaponProp["id"] = self.freeIndexSet.pop()
        # weaponProp["propUUID"] = propUUID
        # weaponProp["propData"] = jsonData
        self.magicWeaponList[weaponProp["propUUID"]] = weaponProp
        self.magicWeaponList = self.magicWeaponList


    def removeMagicWeapon(self, propUUID):
        DEBUG_MSG("MagicWeaponSystem:addMagicWeapon")
        index = self.magicWeaponList[propUUID]["index"]
        self.freeIndexSet.insert(0, index)
        del self.magicWeaponList[propUUID]
