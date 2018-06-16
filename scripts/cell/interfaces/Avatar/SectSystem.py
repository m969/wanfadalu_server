# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import PyDatas.prop_config_Table as prop_config_Table




class SectSystem:
    def __init__(self):
        # DEBUG_MSG("SectSystem:__init__")
        pass


    def onJoinSectResult(self, sectID, result):
        DEBUG_MSG("SectSystem:onJoinSectResult")
        self.sectID = sectID
        propID = 1005
        propData = prop_config_Table.datas[propID]
        self.addProp(self.newPropByData(propID, propData))
