# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import datetime
import math
from interfaces.WorldManager.SpacesManager import SpacesManager
from interfaces.WorldManager.CombatBulletinManager import CombatBulletinManager
from interfaces.WorldManager.RankingListManager import RankingListManager
from interfaces.WorldManager.SectsManager import SectsManager




class WorldManager(KBEngine.Base, SpacesManager, CombatBulletinManager, RankingListManager, SectsManager):
    def __init__(self):
        DEBUG_MSG("WorldManager:__init__")
        KBEngine.Base.__init__(self)
        SpacesManager.__init__(self)
        CombatBulletinManager.__init__(self)
        RankingListManager.__init__(self)
        SectsManager.__init__(self)
        KBEngine.globalData["WorldManager"] = self


    def onTimer(self, timerHandle, userData):
        #CombatBulletinManager.onTimer(self, timerHandle, userData)
        pass
