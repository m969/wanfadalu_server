# -*- coding: utf-8 -*-
import KBEngine
import space_data
import sect_data
from KBEDebug import *
import datetime
import math
from interfaces.Common.EntityObject import EntityObject




class Sect(KBEngine.Base, EntityObject):
    def __init__(self):
        DEBUG_MSG("Sect:__init__")
        KBEngine.Base.__init__(self)
        KBEngine.globalData["sect_%i" % self.sectID] = self
        self.sectData = sect_data.data[self.sectID]
        self.memberList = []


    def requestJoinSect(self, avatarCall):
        DEBUG_MSG("Sect:requestJoinSect")
        self.memberList.append(avatarCall.id)
        avatarCall.onJoinSectResult(self.sectID, 1)
