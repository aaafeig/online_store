class Product:
    products_list = []

    def __init__(self, name, description, price, quality):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quality

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


class Category:

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        self.product_count = sum(product.quantity for product in self.__products)
        Category.category_count += 1

    def add_product(self, product):
        self.__products.append(product)
        self.product_count += product.quantity

    @property
    def products(self):
        return [
            f"{product.name}, {product.price} руб., остаток {product.quantity} штук"
            for product in self.__products
        ]
