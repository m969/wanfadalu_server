# -*- coding: utf-8 -*-
import math
import random
import KBEngine
from KBEDebug import *
from strategy.trigger_strategy import *
import PyDatas.monster_config_Table as monster_config_Table
import Math




class AI:
    def __init__(self):
        self.spawnPos = self.position
        # 移动速度
        self.speed = monster_config_Table.datas[self.typeID]["speed"]
        # 怪物的攻击距离
        self.monsterAttackDistance = monster_config_Table.datas[self.typeID]["attack_distance"]
        # 怪物的活动范围
        self.territoryArea = monster_config_Table.datas[self.typeID]["patrol_radius"]
        #技能移动速度
        self.skillSpeed = monster_config_Table.datas[self.typeID]["skill_speed"]
        # 怪物攻击的敌人ID
        self.targetID = 0
        # 怪物移向敌人的移动id
        self.addTimer(1, 1, 0)


    def initEntity(self):
        pass


    def checkInTerritory(self):
        """
        检查自己是否在可活动领地中
        """
        ret = True
        if self.position.distTo(self.spawnPos) >= self.territoryArea:
            ret = False
        return ret


    def randomMovePos(self):
        """
        怪物的随机运动的坐标
        """
        while True:
            rnd = random.random()
            a = int(self.territoryArea * rnd)  # 移动半径距离在30米内
            b = int(360.0 * rnd)  # 随机一个角度
            x = int(a * math.cos(b))  # 半径 * 正余玄
            z = int(a * math.sin(b))
            movePos = (self.position.x + x, self.position.y, self.position.z + z)
            self.moveToPoint(movePos, self.speed, 0, self, True, False)
            break
        return True


    def addTerritory(self):
        """
        添加领地
        进入领地范围的某些entity将视为敌人
        """
        self.addProximity(self.territoryArea, self.territoryArea, 0)


    def setTarget(self, entityID):
        """
        设置攻击目标
        """
        self.targetID = entityID


    def onEnterTrap(self, entityEntering, range_xz, range_y, controllerID, userarg):
        """
        有entity进入trap
        """
        if entityEntering.getScriptName() != "Avatar":
            return
        self.onAddEnemy(entityEntering.id)


    def onLeaveTrap(self, entityLeaving, range_xz, range_y, controllerID, userarg):
        """
        有entity离开trap
        """
        if entityLeaving.getScriptName() != "Avatar":
            return
        self.onRemoveEnemy(entityLeaving.id)


    def onAddEnemy(self, entityID):
        """
        有敌人进入列表并将设置为敌人
        """
        if self.targetID == 0:
            self.setTarget(entityID)


    def onRemoveEnemy(self, entityID):
        """
        删除敌人
        """
        if self.targetID == entityID:
            self.onLoseTarget()


    def onLoseTarget(self):
        """
        敌人丢失
        """
        self.targetID = 0


    def onMoveOver(self, controllerID, userData):
        """
        当怪物停止移动时调用闲置时的动画
        """
        self.allClients.StopMove()


    def onTimer(self, tid, userArg):
        """
        引擎回调timer触发
        """
        if userArg == 0:
            if self.targetID == 0:
                self.HP = self.HP_Max
                if self.checkInTerritory():
                    self.randomMovePos()
                else:
                    self.moveToPoint(self.spawnPos, self.speed, 0, self, True, False)
                self.allClients.StartMove()
            if self.targetID != 0 and self.HP < self.HP_Max:
                self.moveToEntity(self.targetID, self.speed, self.monsterAttackDistance, self, True, False)
                self.allClients.StartMove()
