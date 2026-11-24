# Import from elsewhere in the package: absolute (always starts with the package name).
from parcel_capacity_agents.config import APP_NAME, DEFAULT_NAME
from parcel_capacity_agents.services.greeter import greet


def main() -> None:
    print(f"Starting {APP_NAME}...")
    print(greet(DEFAULT_NAME))
