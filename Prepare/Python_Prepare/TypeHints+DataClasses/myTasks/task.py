from dataclasses import dataclass
from typing import Optional
import random
import string

@dataclass
class TestUser:
    username: str
    email : str
    phone: Optional[str] = "+79990001122"
    is_active : bool = True

    def __post_init__(self):
       if "@" not in self.email:
           raise ValueError("Email must contain @")

    def deactivate(self) -> None:
        self.is_active = False


    @classmethod
    def create_random_user(cls) -> "TestUser":
        random_name = ''.join(random.choices(string.ascii_lowercase, k = 8))
        return cls(
            username = random_name,
            email = f"{random_name}@test.com"
        )