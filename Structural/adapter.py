from abc import ABC, abstractmethod


# Adaptee
class Payment:
    def credit_card_pay(self, amount: float):
        print(f"paying {amount} with credit card...")


# Target Interface
class CreditCardPayment(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass


# Adapter
class CreditCardPaymentAdapter(CreditCardPayment):
    def __init__(self, old_payment: Payment):
        self.old_payment = old_payment

    def pay(self, amount: float):
        self.old_payment.credit_card_pay(amount=amount)


# Usage
if __name__ == "__main__":
    old_payment_object = Payment()
    payment_adapter = CreditCardPaymentAdapter(old_payment_object)
    payment_adapter.pay(59.99)
