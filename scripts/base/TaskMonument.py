# -*- coding: utf-8 -*-
import KBEngine
import space_data
from KBEDebug import *
import datetime
import math
from interfaces.Common.EntityObject import EntityObject




class TaskMonument(KBEngine.Base, EntityObject):
    def __init__(self):
        DEBUG_MSG("TaskMonument:__init__")
        KBEngine.Base.__init__(self)
        KBEngine.globalData["TaskMonument"] = self
        self.writeToDB(self._onTaskMonumentSaved, True)


    def _onTaskMonumentSaved(self, success, taskMonument):
        DEBUG_MSG("TaskMonument:_onTaskMonumentSaved")


    def addTask(self, taskName, publishAvatarName):
        DEBUG_MSG("TaskMonument:addTask")


    def removeTask(self, taskName):
        DEBUG_MSG("TaskMonument:removeTask")
