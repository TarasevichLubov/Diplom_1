from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestData:
    burger_recept = f"(==== Слойка ====)\n= sauce Соус традиционный галактический =\n(==== Слойка ====)\n\nPrice: 60.35"
    SAUCE_INGREDIENT_NAME = 'Соус традиционный галактический'
    FILLING_INGREDIENT_NAME = 'Хрустящие минеральные кольца'
    ingredient_data = [
        [INGREDIENT_TYPE_SAUCE, SAUCE_INGREDIENT_NAME, 15.00],
        [INGREDIENT_TYPE_FILLING, FILLING_INGREDIENT_NAME, 300.00]
    ]
