# -*- coding: utf-8 -*-
import random
import KBEngine
from KBEDebug import *
from DBID_LIST import TDBIDList




class Account(KBEngine.Proxy):
    def __init__(self):
        KBEngine.Proxy.__init__(self)


    def onTimer(self, id, userArg):
        DEBUG_MSG(id, userArg)


    def onEntitiesEnabled(self):
        DEBUG_MSG(self.avatarDBIDList)
        INFO_MSG("account[%i] entities enable. mailbox:%s" % (self.id, self.client))
        if self.avatarDBID == 0:
            self.avatar = KBEngine.createBaseLocally("Avatar", {})
            if self.avatar:
                self.avatar.accountEntity = self
                self.avatar.cellData["position"] = (120.4, 0.44, 90.6)
                self.avatar.cellData["direction"] = (0.0, 0.0, 0.0)
                self.avatar.cellData["entityName"] = self.__ACCOUNT_NAME__
                campNumber = random.randint(0, 1)
                DEBUG_MSG("campNumber " + str(campNumber))
                if campNumber == 0:
                    self.avatar.cellData["campName"] = "蓝营"
                if campNumber == 1:
                    self.avatar.cellData["campName"] = "红营"
                self.avatar.writeToDB(self._onAvatarSaved)
                self.giveClientTo(self.avatar)
        else:
            KBEngine.createBaseFromDBID("Avatar", self.avatarDBID, self.__onAvatarCreateCB)


    def __onAvatarCreateCB(self, baseRef, dbid, wasActive):
        DEBUG_MSG("__onAvatarCreateCB")
        if wasActive:
            ERROR_MSG("Account::__onAvatarCreated:(%i): this character is in world now!" % (self.id))
            return
        if baseRef is None:
            ERROR_MSG("Account::__onAvatarCreated:(%i): the character you wanted to created is not exist!" % (self.id))
            return
        avatar = KBEngine.entities.get(baseRef.id)
        if avatar is None:
            ERROR_MSG("Account::__onAvatarCreated:(%i): when character was created, it died as well!" % (self.id))
            return
        avatar.accountEntity = self
        avatar.cellData["dbid"] = dbid
        avatar.setAvatarName(self.__ACCOUNT_NAME__)
        self.giveClientTo(avatar)


    def _onAvatarSaved(self, success, avatar):
        self.avatarDBID = self.avatar.databaseID
        self.avatar.cellData["dbid"] = self.avatar.databaseID
        self.writeToDB(self._onAccountSaved)


    def _onAccountSaved(self, success, account):
        pass


    def _onAccountSavedThenDestroy(self, success, account):
        self.destroy()


    def onDestroy(self):
        DEBUG_MSG("Account:onDestroy")


    def onLogOnAttempt(self, ip, port, password):
        INFO_MSG(ip, port, password)
        return KBEngine.LOG_ON_ACCEPT


    def onClientDeath(self):
        DEBUG_MSG("Account[%i].onClientDeath:" % self.id)
        self.destroy()


    def destroyAccount(self):
        self.writeToDB(self._onAccountSavedThenDestroy)
