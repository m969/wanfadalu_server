# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from rx import Observable, Observer
from rx.subjects import Subject


class EventAggregator:
    eventAggregator = Subject()
    def __init__(self):
        DEBUG_MSG("EventAggregator:__init__")

    def publish(self, event):
        DEBUG_MSG("EventAggregator:publish " + str(event))
        self.eventAggregator.on_next(event)

    def onEvent(self, eventName):
        DEBUG_MSG("EventAggregator:onEvent " + eventName)
        filterEvent = self.eventAggregator.filter(lambda evt: evt['eventName'] == eventName)
        return filterEvent
