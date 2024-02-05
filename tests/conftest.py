import pytest

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.data import TestData
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def bun():
    bun = Bun(name="Слойка", price=20.01)
    return bun


@pytest.fixture
def sauce_ingredient():
    sauce_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, TestData.SAUCE_INGREDIENT_NAME, 15.00)
    return sauce_ingredient


@pytest.fixture
def filling_ingredient():
    filling_ingredient = Ingredient(INGREDIENT_TYPE_FILLING, TestData.FILLING_INGREDIENT_NAME, 300.00)
    return filling_ingredient
