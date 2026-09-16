"""
Lightweight test-data factory. Avoids an external Faker dependency so the
framework has a minimal footprint, while still producing unique data per
test run (important for registration flows that require unique emails).
"""

import random, string, time
from dataclasses import dataclass

def _random_string(length:int = 8) -> str:
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))

def _random_digits(length:int = 6) -> str:
    return "".join(random.choice(string.digits) for _ in range(length))

@dataclass
class RegistrationData:
    email:str
    password:str


class TestData:
    @staticmethod
    def unique_email(prefix:str = "qa")->str:
        return f"{prefix}.{_random_string(6)}.{int(time.time()*1000)}@testmail.dev"

    @staticmethod
    def random_password() -> str:
        special_char = random.choice("!@#$%^&*")
        return f"Pass{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_lowercase)}{_random_digits(4)}{_random_string(4)}{special_char}"

    @staticmethod
    def new_registration()->RegistrationData:
        return RegistrationData(
            email = TestData.unique_email(),
            password = TestData.random_password()
        )
    @staticmethod
    def invalid_email()->str:
        return f"not-an-email-{_random_string(4)}"