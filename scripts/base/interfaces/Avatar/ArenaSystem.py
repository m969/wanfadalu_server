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
        KBEngine.globalData["RankingListManager"].requestRankingList(self)


    def onRequestRankingListReturn(self, rankingList):
        DEBUG_MSG("ArenaSystem:requestRankingList")
        self.client.OnRequestRankingListReturn(rankingList)


    def requestSelfRanking(self, exposed):
        DEBUG_MSG("ArenaSystem:requestSelfRanking")
        if exposed != self.id:
            return
        KBEngine.globalData["RankingListManager"].requestAvatarRanking(self, self.id)


    def onRequestSelfRankingReturn(self, rankingInfo):
        DEBUG_MSG("ArenaSystem:onRequestSelfRankingReturn")
        self.client.OnRequestSelfRankingReturn(rankingInfo)
