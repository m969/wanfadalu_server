# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from strategy.trigger_strategy import *
import PyDatas.monster_config_Table as monster_config_Table
import copy




class SpaceMonsterSystem:
    def __init__(self):
        # DEBUG_MSG("SpaceMonsterSystem:__init__")
        self.tmpCreateEntityDatas = []
        try:
            exec("import PyDatas.space_%i_spawn_Table" % self.spaceUID)
        except ImportError:
            pass
        else:
            self.tmpCreateEntityDatas = eval("copy.deepcopy(list(PyDatas.space_%i_spawn_Table.datas.values()))" % self.spaceUID)
        self.addTimer(0, 1, 0)    # 怪物生成定时器 每2秒生成5个


    def onTimer(self, timerHandle, userData):
        if userData is 0:
            if len(self.tmpCreateEntityDatas) <= 0:
                self.delTimer(timerHandle)
                return
            datas = self.tmpCreateEntityDatas.pop(0)
            if datas is None:
                ERROR_MSG("Space::onTimer: spawn %i is error!" % datas[0])
            params = {
                "typeID": datas["typeID"],
                "entityName": monster_config_Table.datas[datas["typeID"]]["name"],
                "HP_Max": monster_config_Table.datas[datas["typeID"]]["hp"],
                "HP": monster_config_Table.datas[datas["typeID"]]["hp"]
            }
            KBEngine.createEntity(datas["entity_type"], self.spaceID, tuple(datas["spawnPos"]), (0.0, 0.0, 0.0), params)


    def monsterReborn(self, spawnPos, typeID):
        """
        重生怪物
        """
        DEBUG_MSG("SpaceMonsterSystem:monsterReborn")
        datas = {}
        datas["entity_type"] = "Monster"
        datas["typeID"] = typeID
        datas["spawnPos"] = spawnPos
        self.tmpCreateEntityDatas.append(datas)
        self.addTimer(2, 1, 0)
