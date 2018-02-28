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
        winnerName = matchResult["winnerInfo"]["name"]
        loserDBID = matchResult["loserInfo"]["dbid"]
        loserName = matchResult["loserInfo"]["name"]
        winnerMatchInfo = self.rankingList.get(winnerDBID)
        loserMatchInfo = self.rankingList.get(loserDBID)
        if winnerMatchInfo is None:
            winnerMatchInfo = TAvatarMatchInfo()
            winnerMatchInfo["avatarDBID"] = winnerDBID
            winnerMatchInfo["avatarName"] = winnerName
            winnerMatchInfo["matchAmount"] = 1
            winnerMatchInfo["winAmount"] = 1
            self.rankingList[winnerDBID] = winnerMatchInfo
        else:
            winnerMatchInfo["matchAmount"] = winnerMatchInfo["matchAmount"] + 1
            winnerMatchInfo["winAmount"] = winnerMatchInfo["winAmount"] + 1
        if loserMatchInfo is None:
            loserMatchInfo = TAvatarMatchInfo()
            loserMatchInfo["avatarDBID"] = loserDBID
            loserMatchInfo["avatarName"] = loserName
            loserMatchInfo["matchAmount"] = 1
            loserMatchInfo["winAmount"] = 0
            self.rankingList[loserDBID] = loserMatchInfo
        else:
            loserMatchInfo["matchAmount"] = loserMatchInfo["matchAmount"] + 1


    def requestRankingList(self, avatarCall):
        DEBUG_MSG("RankingListManager:requestRankingList")
        avatarCall.onRequestRankingListReturn(self.rankingList)


    def requestAvatarRanking(self, avatarCall, avatarDBID):
        DEBUG_MSG("RankingListManager:requestAvatarRanking")
        avatarCall.onRequestSelfRankingReturn(self.rankingList[avatarDBID])
