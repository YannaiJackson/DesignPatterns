from abc import ABC, abstractmethod


# Subscriber Interface
class ObserverInterface(ABC):
    @abstractmethod
    def update(self, news_site_name):
        pass


# Concrete Publisher
class NewsSite:
    def __init__(self, name: str):
        self.subscribers = []
        self.name = name

    def notify(self):
        for subscriber in self.subscribers:
            subscriber.update(news_site_name=self.name)

    def add_subscriber(self, subscriber: ObserverInterface):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber: ObserverInterface):
        self.subscribers.remove(subscriber)


# Concrete Subscribers
class SMSSubscriber(ObserverInterface):
    def __init__(self, phone_number: int):
        self.phone_number = phone_number

    def update(self, news_site_name: str):
        print(f"{self.phone_number} Received SMS: New article available on {news_site_name}")


class EmailSubscriber(ObserverInterface):
    def __init__(self, email_address: str):
        self.email_address = email_address

    def update(self, news_site_name: str):
        print(f"{self.email_address} Received Email: New article available on {news_site_name}")


# Usage
if __name__ == "__main__":
    news_publisher = NewsSite(name="Times Of Israel")
    sms_sub = SMSSubscriber(phone_number=972554267937)
    email_sub = EmailSubscriber(email_address="examplemail@gmail.com")
    news_publisher.add_subscriber(subscriber=sms_sub)
    news_publisher.add_subscriber(subscriber=email_sub)
    news_publisher.notify()
    news_publisher.remove_subscriber(subscriber=sms_sub)
    news_publisher.notify()
