from notification import Notification
from notificationservice import Notifier
from emailnotifier import Email
from sms import SMS
from event import Event
from user import User

service = Notifier()

user1 = User("Shashi",4514,Email())
user2 = User("Andrew",1234,SMS())
user3 = User("Kim K",1567,Email())
user4 = User("Messi",9876,SMS())
user5 = User("Eashan",1246,SMS())


topic1 = "Chris Brown"
topic2 = "Spiderman"
topic3 = "Beauty"
topic4 = "Footbal"

event1 = Event(topic1, " Brown Album hits!!!")
event2 = Event(topic2, "Brand new day")
event3 = Event(topic3, "Beauty skincare and lifestyle")
event4 = Event(topic4, "Worldcup and More")

service.add_subscriber(topic1,user1)

service.add_subscriber(topic2,user2)
service.add_subscriber(topic2,user5)

service.add_subscriber(topic3,user3)

service.add_subscriber(topic4,user1)
service.add_subscriber(topic4,user5)
service.add_subscriber(topic4,user4)

service.publish(Event(topic1," NO signal just came out"))

service.publish(Event(topic2,"Releasing Tomroow"))

service.publish(Event(topic3,"Flat 50 off at sephota"))

service.publish(Event(topic4,"WorldCup Final tomorrow"))

service.remove_subscriber(user5,topic4)
service.add_subscriber(user5,topic2)


service.publish(Event(topic4,"WorldCup Final Today"))
service.publish(Event(topic2,"Dont forget to use coupon kim KKK"))