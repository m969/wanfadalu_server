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
        # propData = prop_config_Table.datas[goodsID]
        # goodsName = propData['name']
        # if goodsName in self.storeData:
        #     if requester.goldCount >= propData['price']:
        #         requester.giveGoods(goodsID)
        #         requester.deductMoney(propData['price'])
        #         return True
        #     else:
        #         return False
        # else:
        #     return False


    def requestDialog(self, requester, flag=0):
        DEBUG_MSG("Npc:requestDialog")


    def requestTask(self, requester):
        """
        请求任务接口。由玩家发起调用，此函数会视情况决策，当玩家没有任务时会赋予玩家任务，当玩家任务已完成会给予奖励，并返回玩家此npc对应的对话信息。
        """
        DEBUG_MSG("Npc:requestDialog")
        # requesterTaskInfoList = []
        # requesterTaskInfoList = requester.getTaskInfo(self.entityName)
        # taskCommitCount = 0 # 任务完成数
        # if requesterTaskInfoList.__len__() == 0:
        #     DEBUG_MSG("avatar has no my task!")
        #     DEBUG_MSG("give task " + str(1))
        #     self.giveTask(requester, 1)
        #     return self.myTaskDict[1].get("任务描述")
        # else:
        #     for requesterTaskInfo in requesterTaskInfoList:
        #         taskNpcName = requesterTaskInfo[0] # npc名称
        #         taskIndex = requesterTaskInfo[1] # 任务索引
        #         isTaskFinish = requesterTaskInfo[2] # 任务是否已完成
        #         isTaskCommit = requesterTaskInfo[3] # 任务是否已提交
        #         if isTaskFinish == False and isTaskCommit == False:
        #             return self.myTaskDict[taskIndex].get("任务描述")
        #             pass
        #         if isTaskFinish == True and isTaskCommit == False:
        #             requester.giveAward(taskNpcName, taskIndex)
        #             return self.myTaskDict[taskIndex].get("任务完成描述")
        #             pass
        #         if isTaskFinish == True and isTaskCommit == True:
        #             taskCommitCount += 1
        #             if taskCommitCount >= self.myTaskDict.__len__():
        #                 return self.myTaskDict[1]['对话列表'][0]
        # DEBUG_MSG("avatar has some finish task!")
        # requesterNextTaskIndex = 0  # 请求者的下一个任务的索引
        # for aTaskInfoFromRequester in requesterTaskInfoList:
        #     aTaskIndexFromRequester = aTaskInfoFromRequester[1]
        #     DEBUG_MSG("task " + str(aTaskIndexFromRequester) + " has finish!")
        #     if aTaskIndexFromRequester >= requesterNextTaskIndex:
        #         requesterNextTaskIndex = aTaskIndexFromRequester + 1  # 如果有完成的任务，就将已完成的任务的索引加一，作为下一个任务的索引
        # if requesterNextTaskIndex == 0:
        #     ERROR_MSG("avatar has some finish task, but requesterNextTaskIndex == 0")
        # else:
        #     DEBUG_MSG("requesterNextTaskIndex is " + str(requesterNextTaskIndex))
        #     DEBUG_MSG("give task " + str(requesterNextTaskIndex))
        #     self.giveTask(requester, requesterNextTaskIndex)
        #     return self.myTaskDict[requesterNextTaskIndex].get("任务描述")


    def giveTask(self, requester, taskID):
        """
        赋予请求者任务。
        """
        DEBUG_MSG("Npc:giveTask")
        # requester.giveTask(self.entityName, taskID)
