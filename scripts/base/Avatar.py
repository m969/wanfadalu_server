# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import datetime
from interfaces.Avatar.ForgeSystem import ForgeSystem
from interfaces.Avatar.ChatChannelSystem import ChatChannelSystem
from interfaces.Avatar.DialogSystem import DialogSystem
from interfaces.Avatar.FriendSystem import FriendSystem
from interfaces.Avatar.MotionSystem import MotionSystem
from interfaces.Avatar.TeleportSystem import TeleportSystem
from interfaces.Avatar.TaskSystem import TaskSystem
from interfaces.Avatar.MagicWeaponSystem import MagicWeaponSystem
from interfaces.Avatar.ArenaSystem import ArenaSystem
from interfaces.Avatar.SectSystem import SectSystem
from interfaces.Avatar.PropSystem import PropSystem
from interfaces.Common.EntityObject import EntityObject
from interfaces.Common.HealthSystem import HealthSystem
from interfaces.Common.SkillSystem import SkillSystem
from interfaces.Common.SuperPowerSystem import SuperPowerSystem




class Avatar(KBEngine.Proxy, 
             EntityObject,
             HealthSystem,
             SuperPowerSystem,
             MotionSystem,
             SkillSystem,
             DialogSystem,
             TeleportSystem,
             FriendSystem,
             ChatChannelSystem,
             ForgeSystem,
             TaskSystem,
             MagicWeaponSystem,
             ArenaSystem,
             SectSystem,
             PropSystem):
    def __init__(self):
        DEBUG_MSG("Avatar:__init__")
        KBEngine.Proxy.__init__(self)
        EntityObject.__init__(self)
        HealthSystem.__init__(self)
        SuperPowerSystem.__init__(self)
        MotionSystem.__init__(self)
        SkillSystem.__init__(self)
        DialogSystem.__init__(self)
        TeleportSystem.__init__(self)
        FriendSystem.__init__(self)
        ChatChannelSystem.__init__(self)
        ForgeSystem.__init__(self)
        TaskSystem.__init__(self)
        MagicWeaponSystem.__init__(self)
        ArenaSystem.__init__(self)
        SectSystem.__init__(self)
        PropSystem.__init__(self)


    def onEntitiesEnabled(self):
        DEBUG_MSG("Avatar:onEntitiesEnabled")
        KBEngine.globalData["SpacesManager"].loginToSpace(self.spaceUID, self)
        KBEngine.globalData["SpacesManager"].addNewAvatar(self.id, self)


    def createCell(self, space):
        DEBUG_MSG("Avatar:createCell")
        self.createCellEntity(space)


    def setAvatarName(self, accountName):
        if self.cell:
            self.cell.setAvatarName(accountName)
        else:
            self.cellData["entityName"] = accountName


    def onGetCell(self):
        DEBUG_MSG("Avatar:onGetCell")
        self.cell.setAvatarDBID(self.databaseID)


    def onLoseCell(self):
        DEBUG_MSG("Avatar:onLoseCell")
        self.destroy()


    def onDestroy(self):
        DEBUG_MSG("Avatar:onDestroy")
        KBEngine.globalData["SpacesManager"].delAvatar(self.id)
        if self.accountEntity is not None:
            self.accountEntity.destroyAccount()


    def onClientGetCell(self):
        DEBUG_MSG("Avatar:onClientGetCell")


    def _onAvatarSaved(self, success, avatar):
        self.destroyCellEntity()


    def onClientDeath(self):
        DEBUG_MSG("Avatar:onClientDeath")
        self.writeToDB(self._onAvatarSaved)


    def publishBulletin(self, bulletinContent):
        DEBUG_MSG("Avatar:publishBulletin")
        self.client.OnPublishBulletin(bulletinContent)
