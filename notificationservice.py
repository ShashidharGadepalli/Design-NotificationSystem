from event import Event
from observer import Observer
from collections import defaultdict
class Notifier:

    def __init__(self):
        self._channel = defaultdict(list)

    def add_subscriber(self,topic,observer:Observer):

        if observer in self._channel[topic]:
            raise ValueError("User already in Channel")
        self._channel[topic].append(observer)

    def remove_subscriber(self,oberver:Observer,topic):
        if topic not in self._channel:
            raise ValueError(" Topic does not exisit in this channel")
        if oberver not in self._channel[topic]:
            raise ValueError(" User does not exisit for this channel")
        self._channel[topic].remove(oberver)

    def publish(self,event:Event):
        for observer in self._channel.get(event.get_eventTopic(),[]):
            observer.update(event)