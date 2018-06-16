# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import GlobalConst
import PyDatas.level_data as level_data
import PyDatas.dialog_config_Table as dialog_config_Table
from DIALOG_ITEM import TDialogItem
from DIALOG_ITEM import TDialogItemList

dialogDatas = dialog_config_Table.datas
dialogTypeMap = {
    1: "Arena",
    2: "Store",
    3: "Sect",
    4: "Task",
}




class DialogSystem:
    def __init__(self):
        # DEBUG_MSG("DialogSystem:__init__")
        pass


    def onTimer(self, timerHandle, userData):
        pass


    def requestBuyGoods(self, exposed, spaceID, npcName, goodsID):
        DEBUG_MSG("DialogSystem:requestBuyGoods")
        if exposed != self.id:
            return


    def giveGoods(self, goodsID):
        DEBUG_MSG("DialogSystem:giveGoods")


    def deleteGoods(self, goodsID):
        """
        删除背包中的物品
        """
        DEBUG_MSG("DialogSystem:deleteGoods")


    def deductMoney(self, num):
        DEBUG_MSG("getMoney")


    def requestDialog(self, exposed, npcEntityID):
        DEBUG_MSG("DialogSystem:requestDialog")
        if exposed != self.id:
            return
        npc = KBEngine.entities.get(npcEntityID)
        if npc is None:
            return
        self.dialogNpc = npc
        dialogItems = TDialogItemList()
        dialogItems["values"] = []
        dialogItems["npcName"] = ""
        dialogItems["npcDialog"] = ""
        if npc.npcType == GlobalConst.NpcType_Arena:
            dialogItems["npcName"] = "守擂人"
            dialogItems["npcDialog"] = "你要上擂台吗？"
            item = TDialogItem()
            item["id"] = 1001
            item["content"] = "我要上擂台"
            dialogItems["values"].append(item)
            # dialogItems[item["id"]] = item
            item = TDialogItem()
            item["id"] = 0
            item["content"] = "算了，怂"
            dialogItems["values"].append(item)
            # dialogItems[item["id"]] = item
            self.client.OnDialogItemsReturn(dialogItems)
        elif npc.npcType == GlobalConst.NpcType_Store:
            dialogItems["npcName"] = "商人"
            dialogItems["npcDialog"] = "你要购买道具吗？"
            item = TDialogItem()
            item["id"] = 1002
            item["content"] = "我要购买道具"
            dialogItems["values"].append(item)
            # dialogItems[item["id"]] = item
            item = TDialogItem()
            item["id"] = 0
            item["content"] = "算了，穷"
            dialogItems["values"].append(item)
            # dialogItems[item["id"]] = item
            self.client.OnDialogItemsReturn(dialogItems)
        elif npc.npcType == GlobalConst.NpcType_Sect:
            dialogItems["npcName"] = "守宗人"
            dialogItems["npcDialog"] = "你要加入云灵宗吗？"
            item = TDialogItem()
            item["id"] = 1002
            item["content"] = "我要加入宗门"
            dialogItems["values"].append(item)
            # dialogItems[item["id"]] = item
            item = TDialogItem()
            item["id"] = 0
            item["content"] = "算了，流浪挺好"
            dialogItems["values"].append(item)
            # dialogItems[item["id"]] = item
            self.client.OnDialogItemsReturn(dialogItems)


    def selectDialogItem(self, exposed, dialogID):
        DEBUG_MSG("DialogSystem:selectDialogItem")
        if exposed != self.id:
            return
        if dialogID == 0:
            return
        dialogData = dialogDatas[dialogID]
        dialogType = dialogData["type"]
        # dialogScript = eval(dialogTypeMap[dialogType])()
        # dialogScript.execute(self)
        npcType = self.dialogNpc.npcType
        if npcType == GlobalConst.NpcType_Arena:
            self.requestEnterArena(self.id, self.dialogNpc.arenaID)
        elif npcType == GlobalConst.NpcType_Store:
            self.requestPullStorePropList(self.id, self.dialogNpc.id)
        elif npcType == GlobalConst.NpcType_Sect:
            self.base.requestJoinSect(self.dialogNpc.sectID)


    def getTaskInfo(self, npcName):
        DEBUG_MSG("DialogSystem:getTaskInfo")


    def setTaskFinish(self, npcName, taskIndex, watcherIndex):
        DEBUG_MSG("DialogSystem:setTaskFinish")


    def isTaskFinish(self, npcName, taskIndex):
        DEBUG_MSG("DialogSystem:isTaskFinish")


    def giveAward(self, npcName, taskIndex):
        DEBUG_MSG("DialogSystem:giveAward")


    def giveTask(self, npcName, taskIndex):
        DEBUG_MSG("DialogSystem:giveTask")
