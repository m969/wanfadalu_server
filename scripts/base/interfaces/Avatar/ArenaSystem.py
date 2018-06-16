# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *




class ArenaSystem:
    def __init__(self):
        # DEBUG_MSG("ArenaSystem:__init__")
        pass


    def requestRankingList(self):
        DEBUG_MSG("ArenaSystem:requestRankingList")
        KBEngine.globalData["RankingListManager"].requestRankingList(self)


    def onRequestRankingListReturn(self, rankingList):
        DEBUG_MSG("ArenaSystem:requestRankingList")
        self.client.OnRequestRankingListReturn(rankingList)


    def requestSelfRanking(self):
        DEBUG_MSG("ArenaSystem:requestSelfRanking")
        KBEngine.globalData["RankingListManager"].requestAvatarRanking(self, self.databaseID)


    def onRequestSelfRankingReturn(self, rankingInfo):
        DEBUG_MSG("ArenaSystem:onRequestSelfRankingReturn")
        self.client.OnRequestSelfRankingReturn(rankingInfo)
