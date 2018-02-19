# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.Avatar.CampSystem import CampSystem
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




class AvatarState:
    def __init__(self):
        DEBUG_MSG("AvatarState")




class StandState(AvatarState):
    def __init__(self):
        DEBUG_MSG("StandState")
        AvatarState.__init__(self)




class RunState(AvatarState):
    def __init__(self):
        DEBUG_MSG("RunState")
        AvatarState.__init__(self)




class Avatar(KBEngine.Entity,
             EntityObject,
             HealthSystem,
             SuperPowerSystem,
             MotionSystem,
             SkillSystem,
             DialogSystem,
             TeleportSystem,
             FriendSystem,
             ChatChannelSystem,
             CampSystem,
             TaskSystem,
             MagicWeaponSystem,
             ArenaSystem,
             SectSystem,
             PropSystem):
    def __init__(self):
        DEBUG_MSG("Avatar.cell:__init__")
        KBEngine.Entity.__init__(self)
        EntityObject.__init__(self)
        HealthSystem.__init__(self)
        SuperPowerSystem.__init__(self)
        MotionSystem.__init__(self)
        SkillSystem.__init__(self)
        DialogSystem.__init__(self)
        TeleportSystem.__init__(self)
        FriendSystem.__init__(self)
        ChatChannelSystem.__init__(self)
        CampSystem.__init__(self)
        TaskSystem.__init__(self)
        MagicWeaponSystem.__init__(self)
        ArenaSystem.__init__(self)
        SectSystem.__init__(self)
        PropSystem.__init__(self)


    def onTimer(self, timerHandle, userData):
        SuperPowerSystem.onTimer(self, timerHandle, userData)   # 10
        HealthSystem.onTimer(self, timerHandle, userData)       # 20
        DialogSystem.onTimer(self, timerHandle, userData)       # 30
        TeleportSystem.onTimer(self, timerHandle, userData)     # 40
        SkillSystem.onTimer(self, timerHandle, userData)        # 100


    def setAvatarName(self, entityName):
        self.entityName = entityName


    def setAvatarDBID(self, dbid):
        self.dbid = dbid


    def onTeleportSuccess(self, nearbyEntity):
        TeleportSystem.onTeleportSuccess(self, nearbyEntity)


    def onEnteredCell(self, parameter_list):
        DEBUG_MSG("Avatar:onEnteredCell 1")


    def onEnteredCell(self, a1, a2):
        DEBUG_MSG("Avatar:onEnteredCell 2")


    def onEnteredCell(self, a1, a2, a3):
        DEBUG_MSG("Avatar:onEnteredCell 3")


    def onDestroy(self):
        DEBUG_MSG("Avatar:onCellDestroy")
