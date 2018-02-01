# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *




class SectSystem:
    def __init__(self):
        DEBUG_MSG("SectSystem:__init__")


    def requestJoinSect(self, sectID):
        DEBUG_MSG("SectSystem:requestJoinSect")
        if self.sectID != 0:
            return
        KBEngine.globalData["sect_%i" % sectID].requestJoinSect(self)


    def onJoinSectResult(self, sectID, result):
        DEBUG_MSG("SectSystem:onJoinSectResult")
        self.sectID = sectID
