import pytest
from src.classes import Product, Category


@pytest.fixture()
def product_test():
    product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    return product

@pytest.fixture()
def price_change():
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    return product

@pytest.fixture()
def category_test():
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    return category1

def test_price_change_null(price_change, monkeypatch):
    assert price_change.price == 210_000.0
    monkeypatch.setattr("builtins.input", lambda *args: "y")
    monkeypatch.setattr = 0.0
    assert price_change.price == 210_000.0

def test_price_change_disagree(price_change, monkeypatch):
    assert price_change.price == 210_000.0
    monkeypatch.setattr("builtins.input", lambda *args: "n")
    price_change.price = 100_000.0
    assert price_change.price == 210_000.0


def test_price_change_agree(price_change, monkeypatch):
    assert price_change.price == 210_000.0
    monkeypatch.setattr("builtins.input", lambda *args: "y")
    price_change.price = 100_000.0
    assert price_change.price == 100_000.0


def test_product(product_test):
    assert product_test.name == "Samsung Galaxy S23 Ultra"
    assert product_test.description == "256GB, Серый цвет, 200MP камера"
    assert product_test.price == 180_000.0
    assert product_test.quantity == 5
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 185000.0,
         "quantity": 3})
    assert product_test.name == "Samsung Galaxy S23 Ultra"
    assert product_test.description == "256GB, Серый цвет, 200MP камера"
    assert product_test.price == max(new_product.price, product_test.price)
    assert product_test.quantity == 8

def test_count(category_test):
    assert category_test.product_count == 27
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category_test.add_product(product4)

    assert category_test.product_count == 27 + product4.quantity
def test_category(category_test):
    assert category_test.name == "Смартфоны"
    assert (
        category_test.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_test.products == [
        "Samsung Galaxy S23 Ultra, 180000.0 руб., остаток 5 штук",
        "Iphone 15, 210000.0 руб., остаток 8 штук",
        "Xiaomi Redmi Note 11, 31000.0 руб., остаток 14 штук",
    ]
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category_test.add_product(product4)
    assert category_test.products == [
        "Samsung Galaxy S23 Ultra, 180000.0 руб., остаток 5 штук",
        "Iphone 15, 210000.0 руб., остаток 8 штук",
        "Xiaomi Redmi Note 11, 31000.0 руб., остаток 14 штук",
        '55" QLED 4K, 123000.0 руб., остаток 7 штук',
    ]
