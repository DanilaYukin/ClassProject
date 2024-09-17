import pytest

from src.main import Product


def test_product_1(product_1):
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


def test_product_2(product_2):
    assert product_2.name == "Iphone 15"
    assert product_2.description == "512GB, Gray space"
    assert product_2.price == 210000.0
    assert product_2.quantity == 8


def test_product_3(product_3):
    assert product_3.name == "Xiaomi Redmi Note 11"
    assert product_3.description == "1024GB, Синий"
    assert product_3.price == 31000.0
    assert product_3.quantity == 14


def test_initial_price(product_1):
    """Тест: проверка начальной установки цены"""
    assert product_1.price == 180000.0


def test_set_valid_price(product_1):
    """Тест: установка корректной цены"""
    product_1.price = 899.99
    assert product_1.price == 899.99


def test_set_invalid_price_negative(product_1):
    """Тест: установка отрицательной цены"""
    product_1.price = -100
    assert "Цена не должна быть нулевая или отрицательная"
    assert product_1.price == 180000.0  # Цена не должна измениться


def test_set_invalid_price_zero(product_1):
    """Тест: установка нулевой цены"""
    product_1.price = 0
    assert "Цена не должна быть нулевая или отрицательная"
    assert product_1.price == 180000.0  # Цена не должна измениться


def test_new_product_creation():
    """Тест: создание продукта через словарь"""
    product_data = {
        "name": "Tablet",
        "description": "Latest tablet model",
        "price": 600.00,
        "quantity": 6
    }
    new_product = Product.new_product(product_data)
    assert new_product.name == "Tablet"
    assert new_product.description == "Latest tablet model"
    assert new_product.price == 600.00
    assert new_product.quantity == 6


def test_str_product(product_1):
    assert Product.__str__(product_1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_add_product(product_1, product_2, product_6, product_7):
    assert Product.__add__(product_1, product_2) == 2580000
    assert Product.__add__(product_6, product_7) == 16750


def test_product_6(product_6):
    assert product_6.name == "Газонная трава"
    assert product_6.description == "Элитная трава для газона"
    assert product_6.price == 500.0
    assert product_6.quantity == 20
    assert product_6.country == "Россия"
    assert product_6.germination_period == "7 дней"
    assert product_6.color == "Зеленый"


def test_product_4(product_4):
    assert product_4.name == "Samsung Galaxy S23 Ultra"
    assert product_4.description == "256GB, Серый цвет, 200MP камера"
    assert product_4.price == 180000.0
    assert product_4.quantity == 5
    assert product_4.model == "S23 Ultra"
    assert product_4.efficiency == 95.5
    assert product_4.memory == 256
    assert product_4.color == "Серый"


def test_zero_quantity():
    with pytest.raises(ValueError):
        Product.__init__(Product(
            name="Iphone 15",
            description="512GB, Gray space",
            price=210000.0,
            quantity=0
        ))
