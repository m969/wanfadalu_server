# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *




class TAvatarMatchInfo(dict):
    def __init__(self):
        dict.__init__(self)

    def asDict(self):
        return self

    def createFromDict(self, dictData):
        self["avatarDBID"] = dictData["avatarDBID"]
        self["avatarName"] = dictData["avatarName"]
        self["matchAmount"] = dictData["matchAmount"]
        self["winAmount"] = dictData["winAmount"]
        return self

class AVATAR_MATCH_INFO_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dic):
        return TAvatarMatchInfo().createFromDict(dic)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, TAvatarMatchInfo)

avatar_match_info_inst = AVATAR_MATCH_INFO_PICKLER()




class TRankingList(dict):
    def __init__(self):
        dict.__init__(self)

    def asDict(self):
        rankingList = []
        for avatarDBID, avatarMatchInfo in self.items():
            rankingList.append(avatarMatchInfo)
        fixedDict = {}
        fixedDict["values"] = rankingList
        return fixedDict

    def createFromDict(self, dictData):
        rankingList = dictData["values"]
        for avatarMatchInfo in rankingList:
            self[avatarMatchInfo["avatarDBID"]] = avatarMatchInfo
        return self

class RANKING_LIST_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dic):
        return TRankingList().createFromDict(dic)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, TRankingList)

ranking_list_inst = RANKING_LIST_PICKLER()
