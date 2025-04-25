from src.classes import Product


def test_mixin(capsys):
    product_example = Product("Тест", "Описание", 1000, 3)
    captured = capsys.readouterr()
    assert "Product(Тест, Описание, 1000, 3)" in captured.out
