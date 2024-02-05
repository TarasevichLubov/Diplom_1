from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.data import TestData
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestBurger:

    def test_create_burger_true(self):
        burger = Burger()
        assert burger.bun is None and burger.ingredients == []

    def test_setting_bun_for_burger(self, bun):
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredients_for_burger_ture(self):
        burger = Burger()
        mock_ingredients = Mock()
        mock_ingredients.name = TestData.SAUCE_INGREDIENT_NAME
        mock_ingredients.type = INGREDIENT_TYPE_SAUCE
        mock_ingredients.price = 2.01
        burger.add_ingredient(mock_ingredients)
        assert burger.ingredients[0] == mock_ingredients

    def test_remove_ingredients_from_burger_true(self):
        burger = Burger()
        mock_ingredients = Mock()
        mock_ingredients.name = TestData.SAUCE_INGREDIENT_NAME
        mock_ingredients.type = INGREDIENT_TYPE_SAUCE
        mock_ingredients.price = 2.01
        burger.add_ingredient(mock_ingredients)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredients_in_burger(self, sauce_ingredient, filling_ingredient):
        burger = Burger()
        burger.add_ingredient(sauce_ingredient)
        burger.add_ingredient(filling_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == sauce_ingredient

    def test_mock_burger_price(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 20.10

        mock_ingredients = Mock()
        mock_ingredients.get_price.return_value = 20.15

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredients)
        burger_price = burger.get_price()
        assert burger_price == 60.35

    def test_recept_burger_mock(self, bun, sauce_ingredient):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "Слойка"
        mock_bun.get_price.return_value = 20.10

        mock_ingredients = Mock()
        mock_ingredients.get_type.return_value = 'SAUCE'
        mock_ingredients.get_name.return_value = "Соус традиционный галактический"
        mock_ingredients.get_price.return_value = 20.15

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredients)
        assert burger.get_receipt() == TestData.burger_recept
