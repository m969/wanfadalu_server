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
        # for (sectID, sectDBID) in self.sectDBIDList.items():
        #     pass
        if not hasattr(self, "sectDBIDList"):
            self.sectDBIDList = {}
        self.sectList = {}
        self.sectCounter = 0
        # for sectID in self.sectDBIDList.keys():
        #     self.sectList[sectID] = True
        for (sectID, sectData) in sect_data.data.items():
            if sectID in self.sectDBIDList.keys():
                KBEngine.createBaseFromDBID("Sect", self.sectDBIDList[sectID], self.__sectCreateCallback)
            else:
                sect = KBEngine.createBaseLocally("Sect", {"sectName": sectData["sectName"], "sectID": sectID})
                sect.writeToDB(self.__onSectSaved)


    def __onSectSaved(self, success, sect):
        DEBUG_MSG("SectsManager:__onSectSaved")
        self.sectDBIDList[sect.sectID] = sect.databaseID


    def __sectCreateCallback(self, baseRef, dbid, wasActive):
        DEBUG_MSG("SectsManager:__sectCreateCallback")
        self.sectCounter = self.sectCounter + 1
        self.sectList[baseRef.sectID] = baseRef
        if self.sectCounter >= len(self.sectDBIDList):
            pass
