# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *




class MotionSystem:
    def __init__(self):
        DEBUG_MSG("MotionSystem:__init__")
        self.controlledByServer = False
        if self.controlledByServer:
            self.controlledBy = None
        else:
            pass
        self.movementId = 0
        self.canMove = True


    def requestMove(self, exposed, point):
        if self.canMove:
            # DEBUG_MSG("MotionSystem:requestMove " + str(point))
            if self.controlledByServer:
                self.controlledBy = None
                self.moveToPointSample(point, 20)
            else:
                pass
            self.allClients.DoMove(point)


    def requestStopMove(self, exposed):
        self.allClients.OnStopMove()


    def stopMove(self):
        # DEBUG_MSG("Avatar:stopMove")
        # self.cancelController(self.movementId)
        self.allClients.OnStopMove()


    def moveToPointSample(self, destination, velocity, distance=0.2):
        """
        移动到某点
        """
        # DEBUG_MSG("MotionSystem:moveToPointSample " + str(self.position))
        self.movementId = self.moveToPoint(destination, velocity, distance, {}, True, True)


    def onMoveOver(self, controllerID, userData):
        # DEBUG_MSG("MotionSystem:onMoveOver " + str(self.position))
        self.stopMove()


    def onMove(self, controllerID, userData):
        pass
