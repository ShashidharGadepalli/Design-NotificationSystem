from notification import Notification

class SMS(Notification):
    def send(self,user,msg):
        print(f"SMS ALERT!!! {user}:{msg}")