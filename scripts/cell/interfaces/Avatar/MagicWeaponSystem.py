# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from KTween.KTweenEnum import KTweenEnum




class MagicWeaponSystem:
    def __init__(self):
        DEBUG_MSG("MagicWeaponSystem:__init__")
        if not hasattr(self, "magicWeaponList"):
            self.magicWeaponList = {}


    def addMagicWeapon(self, magicWeaponID):
        DEBUG_MSG("MagicWeaponSystem:addMagicWeapon")
        #self.magicWeaponList[]
