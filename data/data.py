from dataclasses import dataclass
from random import randint


@dataclass
class Person:
        first_name: str = None
        last_name: str = None
        email: str = None
        current_address: str = None
        mobile: str = None
        subject: str = None
        gender: int = None