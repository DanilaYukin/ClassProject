class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        result = int(self.__price) * self.quantity + int(other.__price) * other.quantity
        return result

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            name=product_data.get("name", "Unknown"),
            description=product_data.get("description", ""),
            price=product_data.get("price", 0.0),
            quantity=product_data.get("quantity", 0)
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value


class Category():
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        result = 0
        for i in self.__products:
            result += i.quantity
        return f"{self.name}, количество продуктов: {result} шт."

    def add_product(self, product: Product):
        """Добавляет товар в приватный список товаров"""
        self.__products.append(product)

    @property
    def products(self):
        """Возвращает список товаров в формате строки"""
        formatted_products = []
        for product in self.__products:
            formatted_products.append(
                f"{product.name}, {product.__price} руб. Остаток: {product.quantity}шт.")
        return "\n".join(formatted_products)

    def get_products_list(self):
        """Возвращает список товаров в категории в виде строк"""
        return [f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт." for p in
                self.__products]
