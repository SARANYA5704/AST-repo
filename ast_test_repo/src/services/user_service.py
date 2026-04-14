from src.repositories.user_repository import UserRepository
from src.utils.helper import validate_email

class UserService:

    def create_user(self, user_data):
        if not validate_email(user_data.get("email")):
            raise ValueError("Invalid email")

        repo = UserRepository()
        return repo.save(user_data)

    def unused_function(self):
        print("This function is never used")
