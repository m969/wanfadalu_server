# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *




class TeleportSystem:
    def __init__(self):
        # DEBUG_MSG("TeleportSystem:__init__")
        pass


    def onTeleportSuccess(self, spaceUID):
        DEBUG_MSG("TeleportSystem:onTeleportSuccess")
        self.spaceUID = spaceUID
