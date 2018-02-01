# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import datetime
import math
from RANKING_LIST import TAvatarMatchInfo
from RANKING_LIST import TRankingList




class RankingListManager:
    def __init__(self):
        DEBUG_MSG("RankingListManager:__init__")
        if not hasattr(self, "rankingList"):
            self.rankingList = TRankingList()
        KBEngine.globalData["RankingListManager"] = self


    def addNewMatchResult(self, matchResult):
        DEBUG_MSG("RankingListManager:addNewMatchResult")
        winnerDBID = matchResult["winnerInfo"]["dbid"]
        loserDBID = matchResult["loserInfo"]["dbid"]
        winnerMatchInfo = self.rankingList.get(winnerDBID)
        loserMatchInfo = self.rankingList.get(loserDBID)
        if winnerMatchInfo is None:
            self.rankingList[winnerDBID] = TAvatarMatchInfo()
            self.rankingList[winnerDBID]["avatarDBID"] = winnerDBID
            self.rankingList[winnerDBID]["matchAmount"] = 1
            self.rankingList[winnerDBID]["winAmount"] = 1
        else:
            winnerMatchInfo["matchAmount"] = winnerMatchInfo["matchAmount"] + 1
            winnerMatchInfo["winAmount"] = winnerMatchInfo["winAmount"] + 1
        if loserMatchInfo is None:
            self.rankingList[loserDBID] = TAvatarMatchInfo()
            self.rankingList[loserDBID]["avatarDBID"] = loserDBID
            self.rankingList[loserDBID]["matchAmount"] = 1
            self.rankingList[loserDBID]["winAmount"] = 0
        else:
            loserMatchInfo["matchAmount"] = loserMatchInfo["matchAmount"] + 1


    def requestRankingList(self):
        DEBUG_MSG("RankingListManager:requestRankingList")


    def requestAvatarRanking(self, avatarDBID):
        DEBUG_MSG("RankingListManager:requestAvatarRanking")
