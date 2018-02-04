# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import space_data




class SpaceNpcSystem:
    def __init__(self):
        DEBUG_MSG("SpaceNpcSystem:__init__")

        self.spaceData = space_data.data[self.cityName]  # 取出自身的场景数据
        # self.npcList = {}
        # self.npcsData = self.spaceData["Npc数据"]      # 取出场景Npc数据
        # for npcName, npcData in self.npcsData.items():
        #     self.npcList[npcName] = KBEngine.createEntity("Npc",
        #                                                   self.spaceID,
        #                                                   npcData["坐标"],
        #                                                   (0.0, 0.0, 0.0),
        #                                                   {
        #                                                       "npcID": npcData["id"],
        #                                                       "entityName": npcName,
        #                                                       'modelName': npcData["模型名称"]
        #                                                   })     # 创建Npc


    def requestNpc(self, npcName):
        DEBUG_MSG("SpaceNpcSystem:requestNpc")
        DEBUG_MSG(self.npcList)
        if npcName in self.npcList:
            return self.npcList[npcName]
        else:
            DEBUG_MSG("No this Npc")
