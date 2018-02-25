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
        DEBUG_MSG(self.magicWeaponList)
        for propUUID, prop in self.propList.items():
            propData = json.loads(prop["propData"])
            weaponMap = TWeaponMap()
            weaponMap["index"] = len(self.magicWeaponList)
            weaponMap["propUUID"] = prop["propUUID"]
            if propData["type"] == "weapon":
                self.magicWeaponList[weaponMap["index"]] = weaponMap


    def onGetMagicWeapon(self, magicWeaponTypeID, weaponData):
        DEBUG_MSG("MagicWeaponSystem:onGetMagicWeapon")
        #self.magicWeaponList[]
