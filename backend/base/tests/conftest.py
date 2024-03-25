import pytest
from faker import Faker


@pytest.fixture
def user_data():
    fake = Faker()
    return {
        "name": fake.name(),
        "email": fake.email(),
        "password": fake.password(),
    }
