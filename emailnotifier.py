from notification import Notification

class Email(Notification):
    def send(self, user, msg):
        print(f"EMAIL ALERT!!!! {user}: {msg}")