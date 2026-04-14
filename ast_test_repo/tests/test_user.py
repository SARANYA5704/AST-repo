from src.services.user_service import UserService

def test_create_user():
    service = UserService()
    user = {"name": "Test", "email": "test@test.com"}
    assert service.create_user(user) == True
