# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *


class TeleportSystem:
    def __init__(self):
        DEBUG_MSG("TeleportSystem:__init__")

    def teleportToSpace(self, baseMailbox):
        DEBUG_MSG("Avatar:teleportToSpace")
        self.teleport(baseMailbox)

    def onTeleportSuccess(self, spaceName):
        DEBUG_MSG("Avatar:onTeleportSuccess")
        self.spaceName = spaceName
