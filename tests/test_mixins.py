from src.classes import Product


def test_mixin_log():
    product_example = Product("Тест", "Описание", 1000, 3)
    assert repr(product_example) == "Product(Тест, Описание, 1000, 3)"
