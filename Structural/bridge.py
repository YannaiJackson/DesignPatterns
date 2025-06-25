from abc import ABC, abstractmethod


# Implementation - how it's done (low level)
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass


class CreditCard(PaymentMethod):
    def pay(self, amount: float):
        print(f"paid {amount} via credit-card.")


class PayPal(PaymentMethod):
    def pay(self, amount: float):
        print(f"paid {amount} via paypal.")


# Abstraction - what is done (high level)
class PaymentPlatform(ABC):
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    @abstractmethod
    def process_payment(self, amount: float):
        pass


class MobileApp(PaymentPlatform):
    def process_payment(self, amount: float):
        self.payment_method.pay(amount=amount)
        print(f"processed payment through mobile app.")


class Website(PaymentPlatform):
    def process_payment(self, amount: float):
        self.payment_method.pay(amount=amount)
        print(f"processed payment through website.")


# Usage
if __name__ == "__main__":
    payment_platform = Website(payment_method=PayPal())
    payment_platform.process_payment(amount=132.99)
    payment_platform = MobileApp(payment_method=CreditCard())
    payment_platform.process_payment(amount=79.99)
