# -*- coding: utf-8 -*-
import KBEngine
import PyDatas.sect_config_Table as sect_config_Table
from KBEDebug import *
import GlobalConst
import datetime
import math
from interfaces.Common.EntityObject import EntityObject




class Sect(KBEngine.Entity, EntityObject):
	def __init__(self):
		DEBUG_MSG("Sect:__init__")
		KBEngine.Entity.__init__(self)
		KBEngine.globalData["space_base_spaceID_%i" % self.spaceID].cell.onEnter(self)
		params = {}
		params["npcID"] = 0
		params["npcType"] = GlobalConst.NpcType_Sect
		params["sectID"] = self.cell_sectID
		params["arenaID"] = 0
		params["entityName"] = self.entityName
		z = sect_config_Table.datas[self.cell_sectID]["gateDir"][1]
		KBEngine.createEntity("Npc", self.spaceID, sect_config_Table.datas[self.cell_sectID]["gatePos"], (0.0, 0.0, math.radians(z)), params)


	def onEntityEnterSpace(self, spaceID, spaceName):
		DEBUG_MSG("Sect:onEntityEnterSpace %i %s" % (spaceID, spaceName))
