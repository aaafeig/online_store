class Product:
    def __init__(self, name, description, price, quality):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quality




class Category:
    product_count = 0
    category_count = 0
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)

