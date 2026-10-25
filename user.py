from notification import Notification
from event import Event
from observer import Observer

class User(Observer):
    def __init__(self,userName:str,userId:int,notifier:Notification):
        self._username = userName
        self._userId = userId
        self._notifier = notifier

    def get_userName(self):
        return self._username

    def get_userId(self):
        return self._userId

    def update(self,event:Event):
        return self._notifier.send(self._username,event.get_eventDesc())