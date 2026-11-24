from parcel_capacity_agents.config import DEFAULT_NAME
from parcel_capacity_agents.services.greeter import greet


def test_greet_default() -> None:
    assert greet(DEFAULT_NAME) == "Hello, world!"


def test_greet_loud() -> None:
    assert greet("User", loud=True) == "HELLO, USER!"
