import pytest
from src.classes import Product, Category


@pytest.fixture()
def product_test():
    return Product("Xiaomi TV A 50", "4K, темный цвет, Google assistant", 35000, 5)

@pytest.fixture()
def category_test():
    return  Category("Телевизор", "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
[product_test])