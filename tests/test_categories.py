import pytest

from src.categories import Smartphone, LawnGrass


@pytest.fixture
def smartphone():
    smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    return smartphone


@pytest.fixture
def lawn_grass():
    grass = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    return grass


def test_smartphone(smartphone):
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"


def test_lawn_grass(lawn_grass):
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == "7 дней"
    assert lawn_grass.color == "Зеленый"


def test_add(smartphone):
    smartphone2 = Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )
    assert (
        int(smartphone + smartphone2)
        == smartphone.price * smartphone.quantity
        + smartphone2.price * smartphone2.quantity
    )


def test_add_fall(smartphone, lawn_grass):
    with pytest.raises(TypeError):
        smartphone + lawn_grass
