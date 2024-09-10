def test_category(second_category):
    assert second_category.name == "Second Category"
    assert second_category.description == "Description of the Second category"


def test_category_initialization(first_category):
    """Тест: проверка начальной инициализации категории"""
    assert first_category.name == "Category"
    assert first_category.description == "Description of the category"


def test_add_product_to_category(first_category, product_1, product_2):
    """Тест: добавление товаров в категорию"""
    first_category.add_product(product_1)
    first_category.add_product(product_2)
    assert len(first_category.get_products_list()) == 2
    assert "Samsung Galaxy S23 Ultra" in first_category.get_products_list()[0]
    assert "Iphone 15" in first_category.get_products_list()[1]


def test_get_products_list(first_category, product_1, product_2):
    """Тест: проверка получения списка товаров"""
    first_category.add_product(product_1)
    first_category.add_product(product_2)
    products_list = first_category.get_products_list()
    expected_output = [
        'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.',
        'Iphone 15, 210000.0 руб. Остаток: 8 шт.'
    ]
    assert products_list == expected_output
