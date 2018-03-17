# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import datetime
import math
import PyDatas.sect_config_Table as sect_config_Table
from ID_DBID_MAP_LIST import TIdDbidMap
from ID_DBID_MAP_LIST import TIdDbidMapList




class SectsManager:
    def __init__(self):
        DEBUG_MSG("SectsManager:__init__")
        KBEngine.globalData["SectsManager"] = self
        self.sectList = {}


    def onAllSpacesGetCell(self):
        DEBUG_MSG("SectsManager:onAllSpacesGetCell")
        for (sectID, sectData) in sect_config_Table.datas.items():
            if sectID in self.sectDBIDList.keys():
                KBEngine.createBaseFromDBID("Sect", self.sectDBIDList[sectID]["dbid"], self.__sectCreateCallback)
            else:
                sect = KBEngine.createBaseLocally("Sect", {"entityName": sectData["sectName"], "sectID": sectID, "position": sectData["pos"]})
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
