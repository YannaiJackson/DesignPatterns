from abc import ABC, abstractmethod


# Abstract handler
class Validator(ABC):
    def __init__(self):
        self._next = None

    def set_next(self, next_validator):
        self._next = next_validator
        return next_validator

    def validate(self, data):
        self._check(data)
        if self._next:
            self._next.validate(data)

    def _check(self, data):
        pass


# Concrete validators
class UsernameValidator(Validator):
    def _check(self, data):
        if not data.get("username"):
            raise ValueError("Username cannot be empty")


class PasswordValidator(Validator):
    def _check(self, data):
        if len(data.get("password", "")) < 8:
            raise ValueError("Password must be at least 8 characters")


class EmailValidator(Validator):
    def _check(self, data):
        email = data.get("email", "")
        if "@" not in email:
            raise ValueError("Invalid email address")


# Usage
if __name__ == "__main__":
    validator_chain = UsernameValidator()
    validator_chain.set_next(PasswordValidator()).set_next(EmailValidator())
    form_data = {
        "username": "johndoe",
        "password": "strongpass123",
        "email": "john@example.com"
    }
    validator_chain.validate(form_data)
