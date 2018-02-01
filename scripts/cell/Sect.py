# -*- coding: utf-8 -*-
import KBEngine
import space_data
from KBEDebug import *
import datetime
import math
from interfaces.Common.EntityObject import EntityObject




class Sect(KBEngine.Entity, EntityObject):
    def __init__(self):
        DEBUG_MSG("Sect:__init__")
        KBEngine.Entity.__init__(self)
