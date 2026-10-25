class Event:

    def __init__(self,topic:str,content:str):
        self._topic = topic
        self._content = content

    def get_eventTopic(self):
        return self._topic
    
    def get_eventDesc(self):
        return self._content