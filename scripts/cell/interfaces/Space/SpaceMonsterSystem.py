# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from strategy.trigger_strategy import *
import PyDatas.monster_config_Table as monster_config_Table
import copy




class SpaceMonsterSystem:
    def __init__(self):
        DEBUG_MSG("SpaceMonsterSystem:__init__")
        self.tmpCreateEntityDatas = []
        try:
            exec("import PyDatas.space_%i_spawn_Table" % self.spaceUID)
        except ImportError:
            pass
        else:
            self.tmpCreateEntityDatas = eval("copy.deepcopy(list(PyDatas.space_%i_spawn_Table.datas.values()))" % self.spaceUID)
        self.addTimer(0, 1, 0)    # 怪物生成定时器 每2秒生成5个
        # self.monsterSpawnCounter = {}
        # self.monsterSpawnPositionList = self.spaceData["怪物数据"]       # 怪物出生点列表
        # for monsterName, monsterSpawnPositionList in self.monsterSpawnPositionList.items():
        #     self.monsterSpawnCounter[monsterName] = 0


    def onTimer(self, timerHandle, userData):
        if userData is 0:
            if len(self.tmpCreateEntityDatas) <= 0:
                self.delTimer(timerHandle)
                return
            datas = self.tmpCreateEntityDatas.pop(0)
            if datas is None:
                ERROR_MSG("Space::onTimer: spawn %i is error!" % datas[0])
            params = {
                "typeID": datas["typeID"]
            }
            KBEngine.createEntity(datas["entity_type"], self.spaceID, tuple(datas["spawnPos"]), (0.0, 0.0, 0.0), params)
            # finishCounter = 0
            # for (monsterName, spawnPositionList) in self.monsterSpawnPositionList.items():
            #     tempCounter = 0
            #     counter = self.monsterSpawnCounter[monsterName]
            #     for position in spawnPositionList:
            #         if counter >= len(spawnPositionList):
            #             finishCounter += 1
            #             break
            #         else:
            #             params = {
            #                 'entityName': monsterName,
            #                 'modelName': monster_config_Table.datas[monsterName]["模型名称"]
            #             }
            #             monster = KBEngine.createEntity("Monster", self.spaceID, spawnPositionList[counter], (0.0, 0.0, 0.0), params)# 创建Monster
            #             monster.receiveSpawnPos(spawnPositionList[counter])
            #             if tempCounter >= 5:
            #                 break
            #             counter += 1
            #             tempCounter += 1
            #             self.monsterSpawnCounter[monsterName] = counter
            # if finishCounter >= len(self.monsterSpawnPositionList):
            #     self.delTimer(timerHandle)


    def monsterReborn(self, spawnPos, name):
        """
        重生怪物
        """
        DEBUG_MSG("SpaceMonsterSystem:monsterReborn")
        params = {
            'entityName': name,
            'modelName': monster_config_Table.datas[name]["模型名称"]
        }
        monster = KBEngine.createEntity("Monster", self.spaceID, spawnPos, (0.0, 0.0, 0.0), params)
        monster.receiveSpawnPos(spawnPos)
