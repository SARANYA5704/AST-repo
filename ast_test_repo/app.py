from src.controllers.user_controller import create_user

def main():
    user = {"name": "Durai", "email": "durai@test.com"}
    create_user(user)

if __name__ == "__main__":
    main()
