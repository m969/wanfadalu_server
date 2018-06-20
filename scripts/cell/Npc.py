# -*- coding: utf-8 -*-
import KBEngine
import PyDatas.prop_config_Table as prop_config_Table
from KBEDebug import *
from interfaces.Common.EntityObject import EntityObject
from interfaces.Npc.NpcDialogSystem import NpcDialogSystem
from interfaces.Npc.NpcStoreSystem import NpcStoreSystem
from interfaces.Npc.NpcTaskSystem import NpcTaskSystem




class Npc(KBEngine.Entity, EntityObject, NpcDialogSystem, NpcStoreSystem, NpcTaskSystem):
    def __init__(self):
        # DEBUG_MSG("Npc:__init__")
        KBEngine.Entity.__init__(self)
        EntityObject.__init__(self)
        if self.npcType == 1:
            NpcStoreSystem.__init__(self)
        responseItems = {}


    def requestBuyGoods(self, requester, goodsID):
        DEBUG_MSG("Npc:requestBuyGoods")


    def requestDialog(self, requester, flag=0):
        DEBUG_MSG("Npc:requestDialog")


    def requestTask(self, requester):
        """
        请求任务接口。由玩家发起调用，此函数会视情况决策，当玩家没有任务时会赋予玩家任务，当玩家任务已完成会给予奖励，并返回玩家此npc对应的对话信息。
        """
        DEBUG_MSG("Npc:requestDialog")


    def giveTask(self, requester, taskID):
        """
        赋予请求者任务。
        """
        DEBUG_MSG("Npc:giveTask")
        # requester.giveTask(self.entityName, taskID)
