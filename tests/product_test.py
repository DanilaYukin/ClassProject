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
