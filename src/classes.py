from src.abstract_classes import BaseProduct, BaseOrder
from src.mixins import MixinLog
from src.excpetion_classes import ProductQuantityError


class Product(MixinLog, BaseProduct):
    products_list = []

    def __init__(self, name, description, price, quality):
        if quality == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

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
        return f"{self.name}, {self.price} руб. остаток: {self.quantity}"

    def __add__(self, other):
        if type(other) is type(self):
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError


class Category(BaseOrder):

    category_count = 0  # счетчик всех категорий
    product_count = 0  # счетчик количества продуктов всех экземпляров

    def __init__(self, name, description, products):
        super().__init__(name, description)
        self.__products = products
        Category.product_count += sum(product.quantity for product in self.__products)
        self.__count_price_product = sum(
            product.price * product.quantity for product in self.__products
        )  # сумма цен на уровне экземпляра
        self.__product_count = sum(
            product.quantity for product in self.__products
        )  # счетчик количества товара для 1 экземпляра
        Category.category_count += 1

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только экземпляры Product!")

        if product.quantity == 0:
            raise ProductQuantityError("Нельзя добавить товар с нулевым количеством!")

        self.__products.append(product)
        self.__product_count += product.quantity
        self.__count_price_product += product.price * product.quantity
        Category.product_count += product.quantity
        print(f"Товар {product.name} добавлен успешно")

    @property
    def products(self):
        return [str(product) for product in self.__products]

    @property
    def middle_price(self):
        try:
            avg_price = self.__count_price_product / self.__product_count
            return round(avg_price, 2)
        except Exception:
            return 0

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.__product_count}"


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

        if quantity == 0:
            raise ProductQuantityError

        super().__init__(product.name, product.description)
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity
        print("Товар добавлен")

    def __str__(self):
        return f"Заказ: {self.name}, {self.quantity} штук, {self.total_price} руб."
