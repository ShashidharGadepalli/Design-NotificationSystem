# Notification System

A small Python notification system built around the Observer pattern. Users
subscribe to topics, and the notification service delivers published events
through each user's selected notification channel.

## Features

- Topic-based subscriptions
- Add and remove subscribers
- Email and SMS notification implementations
- Abstract interfaces for adding more notification channels
- Multiple subscribers per topic

## Project structure

| File | Purpose |
| --- | --- |
| `event.py` | Defines notification topics and event content |
| `observer.py` | Defines the observer interface |
| `notification.py` | Defines the notification channel interface |
| `user.py` | Implements a subscriber/observer |
| `notificationservice.py` | Manages subscriptions and publishes events |
| `emailnotifier.py` | Sends notifications through email output |
| `sms.py` | Sends notifications through SMS output |
| `main.py` | Example application demonstrating the system |

## Requirements

- Python 3.9 or newer

No third-party packages are required.

## Run the example

From the project directory:

```bash
python3 main.py
```

The example prints email and SMS alerts for the topics to which each user is
subscribed.

## Basic usage

```python
from event import Event
from emailnotifier import Email
from notificationservice import Notifier
from user import User

service = Notifier()
subscriber = User("Alex", 1001, Email())

service.add_subscriber("product-news", subscriber)
service.publish(Event("product-news", "A new product is available."))
```

To add another notification channel, implement the `Notification.send`
method and pass an instance of that channel to `User`.
