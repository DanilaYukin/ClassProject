import pytest

from src.main import Category
from src.main import Product


@pytest.fixture()
def product_1():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5
    )


@pytest.fixture()
def product_2():
    return Product(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8
    )


@pytest.fixture()
def product_3():
    return Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14
    )


@pytest.fixture
def first_category(product_1, product_2):
    return Category(
        name="Category",
        description="Description of the category",
        products=[product_1, product_2]
    )


@pytest.fixture
def second_category(product_2, product_3, product_1):
    return Category(
        name="Second Category",
        description="Description of the Second category",
        products=[product_1, product_2, product_3]
    )
