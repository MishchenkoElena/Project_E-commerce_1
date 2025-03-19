class Product:
    """Класс определения списка товаров"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is Product:
            return self.__price * self.quantity + other.price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, new_product_data, products_list):
        """Метод, который принимает на вход параметры товара в словаре и возвращает созданный объект класса Product"""
        for product in products_list:
            if product.name == new_product_data["name"]:
                product.quantity += new_product_data["quantity"]
                product.price = max(product.price, new_product_data["price"])
                return product
        name = new_product_data["name"]
        description = new_product_data["description"]
        price = new_product_data["price"]
        quantity = new_product_data["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Геттер для приватного атрибута price"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для проверки/изменения цены товара при добавлении в список товаров"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        elif new_price < self.__price:
            user_choice = input("Вы действительно хотите снизить цену товара? (y/n)\n").strip().lower()
            if user_choice != "y":
                return
        self.__price = new_price


class Category:
    """Класс определения категорий товаров"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0
    products_list = []

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product):
        """Метод для добавления товаров в категорию"""
        self.__products.append(product)
        Category.product_count += 1
        Category.products_list.append(product)

    @property
    def products(self):
        """Геттер, который выводит список товаров в виде строк"""
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    @property
    def products_in_list(self):
        """Геттер, который выводит список товаров в виде списка"""
        return self.__products
