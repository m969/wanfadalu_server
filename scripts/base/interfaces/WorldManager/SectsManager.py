# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import datetime
import math




class SectsManager:
    def __init__(self):
        DEBUG_MSG("SectsManager:__init__")
        KBEngine.globalData["SectsManager"] = self
        KBEngine.createBaseLocally("Sect", {"sectName": "云灵宗", "sectID": 1})
