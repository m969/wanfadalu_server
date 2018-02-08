# -*- coding: utf-8 -*-
import KBEngine
import space_data
from KBEDebug import *
import datetime
import math
from interfaces.Common.EntityObject import EntityObject




class Sect(KBEngine.Entity, EntityObject):
	def __init__(self):
		DEBUG_MSG("Sect:__init__")
		KBEngine.Entity.__init__(self)
		KBEngine.globalData["space_cell_spaceID_%i" % self.spaceID].onEnter(self)


	def onEntityEnterSpace(self, spaceID, spaceName):
		DEBUG_MSG("Sect:onEntityEnterSpace %i %s" % (spaceID, spaceName))
