
class UsersProvider:

    @staticmethod
    def fake_user():
        return {
            "login": "dasdasdasdsada",
            "id": 4324234,
        }

    @staticmethod
    def existing_user():
        return {
            "login": "defunkt",
            "id": 2,
        }

    @staticmethod
    def login_user_exists():
        return {
            "username": "kateryna122",
            "password": "S****!",
        }

    @staticmethod
    def login_user_non_exists():
        return {
            "username": "dsdafsdgddffdg",
            "password": "gfgdfgdfgdfgd",
        }