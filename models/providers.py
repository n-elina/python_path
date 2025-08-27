import csv
from models.users import User, Status


class UserProvider:
    def get_users(self) -> list[User]:
        raise NotImplementedError


class CsvUserProvider(UserProvider):
    def get_users(self) -> list[User]:
        with open('/Users/Elina1518/PycharmProjects/python_path/python_basis/3/users.csv') as f:
            users = list(csv.DictReader(f, delimiter=';'))
        return [
            User(name=user['name'],
                 age=int(user['age']),
                 status=Status(user['status']),
                 items=user['items'])
            for user in users
        ]


class DataBaseUserProvider(UserProvider):
    def get_users(self) -> list[User]:
        pass


class ApiUserProvider(UserProvider):
    def get_users(self) -> list[User]:
        pass
