# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from PROP_LIST import TProp
from PROP_LIST import TPropList
import json




class PropSystem:
    def __init__(self):
        DEBUG_MSG("PropSystem:__init__")
    #     if not hasattr(self, "propList"):
    #         self.propList = TPropList()


    # def addProp(self, propTypeID, propData):
    #     DEBUG_MSG("PropSystem:addProp")
    #     prop = TProp()
    #     prop["propTypeID"] = propTypeID
    #     prop["propData"] = propData
    #     self.propList.append(prop)


    # def removeProp(self, propIndex):
    #     DEBUG_MSG("PropSystem:removeProp")
    #     del self.propList[propIndex]
