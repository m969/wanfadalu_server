# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import datetime
import math
import sect_data
from ID_DBID_MAP_LIST import TIdDbidMap
from ID_DBID_MAP_LIST import TIdDbidMapList




class SectsManager:
    def __init__(self):
        DEBUG_MSG("SectsManager:__init__")
        KBEngine.globalData["SectsManager"] = self
        if not hasattr(self, "sectDBIDList"):
            self.sectDBIDList = TIdDbidMapList()
        self.sectList = {}


    def onAllSpacesGetCell(self):
        DEBUG_MSG("SectsManager:onAllSpacesGetCell")
        for (sectID, sectData) in sect_data.data.items():
            if sectID in self.sectDBIDList.keys():
                KBEngine.createBaseFromDBID("Sect", self.sectDBIDList[sectID]["dbid"], self.__sectCreateCallback)
            else:
                sect = KBEngine.createBaseLocally("Sect", {"sectName": sectData["sectName"], "sectID": sectID, "position": sectData["position"]})
                sect.writeToDB(self.__onSectSaved)
                self.sectList[sect.sectID] = sect


    def __onSectSaved(self, success, sect):
        DEBUG_MSG("SectsManager:__onSectSaved")
        idMap = TIdDbidMap()
        idMap["id"] = sect.sectID
        idMap["dbid"] = sect.databaseID
        self.sectDBIDList[sect.sectID] = idMap
        self.writeToDB(self.__onSectsManagerSaved, True)


    def __sectCreateCallback(self, baseRef, dbid, wasActive):
        DEBUG_MSG("SectsManager:__sectCreateCallback")
        self.sectList[baseRef.sectID] = baseRef


    def __onSectsManagerSaved(self, success, sectsManager):
        DEBUG_MSG("SectsManager:__onSectsManagerSaved")
