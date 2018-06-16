# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import Math
import GlobalConst
import PyDatas.arena_config_Table as arena_config_Table




class SpaceArenaSystem:
	def __init__(self):
		# DEBUG_MSG("SpaceArenaSystem:__init__")
		for arenaID, arenaData in arena_config_Table.datas.items():
			if arenaData["spaceUID"] == self.spaceUID:
				arenaPosition = arenaData["pos"]
				self.createArena(arenaPosition, arenaID)


	def createArena(self, arenaPosition, arenaID):
		DEBUG_MSG("SpaceArenaSystem:createArena")
		params = {}
		params["entityName"] = "ArenaView"
		params["arenaID"] = arenaID
		self.arena = KBEngine.createEntity("Arena", self.spaceID, arenaPosition, (0.0, 0.0, 0.0), params)
		params = {}
		params["npcID"] = 0
		params["npcType"] = GlobalConst.NpcType_Arena
		params["sectID"] = 0
		params["entityName"] = "守擂人"
		params["arenaID"] = arenaID
		npcPosition = (arenaPosition[0] - 14, arenaPosition[1], arenaPosition[2] - 14)
		self.arenaNpc = KBEngine.createEntity("Npc", self.spaceID, npcPosition, (0.0, 0.0, 3.2), params)
		self.arena.arenaNpc = self.arenaNpc


	def createArenaTrigger(self):
		DEBUG_MSG("SpaceArenaSystem:createArenaTrigger")


	def startShield(self):
		DEBUG_MSG("SpaceArenaSystem:startShield")


	def closeShield(self):
		DEBUG_MSG("SpaceArenaSystem:closeShield")
