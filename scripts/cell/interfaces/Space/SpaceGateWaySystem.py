# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import PyDatas.trigger_config_Table as trigger_config_Table
from strategy.trigger_strategy import *




class SpaceGateWaySystem:
    def __init__(self):
        # DEBUG_MSG("SpaceGateWaySystem:__init__")
        for triggerID, triggerData in trigger_config_Table.datas.items():
            if triggerData["spaceUID"] == self.spaceUID:
                # exec("self.triggerStrategy = " + triggerData["type"] + "Strategy()")
                # self.triggerStrategy.initializeStrategy(triggerData)
                strategyName = triggerData["type"] + "Strategy"
                strategy = eval(strategyName + "()")
                strategy.initializeStrategy(triggerData)
                params = {}
                params['entityName'] = "GateWayTrigger"
                params['owner'] = self
                params['lifeSpans'] = 0.0
                params['triggerSize'] = 4.0
                params['triggerStrategy'] = {strategyName: strategy}
                trigger = KBEngine.createEntity("Trigger", self.spaceID, triggerData["pos"], (0.0, 0.0, 0.0), params)
