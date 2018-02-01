# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *




class ArenaSystem:
    def __init__(self):
        DEBUG_MSG("ArenaSystem:__init__")


    def requestRankingList(self, exposed):
        DEBUG_MSG("ArenaSystem:requestRankingList")
        if exposed != self.id:
            return
        KBEngine.globalData["RankingListManager"].requestRankingList()
