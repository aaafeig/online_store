class ProductQuantityError(Exception):

    def __init__(self, message="Невозможно добавить товар с нулевым количеством"):
        self.message = message
        super().__init__(self.message)
