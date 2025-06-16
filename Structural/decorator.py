from abc import ABC, abstractmethod


class Coffee:
    def __init__(self):
        self.price = 16.0

    def pay(self):
        print(f"Regular coffee, Total - {self.price}")


class CreamDecorator:
    def __init__(self, coffee: Coffee):
        self.price = coffee.price + 0.2

    def pay(self):
        print(f"Coffee with cream, Total - {self.price}")


# Usage
if __name__ == "__main__":
    first_coffee = Coffee()
    second_coffee = CreamDecorator(Coffee())
    first_coffee.pay()
    second_coffee.pay()
