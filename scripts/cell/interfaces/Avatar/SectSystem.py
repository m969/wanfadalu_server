# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *




class SectSystem:
    def __init__(self):
        DEBUG_MSG("SectSystem:__init__")


    def onJoinSectResult(self, sectID, result):
        DEBUG_MSG("SectSystem:onJoinSectResult")
        self.sectID = sectID
