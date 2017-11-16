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
        
        KBEngine.globalData["taskMonument"] = self
        self.writeToDB(self._onTaskMonumentSaved, True)
        pass

    def _onTaskMonumentSaved(self, success, taskMonument):
        DEBUG_MSG("TaskMonument:_onTaskMonumentSaved")
        DEBUG_MSG(taskMonument.databaseID)

    def addTask(self, taskName, publishAvatarName):
        DEBUG_MSG("TaskMonument:addTask")
        pass

    def removeTask(self, taskName):
        pass
