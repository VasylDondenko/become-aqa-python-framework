import pytest

from src.config.config import config


class User:
    def __init__(self, name, password, age) -> None:
        self.name = name
        self.password = password
        self.age = age

    def remove(self):
        # DB interactions
        self.name = None
        self.age = None


@pytest.fixture(scope="function")
def user():
    # before test
    print("Create user")
    user = User(config.get("USER_LOGIN"), config.get("USER_PASSWORD"), 42)

    # pass user object to test
    yield user

    # after test
    print("Remove user")
    user.remove()
