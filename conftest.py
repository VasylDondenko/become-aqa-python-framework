import pytest

from src.config.config import config


class User:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def remove(self):
        # DB interactions
        self.name = None
        self.age = None


@pytest.fixture(scope="function")
def user():
    # before test
    print("Create user")
    user = User(config.get("BASE_URL_UI"), 42)

    # pass user object to test
    yield user

    # after test
    print("Remove user")
    user.remove()
