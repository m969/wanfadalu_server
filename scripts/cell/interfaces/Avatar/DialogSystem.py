# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import avatar_skill_data
import npc_data
import prop_data
import level_data
from TASK_INFO import TTaskInfo
from taskScripts.MuJingGuaiRenWu import MuJingGuaiRenWu
from taskScripts.YanShiLingGuaiRenWu import YanShiLingGuaiRenWu
from taskScripts.Duihuarenwu import Duihuarenwu
from taskScripts.Xiaoshiniudao_San import Xiaoshiniudao_San
from taskScripts.Caijizuanshi import Caijizuanshi
from taskScripts.TanxianshandongRenWu import TanxianshandongRenWu
from taskScripts.Bangzhushenmiren import Bangzhushenmiren
from taskScripts.Sidingzhongsheng import Sidingzhongsheng
from taskScripts.Qianlisongqing import Qianlisongqing
from taskScripts.Xunzhaobaoma import Xunzhaobaoma
from taskScripts.Pobudeyi import Pobudeyi




class DialogSystem:
    def __init__(self):
        DEBUG_MSG("DialogSystem:__init__")
        self.canDialog = True
        self.taskScriptList = {}
        self.finishTaskScriptList = []
        """
        在角色初始化时，遍历角色的任务列表，通过任务的所属npc（avatarTaskInfo[0]）以及任务索引（avatarTaskInfo[1]）
        找出任务的所有信息，
        提取任务脚本信息并且创建任务监视脚本。onTimer函数会每秒调用任务监视脚本的检测函数检测任务是否满足完成条件。
        """
        for (key, avatarTaskInfo) in self.taskInfoList.items():
            npcTaskList = npc_data.data[avatarTaskInfo[0]]
            for (taskIndex, taskInfo) in npcTaskList.items():
                if taskIndex == avatarTaskInfo[1]:
                    taskScript = taskInfo["任务脚本"]
                    nextTaskScriptKey = 0
                    for taskScriptKey in self.taskScriptList.keys():
                        if taskScriptKey >= nextTaskScriptKey:
                            nextTaskScriptKey = taskScriptKey
                    nextTaskScriptKey += 1
                    exec("self.taskScriptList[" + str(nextTaskScriptKey) + "] = " + taskScript + "(self, " + str(
                        nextTaskScriptKey) +
                         ", avatarTaskInfo[0], avatarTaskInfo[1])")
        self.addTimer(1, 1, 31)  # 添加 任务监视检测 定时器
        #self.giveTask("TestNpc", 1)


    def onTimer(self, timerHandle, userData):
        if userData == 31:  # 任务监视检测 定时器
            """
            此Timer会每秒调用任务监视脚本的检测函数检测任务是否满足完成条件。
            """
            tempDict = {}
            for k in self.taskScriptList.keys():
                self.taskScriptList[k].detectTaskCompleteness()
            count = 0
            for (key, value) in self.taskScriptList.items():
                for k in self.finishTaskScriptList:
                    if k == key:
                        count = 1
                if count == 0:
                    tempDict[key] = value
            self.taskScriptList = tempDict
            self.finishTaskScriptList.clear()


    def requestBuyGoods(self, exposed, spaceID, npcName, goodsID):
        if exposed != self.id:
            return
        DEBUG_MSG("DialogSystem:requestBuyGoods")
        npcMailbox = KBEngine.globalData["space_cell_%i" % spaceID].requestNpc(npcName)
        result = npcMailbox.requestBuyGoods(self, goodsID)
        self.client.BuyResult(result)


    def giveGoods(self, goodsID):
        DEBUG_MSG("DialogSystem:giveGoods")
        tempBag = self.avatarBag
        DEBUG_MSG(tempBag)
        tempBag[goodsID] = goodsID
        self.avatarBag = tempBag
        DEBUG_MSG(self.avatarBag)
        if prop_data.data[goodsID]['name'] == "木剑":
            if self.hasAttr("Xiaoshiniudao_San_TaskCounter") is True:
                self.setAttr("Xiaoshiniudao_San_TaskCounter",
                             self.Xiaoshiniudao_San_TaskCounter + 1)
            else:
                self.setAttr("Xiaoshiniudao_San_TaskCounter", 1)
        if prop_data.data[goodsID]['name'] == "精致宝箱":
            if self.hasAttr("TanxianshandongRenWu_TaskCounter") is True:
                self.setAttr("TanxianshandongRenWu_TaskCounter",
                             self.TanxianshandongRenWu_TaskCounter+ 1)
            else:
                self.setAttr("TanxianshandongRenWu_TaskCounter", 1)
        if prop_data.data[goodsID]['name'] == "钻石":
            if self.hasAttr("Caijizuanshi_TaskCounter") is True:
                self.setAttr("Caijizuanshi_TaskCounter",
                             self.Caijizuanshi_TaskCounter + 1)
            else:
                self.setAttr("Caijizuanshi_TaskCounter", 1)
        if prop_data.data[goodsID]['name'] == "宝马":
            if self.hasAttr("Xunzhaobaoma_TaskCounter") is True:
                self.setAttr("Xunzhaobaoma_TaskCounter",
                             self.Xunzhaobaoma_TaskCounter + 1)
            else:
                self.setAttr("Xunzhaobaoma_TaskCounter", 1)


    def deleteGoods(self, goodsID):
        """
        删除背包中的物品
        """
        DEBUG_MSG("DialogSystem:deleteGoods")
        tempBag = self.avatarBag
        DEBUG_MSG(tempBag)
        if goodsID in tempBag.keys():
            del tempBag[goodsID]
        self.avatarBag = tempBag
        DEBUG_MSG(self.avatarBag)
        if prop_data.data[goodsID]['name'] == "信":
            if self.hasAttr("Qianlisongqing_TaskCounter") is True:
                self.setAttr("Qianlisongqing_TaskCounter",
                             self.Qianlisongqing_TaskCounter + 1)
            else:
                self.setAttr("Qianlisongqing_TaskCounter", 1)


    def deductMoney(self, num):
        DEBUG_MSG("getMoney")
        self.goldCount -= num


    def requestDialog(self, exposed, npcEntityID):
        DEBUG_MSG("DialogSystem:requestDialog")
        if exposed != self.id:
            return
        npc = KBEngine.entities.get(npcEntityID)
        if npc is None:
            return
        dialogItems = {}
        if npc.npcType == 1:
            dialogItems[0] = {"dialogIndex":0, "dialogID":1001, "content":"我要上擂台"}
            dialogItems[1] = {"dialogIndex":1, "dialogID":0, "content":"算了，怂"}
            self.client.OnDialogItemsReturn(dialogItems)
        elif npc.npcType == 2:
            dialogItems[0] = {"dialogIndex":0, "dialogID":1002, "content":"我要购买道具"}
            dialogItems[1] = {"dialogIndex":1, "dialogID":0, "content":"算了，穷"}
            self.client.OnDialogItemsReturn(dialogItems)
        elif npc.npcType == 3:
            dialogItems[0] = {"dialogIndex":0, "dialogID":1003, "content":"我要加入宗门"}
            dialogItems[1] = {"dialogIndex":1, "dialogID":0, "content":"算了，流浪挺好"}
            self.client.OnDialogItemsReturn(dialogItems)
        # npcMailbox = KBEngine.globalData["space_cell_%i" % self.spaceID].requestNpc(npcName)
        # if npcMailbox:
        #     dialog = npcMailbox.requestTask(self)
        #     self.client.DoDialog(npcMailbox.name, dialog)
        # else:
        #     DEBUG_MSG("npcMailbox is None")


    def selectDialogItem(self, exposed, dialogID):
        DEBUG_MSG("DialogSystem:selectDialogItem")
        if exposed != self.id:
            return
        if dialogID == 0:
            return


    def getTaskInfo(self, npcName):
        DEBUG_MSG("DialogSystem:getTaskInfo")
        specificNpcTaskInfo = []
        for aTaskInfo in self.taskInfoList.values():
            if aTaskInfo[0] == npcName:
                specificNpcTaskInfo.append(aTaskInfo)
        return specificNpcTaskInfo


    def setTaskFinish(self, npcName, taskIndex, watcherIndex):
        """
        任务完成度监视脚本会监测任务是否已完成，如果任务完成了就会调用这个函数，设置角色任务信息为已完成状态，
        并且删除任务完成度监视脚本。
        """
        DEBUG_MSG("DialogSystem:setTaskFinish")
        for (key, taskInfo) in self.taskInfoList.items():
            if npcName == taskInfo[0] and taskIndex == taskInfo[1]:
                DEBUG_MSG("setTaskFinish")
                taskInfo[2] = True
                self.taskInfoList[key] = taskInfo
                self.finishTaskScriptList.append(watcherIndex)


    def isTaskFinish(self, npcName, taskIndex):
        DEBUG_MSG("DialogSystem:isTaskFinish")
        for taskInfo in self.taskInfoList.values():
            if npcName == taskInfo[0] and taskIndex == taskInfo[1]:
                DEBUG_MSG("return isTaskFinish")
                return taskInfo[2]
        return False


    def giveAward(self, npcName, taskIndex):
        """
        任务完成给予奖励，由npc调用，成功给予奖励后设置角色任务信息为已提交。
        """
        DEBUG_MSG("DialogSystem:giveAward")
        self.goldCount += npc_data.data[npcName][taskIndex]["金币奖励"]
        for (propName, propCount) in npc_data.data[npcName][taskIndex]["道具奖励"].items():
            # goodsInfo = {0:propName, 1:propCount}
            i = 0
            for (k, va) in prop_data.data.items():
                if propName == va["name"]:
                    i = 1
                    DEBUG_MSG("give prop id = " + str(k))
                    self.giveGoods(k)
            if i == 0:
                DEBUG_MSG("has no this prop!")
        for (propName, propCount) in npc_data.data[npcName][taskIndex]["道具丢弃"].items():
            i = 0
            for (k, va) in prop_data.data.items():
                if propName == va["name"]:
                    i = 1
                    DEBUG_MSG("delete prop id = " + str(k))
                    self.deleteGoods(k)
            if i == 0:
                DEBUG_MSG("has no this prop!")
        for (key, value) in self.taskInfoList.items():
            if value[0] == npcName and value[1] == taskIndex:
                self.taskInfoList[key][3] = True
                return


    def giveTask(self, npcName, taskIndex):
        """
        赋予任务，由npc调用。
        """
        DEBUG_MSG("DialogSystem:giveTask")
        taskInfo = TTaskInfo()
        taskInfo.extend([npcName, taskIndex, False, False])
        self.taskInfoList[npcName + str(taskIndex)] = taskInfo
        taskScript = npc_data.data[npcName][taskIndex]["任务脚本"]
        indexOnAvatarTaskScriptList = 0
        for keyIndex in self.taskScriptList.keys():
            DEBUG_MSG("taskScriptList.keys() = ")
            DEBUG_MSG(self.taskScriptList.keys())
            if keyIndex >= indexOnAvatarTaskScriptList:
                indexOnAvatarTaskScriptList = keyIndex
        indexOnAvatarTaskScriptList += 1
        exec("self.taskScriptList[" + str(indexOnAvatarTaskScriptList) + "] = " + taskScript + "(self, " + str(
            indexOnAvatarTaskScriptList) +
             ", npcName, taskIndex)")
