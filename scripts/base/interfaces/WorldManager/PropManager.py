# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import datetime
import math
import sect_data
from ID_DBID_MAP_LIST import TIdDbidMap
from ID_DBID_MAP_LIST import TIdDbidMapList




class PropManager:
    """
    道具管理
    """
    def __init__(self):
        DEBUG_MSG("PropManager:__init__")
        KBEngine.globalData["PropManager"] = self


    def __onSectSaved(self, success, sect):
        DEBUG_MSG("PropManager:__onSectSaved")
        idMap = TIdDbidMap()
        idMap["id"] = sect.sectID
        idMap["dbid"] = sect.databaseID
        self.sectDBIDList[sect.sectID] = idMap
        self.writeToDB(self.__onSectsManagerSaved, True)


    def __sectCreateCallback(self, baseRef, dbid, wasActive):
        DEBUG_MSG("PropManager:__sectCreateCallback")
        self.sectList[baseRef.sectID] = baseRef


    def __onSectsManagerSaved(self, success, sectsManager):
        DEBUG_MSG("PropManager:__onSectsManagerSaved")
