
# Subsystem Classes
class Validator:
    def validate(self, user_data):
        print("Validating user data...")
        if not user_data.get("email") or "@" not in user_data["email"]:
            raise ValueError("Invalid email")
        if len(user_data.get("password", "")) < 6:
            raise ValueError("Password too short")
        print("Validation passed.")


class Database:
    def save_user(self, user_data):
        print(f"Saving user '{user_data['email']}' to the database.")


class EmailService:
    def send_welcome_email(self, email):
        print(f"Sending welcome email to {email}.")


class AuditLogger:
    def log_registration(self, email):
        print(f"Logged registration for {email}.")


# Facade
class UserRegistrationFacade:
    def __init__(self):
        self.validator = Validator()
        self.database = Database()
        self.email_service = EmailService()
        self.logger = AuditLogger()

    def register_user(self, user_data):
        try:
            print("\n--- Registering User ---")
            self.validator.validate(user_data)
            self.database.save_user(user_data)
            self.email_service.send_welcome_email(user_data["email"])
            self.logger.log_registration(user_data["email"])
            print("--- Registration Complete ---\n")
        except ValueError as e:
            print(f"Registration failed: {e}")


# Usage
if __name__ == "__main__":
    user_data = {
        "email": "user@example.com",
        "password": "secret123"
    }

    registration = UserRegistrationFacade()
    registration.register_user(user_data)
