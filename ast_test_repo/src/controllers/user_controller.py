from src.services.user_service import UserService

def create_user(user_data):
    service = UserService()
    return service.create_user(user_data)
