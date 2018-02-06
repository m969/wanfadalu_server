# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import datetime
import math
import sect_data




class SectsManager:
    def __init__(self):
        DEBUG_MSG("SectsManager:__init__")
        KBEngine.globalData["SectsManager"] = self
        if not hasattr(self, "sectDBIDList"):
            self.sectDBIDList = {}
        self.sectList = {}
        for (sectID, sectData) in sect_data.data.items():
            if sectID in self.sectDBIDList.keys():
                KBEngine.createBaseFromDBID("Sect", self.sectDBIDList[sectID], self.__sectCreateCallback)
            else:
                sect = KBEngine.createBaseLocally("Sect", {"sectName": sectData["sectName"], "sectID": sectID})
                sect.writeToDB(self.__onSectSaved, True)


    def __onSectSaved(self, success, sect):
        DEBUG_MSG("SectsManager:__onSectSaved")
        self.sectDBIDList[sect.sectID] = sect.databaseID
        self.writeToDB(self.__onSectsManagerSaved, True)


    def __sectCreateCallback(self, baseRef, dbid, wasActive):
        DEBUG_MSG("SectsManager:__sectCreateCallback")
        self.sectList[baseRef.sectID] = baseRef


    def __onSectsManagerSaved(self, success, sectsManager):
        DEBUG_MSG("SectsManager:__onSectsManagerSaved")
