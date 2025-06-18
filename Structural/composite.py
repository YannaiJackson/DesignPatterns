from abc import ABC, abstractmethod
from typing import List


# Component Interface
class Worker(ABC):
    @abstractmethod
    def get_salary(self):
        pass

    @abstractmethod
    def list_employees(self, indent: int = 0):
        pass


# Leaf
class Employee(Worker):
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

    def list_employees(self, indent: int = 0):
        print(" " * indent + self.get_salary())


# Composite
class Manager(Worker):
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary
        self.employees: List[Worker] = []

    def add(self, employee: Worker):
        self.employees.append(employee)

    def get_salary(self):
        return f"Manager: {self.name}, Salary: {self.salary}"

    def list_employees(self, indent: int = 0):
        print(" " * indent + self.get_salary())
        for employee in self.employees:
            employee.list_employees(indent + 3)


# Usage
if __name__ == "__main__":
    worker1 = Employee(name="James", salary=25000)
    worker2 = Employee(name="Karen", salary=27000)
    worker3 = Manager(name="Arthur", salary=36000)
    worker4 = Manager(name="Mathew", salary=45000)
    worker3.add(employee=worker1)
    worker4.add(employee=worker3)
    worker3.add(employee=worker2)
    worker4.list_employees()
