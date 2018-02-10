# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *




class SectSystem:
    def __init__(self):
        DEBUG_MSG("SectSystem:__init__")
        if self.sectID_b != 0:
            if not hasattr(self, "sectData"):
                self.sectData = { "sectID": self.sectID_b }


    def requestJoinSect(self, sectID):
        DEBUG_MSG("SectSystem:requestJoinSect")
        if self.sectID_b != 0:
            return
        KBEngine.globalData["sect_%i" % sectID].requestJoinSect(self, self.databaseID)


    def onJoinSectResult(self, sectID, result):
        DEBUG_MSG("SectSystem:onJoinSectResult")
        self.sectID_b = sectID
        self.client.onJoinSectResult(sectID, result)


    def requestSelfSectData(self):
        DEBUG_MSG("SectSystem:requestSelfSectData")
        if self.sectID_b == 0:
            return
        self.client.onRequestSelfSectDataReturn(self.sectData)
