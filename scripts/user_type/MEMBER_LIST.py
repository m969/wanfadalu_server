# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *




class TMemberList(list):
    def __init__(self):
        list.__init__(self)


    def asDict(self):
        # DEBUG_MSG("TMemberList:asDict")
        # DEBUG_MSG(self)
        datas = []
        dic = {"values":datas}
        for value in self:
            datas.append(value)
        return dic


    def createFromDict(self, dictData):
        # DEBUG_MSG("TMemberList:createFromDict")
        # DEBUG_MSG(self)
        # DEBUG_MSG(dictData)
        for data in dictData["values"]:
            self.append(data)
        return self




class MEMBER_LIST_PICKLER:
    def __init__(self):
        pass


    def createObjFromDict(self, dictData):
        return TMemberList().createFromDict(dictData)


    def getDictFromObj(self, obj):
        return obj.asDict()


    def isSameType(self, obj):
        return isinstance(obj, TMemberList)


member_list_inst = MEMBER_LIST_PICKLER()
