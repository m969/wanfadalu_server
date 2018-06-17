# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.Common.EntityObject import EntityObject
from interfaces.Common.HealthSystem import HealthSystem
from interfaces.Common.SuperPowerSystem import SuperPowerSystem
from interfaces.Common.SkillSystem import SkillSystem
from interfaces.Monster.AI import AI




class Monster(KBEngine.Entity, EntityObject, AI, HealthSystem, SuperPowerSystem, SkillSystem):
    def __init__(self):
        DEBUG_MSG("Monster::__init__")
        KBEngine.Entity.__init__(self)
        EntityObject.__init__(self)
        AI.__init__(self)
        HealthSystem.__init__(self)
        SuperPowerSystem.__init__(self)
        SkillSystem.__init__(self)


    def onTimer(self, tid, userArg):
        AI.onTimer(self, tid, userArg)
        HealthSystem.onTimer(self, tid, userArg)
        SuperPowerSystem.onTimer(self, tid, userArg)
        SkillSystem.onTimer(self, tid, userArg)


    def receiveDamage(self, attackerMailbox, damage):
        HealthSystem.receiveDamage(self, attackerMailbox, damage)
        AI.receiveDamage(self, attackerMailbox, damage)


    def receiveSpawnPos(self, spawnPos):
        #DEBUG_MSG("Monster:receiveSpawnPos")
        self.spawnPos = spawnPos


    def onDead(self, murderer):
        #DEBUG_MSG("Monster:onDead")
        HealthSystem.onDead(self, murderer)
        self.destroy()


    def onDestroy(self):
        KBEngine.globalData["space_base_spaceID_%i" % self.spaceID].cell.monsterReborn(self.spawnPos, self.typeID)
