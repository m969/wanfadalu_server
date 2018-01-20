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
        """
        转换为固定字典格式存到数据库
        :return:
        """
        rankingList = []
        for avatarDBID, avatarMatchInfo in self.items():
            rankingList.append(avatarMatchInfo)
        fixedDict = {}
        fixedDict["values"] = rankingList
        return fixedDict

    def createFromDict(self, dictData):
        """
        从数据库取出固定字典并转换为脚本内存格式
        :param dictData:
        :return:
        """
        rankingList = dictData["values"]
        for avatarMatchInfo in rankingList:
            self[avatarMatchInfo["avatarDBID"]] = avatarMatchInfo
        return self

class RANKING_LIST_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dic):
        """
        // 此接口被C++底层调用
        // 引擎将数据交给脚本层管理，脚本层可以将这个字典重定义为任意类型
        // dct中的数据为 {"k1" : 0, "k2" : 0}, 它就是一个字典，包含了2个固定的key
        // 且值一定是符合alias.xml中定义的类型
        // XXX_TYPE().createFromDict接口调用后，返回的是一个list([0, 0])
        // createObjFromDict被调用后，返回的数据将直接赋值到脚本中的变量
        """
        return TRankingList().createFromDict(dic)

    def getDictFromObj(self, obj):
        """
        // 此接口被C++底层调用
        // 底层需要从脚本层中获取数据，脚本层此时应该将数据结构还原为固定字典
        // list([0, 0]) => {"k1" : 0, "k2" : 0}
        """
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, TRankingList)

ranking_list_inst = RANKING_LIST_PICKLER()
