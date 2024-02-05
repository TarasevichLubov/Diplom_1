import pytest

from praktikum.ingredient import Ingredient
from praktikum.data import TestData


class TestIngredients:

    @pytest.mark.parametrize(
        'ingredient_type, name, price', TestData.ingredient_data)
    def test_check_ingredients_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize(
        'ingredient_type, name, price', TestData.ingredient_data)
    def test_check_ingredients_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize(
        'ingredient_type, name, price', TestData.ingredient_data)
    def test_check_ingredients_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
