import pytest


class User:
    def __init__(self, age=42) -> None:
        self.age = age

    def remove(self):
        # DB interactions
        self.age = None


@pytest.fixture(scope="function")
def user():
    # before test
    print("Create user")
    user = User(42)

    # pass user object to test
    yield user

    # after test
    print("Remove user")
    user.remove()
