# -*- coding: utf-8 -*-
import KBEngine
import PyDatas.sect_config_Table as sect_config_Table
from KBEDebug import *
import datetime
import math
from interfaces.Common.EntityObject import EntityObject
from DBID_LIST import TDBIDList




class Sect(KBEngine.Base, EntityObject):
    def __init__(self):
        DEBUG_MSG("Sect:__init__")
        KBEngine.Base.__init__(self)
        KBEngine.globalData["sect_%i" % self.sectID] = self
        self.cellData["cell_sectID"] = self.sectID
        self.sectData = sect_config_Table.datas[self.sectID]
        KBEngine.globalData["space_base_spaceUID_%i" % self.sectData["spaceUID"]].loginSpace(self)


    def createCell(self, space):
        DEBUG_MSG("Sect:createCell")
        self.createCellEntity(space)


    def onGetCell(self):
        DEBUG_MSG("Sect:onGetCell")


    def onLoseCell(self):
        DEBUG_MSG("Sect:onLoseCell")
        self.destroy()


    def requestJoinSect(self, avatarCall, avatarDBID):
        DEBUG_MSG("Sect:requestJoinSect")
        if avatarDBID in self.memberDBIDList:
            return
        self.memberDBIDList.append(avatarCall.id)
        avatarCall.onJoinSectResult(self.sectID, 1)
        self.writeToDB()
