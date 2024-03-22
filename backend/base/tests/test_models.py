import pytest
from django.contrib.auth.models import User
from base.models import Product
from faker import Faker
from django.core.exceptions import ValidationError

fake = Faker()


@pytest.fixture
def user():
    return User.objects.create_user(username="testuser", password="12345")


@pytest.fixture
def product(user):
    return Product.objects.create(
        user=user,
        name=fake.name(),
        image=fake.image_url(),
        brand=fake.company(),
        category=fake.random_element(elements=("Electronics", "Clothing", "Books")),
        description=fake.text(),
        rating=fake.pydecimal(left_digits=1, right_digits=2, positive=True),
        price=fake.pydecimal(left_digits=4, right_digits=2, positive=True),
    )


@pytest.mark.django_db
def test_product_creation(product):
    assert product.pk is not None


@pytest.mark.django_db
def test_product_string_representation(product):
    assert str(product) == product.name


@pytest.mark.django_db
def test_product_default_values(product):
    assert product.numReviews == 0
    assert product.countInStock == 0
