# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *




class TDialogItem(dict):
    def __init__(self):
        dict.__init__(self)

    def asDict(self):
        fixedDict = {}
        fixedDict["id"] = self["id"]
        fixedDict["content"] = self["content"]
        return fixedDict

    def createFromDict(self, dictData):
        self["id"] = dictData["id"]
        self["content"] = dictData["content"]
        return self

class PICKLER1:
    def __init__(self):
        pass

    def createObjFromDict(self, dic):
        return TDialogItem().createFromDict(dic)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, TDialogItem)

dialog_item_inst = PICKLER1()




class TDialogItemList(dict):
    def __init__(self):
        dict.__init__(self)

    def asDict(self):
        # itemList = []
        # for key, item in self.items():
        #     itemList.append(item)
        # fixedDict = {}
        # fixedDict["values"] = itemList
        fixedDict = {}
        fixedDict["values"] = self["values"]
        fixedDict["npcName"] = self["npcName"]
        fixedDict["npcDialog"] = self["npcDialog"]
        return fixedDict

    def createFromDict(self, dictData):
        # itemList = dictData["values"]
        # for item in itemList:
        #     self[item["id"]] = item
        self["values"] = dictData["values"]
        self["npcName"] = dictData["npcName"]
        self["npcDialog"] = dictData["npcDialog"]
        return self

class PICKLER2:
    def __init__(self):
        pass

    def createObjFromDict(self, dic):
        return TDialogItemList().createFromDict(dic)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, TDialogItemList)

dialog_item_list_inst = PICKLER2()
