# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.Common.EntityObject import EntityObject
import Math




class Trigger(KBEngine.Entity, EntityObject):
    def __init__(self):
        #DEBUG_MSG("Trigger:__init__")
        KBEngine.Entity.__init__(self)
        EntityObject.__init__(self)
        self.isTrigger = True
        self.entityList = []
        self.inEntityList = []
        self.delEntityList = []
        if self.lifeSpans > 0.0:
            self.addTimer(self.lifeSpans, 0, 0)
        if self.circleTrigger:
            self.addTimer(0, 0.01, 1)
        if self.rectangleTrigger:
            if abs(self.triggerDirection.z) < 0.001:
                self.triggerDirection2 = Math.Vector3(0, 0, 1)
            if abs(self.triggerDirection.x) < 0.001:
                self.triggerDirection2 = Math.Vector3(1, 0, 0)
            if (abs(self.triggerDirection.x) > 0.001) and (abs(self.triggerDirection.z) > 0.001):
                z = self.triggerDirection.x / (0 - self.triggerDirection.z)
                self.triggerDirection2 = Math.Vector3(1, 0, z)
            self.triggerDirection2.normalise()
            self.addTimer(0, 0.01, 2)
        self.proximityID = 0


    def destroySelf(self):
        if not self.isDestroyed:
            self.destroy()


    def onTimer(self, tid, userArg):
        if userArg == 0:
            self.destroySelf()
        elif userArg == 1:
            for entityId in self.entityList:
                entity = KBEngine.entities.get(entityId, None)
                if entity is None:
                    self.delEntityList.append(entityId)
                    return
                dist = self.position.distTo(entity.position)
                if dist <= self.triggerSize and (entityId not in self.inEntityList):
                    self.inEntityList.append(entityId)
                    self.executeStrategy(entity)
                elif dist > self.triggerSize and (entityId in self.inEntityList):
                    del self.inEntityList[entityId]
        elif userArg == 2:
            for entityId in self.entityList:
                otherEntity = KBEngine.entities.get(entityId, None)
                if otherEntity is None:
                    self.delEntityList.append(entityId)
                    return
                direct = otherEntity.position - self.position
                S = abs(self.triggerDirection.cross2D(direct))
                S2 = abs(self.triggerDirection2.cross2D(direct))
                if S <= self.triggerWidth and S2 <= self.triggerLength and (entityId not in self.inEntityList):
                    self.inEntityList.append(entityId)
                    self.executeStrategy(otherEntity)
                elif (S > self.triggerWidth or S2 > self.triggerLength) and (entityId in self.inEntityList):
                    del self.inEntityList[entityId]
        elif userArg == 3:
            self.proximityID = self.addProximity(self.triggerSize, self.triggerSize, 0)
        for entityId in self.delEntityList:
            if entityId in self.entityList:
                self.entityList.remove(entityId)
            if entityId in self.inEntityList:
                self.inEntityList.remove(entityId)
        self.delEntityList = []


    def executeStrategy(self, entity):
        if self.triggerStrategy is None:
            return
        for strategy in self.triggerStrategy.values():
            strategy.setInfo(self, entity, self.triggerSize, self.triggerSize, self.triggerControllerID, None)
            strategy.execute(self, entity)


    def onEnterTrap(self, other, rangeXZ, rangeY, controllerID, userArg):
        """
        当进入触发器时
        """
        #DEBUG_MSG("Trigger:onEnterTrap")
        if self.proximityID == 0:
            return
        self.triggerControllerID = controllerID
        if self.circleTrigger or self.rectangleTrigger:
            if other.id == self.owner.id:
                return
            if other.id in self.entityList:
                return
            self.entityList.append(other.id)
        else:
            self.executeStrategy(other)


    def onLeaveTrap(self, other, rangeXZ, rangeY, controllerID, userArg):
        """
        当离开触发器时
        """
        if self.circleTrigger or self.rectangleTrigger:
            if other.id in self.entityList:
                self.delEntityList.append(other.id)


    def onWitnessed(self, isWitnessed):
        """
        当被看到时
        """
        #DEBUG_MSG("Trigger:onWitnessed")
        # self.addTimer(0.1, 0, 3)
        self.proximityID = self.addProximity(self.triggerSize, self.triggerSize, 0)
        pass


    def moveToPointSample(self, destination, velocity, distance=0.2):
        """
        移动到某点
        """
        self.moveToPoint(destination, velocity, distance, {}, True, True)


    def moveToEntitySample(self, destEntityID, velocity, distance=0.1):
        """
        移动到某点
        """
        self.moveToEntity(destEntityID, velocity, distance, {}, True, True)
