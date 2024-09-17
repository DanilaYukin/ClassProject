from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def work_class(self):
        """Функция для отработки пройденного материала"""
        print("Abstract класс")


class MixinLog:

    def __init__(self):
        print(repr(self))
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"


class Product(BaseProduct, MixinLog):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def work_class(self):
        """Функция для отработки пройденного материала"""
        print("Product класс")

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) == type(self):
            result = int(self.__price) * self.quantity + int(other.__price) * other.quantity
            return result
        raise TypeError

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            name=product_data.get("name", "Unknown"),
            description=product_data.get("description", ""),
            price=product_data.get("price", 0.0),
            quantity=product_data.get("quantity", 0),
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


class Category:
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

    def add_product(self, product):
        """Добавляет товар в приватный список товаров"""
        if isinstance(product, Product):
            return self.__products.append(product)
        raise TypeError

    @property
    def products(self):
        """Возвращает список товаров в формате строки"""
        formatted_products = []
        for product in self.__products:
            formatted_products.append(f"{product.name}, {Product.price} руб. Остаток: {product.quantity}шт.")
        return "\n".join(formatted_products)

    def get_products_list(self):
        """Возвращает список товаров в категории в виде строк"""
        return [f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт." for p in self.__products]


class Smartphone(Product, MixinLog):
    name: str
    description: str
    price: float
    quantity: int
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.__price = price
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def work_class(self):
        """Функция для отработки пройденного материала"""
        print("Smartphone класс")


class LawnGrass(Product, MixinLog):
    name: str
    description: str
    price: float
    quantity: int
    country: str
    germination_period: str
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.__price = price
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def work_class(self):
        """Функция для отработки пройденного материала"""
        print("LawnGrass класс")


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)