# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from rx import Observable, Observer
from rx.subjects import Subject


class EventAggregator:
    eventAggregator = Subject()
    def __init__(self):
        DEBUG_MSG("EventAggregator:__init__")
        pass

    def publish(self, event):
        DEBUG_MSG("EventAggregator:publish " + str(event))
        self.eventAggregator.on_next(event)
        pass

    def onEvent(self, eventName, onNext, onCompeleted = lambda evt: DEBUG_MSG("onCompeleted"), onError =lambda evt: DEBUG_MSG("onError")):
        DEBUG_MSG("EventAggregator:onEvent " + eventName)
        self.eventAggregator.filter(lambda evt: evt['eventName'] == eventName).subscribe(on_next=onNext, on_completed=onCompeleted, on_error=onError)
        pass
