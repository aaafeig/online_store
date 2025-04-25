from src.abstract_classes import BaseProduct, BaseOrder
from src.Mixins import MixinLog


class Product(MixinLog, BaseProduct):
    products_list = []

    def __init__(self, name, description, price, quality):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quality
        super().__init__()

    @classmethod
    def new_product(cls, dict_ab_product):
        for product in cls.products_list:
            if product.name == dict_ab_product["name"]:
                product.quantity += dict_ab_product["quantity"]
                product.__price = max(product.__price, dict_ab_product["price"])
                return product

        new_product = cls(
            dict_ab_product["name"],
            dict_ab_product["description"],
            dict_ab_product["price"],
            dict_ab_product["quantity"],
        )
        cls.products_list.append(new_product)
        return new_product

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            if new_price < self.__price:
                ask_y_n = input("Вы точно хотите понизить цену ('y/n') ") == "y"
                if ask_y_n:
                    self.__price = new_price
            else:
                self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    def __str__(self):
        return f"{self.name}, {self.__price} руб. остаток: {self.quantity}"

    def __add__(self, other):
        if type(other) is type(self):
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError


class Category(BaseOrder):

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        super().__init__(name, description)
        self.__products = products
        self.__class__.product_count = sum(
            product.quantity for product in self.__products
        )
        Category.category_count += 1

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            self.__class__.product_count += product.quantity
        else:
            raise TypeError

    @property
    def products(self):
        return [str(product) for product in self.__products]

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.product_count}"


class CategoryIterator:

    def __init__(self, category):
        self.__products = category._Category__products
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index < len(self.__products):
            product = self.__products[self.__index]
            self.__index += 1
            return product
        else:
            raise StopIteration

class Order(BaseOrder):

    def __init__(self, product, quantity):
        super().__init__(product.name, product.description)
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

    def __str__(self):
        return f"Заказ: {self.name}, {self.quantity} штук, {self.total_price} руб."