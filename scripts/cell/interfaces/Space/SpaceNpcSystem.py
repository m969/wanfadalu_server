# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import PyDatas.npc_config_Table as npc_config_Table
import GlobalConst
import math




class SpaceNpcSystem:
    def __init__(self):
        # DEBUG_MSG("SpaceNpcSystem:__init__")
        self.npcDatas = {}
        for npcID, npcData in npc_config_Table.datas.items():
            if npcData["spaceUID"] == self.spaceUID:
                self.npcDatas[npcID] = npcData
                params = {}
                params["npcID"] = npcID
                params["npcType"] = npcData["type"]
                params["store"] = npcData["store"]
                params["entityName"] = npcData["name"]
                KBEngine.createEntity("Npc", self.spaceID, npcData["pos"], (0.0, 0.0, math.radians(npcData["dir"][1])), params)


    def requestNpc(self, npcName):
        DEBUG_MSG("SpaceNpcSystem:requestNpc")
        DEBUG_MSG(self.npcList)
        if npcName in self.npcList:
            return self.npcList[npcName]
        else:
            DEBUG_MSG("No this Npc")
