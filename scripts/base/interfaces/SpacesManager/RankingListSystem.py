# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import datetime
import math


class RankingListSystem:
    def __init__(self):
        DEBUG_MSG("RankingListSystem:__init__")
        self.rankingList = {}
        self.rankingList.__setitem__(1, { "avatarDBID": 1, "matchAmount": 10, "winAmount": 5 })

    def addNewMatchResult(self, matchResult):
        DEBUG_MSG("RankingListSystem:addNewMatchResult")
        winnerMatchInfo = self.rankingList.get(matchResult["winnerInfo"]["dbid"])
        if winnerMatchInfo is None:
            self.rankingList[matchResult["winnerInfo"]["dbid"]] = { "avatarDBID": matchResult["winnerInfo"]["dbid"], "matchAmount":1, "winAmount": 1 }
        else:
            winnerMatchInfo["matchAmount"] = winnerMatchInfo["matchAmount"] + 1
            winnerMatchInfo["winAmount"] = winnerMatchInfo["winAmount"] + 1
        loserMatchInfo = self.rankingList.get(matchResult["loserInfo"]["dbid"])
        if loserMatchInfo is None:
            self.rankingList[matchResult["loserInfo"]["dbid"]] = { "avatarDBID": matchResult["loserInfo"]["dbid"], "matchAmount":1, "winAmount": 1 }
        else:
            loserMatchInfo["matchAmount"] = loserMatchInfo["matchAmount"] + 1
