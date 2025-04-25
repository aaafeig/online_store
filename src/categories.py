from .classes import Product


class Smartphone(Product):
    def __init__(
        self, name, description, price, quality, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quality)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self, name, description, price, quality, country, germination_period, color
    ):
        super().__init__(name, description, price, quality)
        self.country = country
        self.germination_period = germination_period
        self.color = color
