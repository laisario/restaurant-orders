from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, restriction_map
import pytest


# Req 2
def test_dish():
    massa_de_lasanha = Dish('massa de lasanha', 19.90)
    arroz = Dish('Arroz', 7.50)

    assert massa_de_lasanha.name == 'massa de lasanha'
    assert massa_de_lasanha.price == 19.90
    assert repr(massa_de_lasanha) == "Dish('massa de lasanha', R$19.90)"
    assert massa_de_lasanha.__eq__(other=arroz) is False
    assert massa_de_lasanha.__eq__(other=massa_de_lasanha) is True
    assert hash(massa_de_lasanha) != hash(arroz)
    assert hash(massa_de_lasanha) == hash(massa_de_lasanha)

    with pytest.raises(TypeError):
        Dish('Inválido', 'blabla')
    with pytest.raises(ValueError):
        Dish('Inválido', -7)

    ingredients = set()
    queijo = Ingredient('queijo parmesão')
    ingredients.add(queijo)
    massa_de_lasanha.add_ingredient_dependency(queijo, 5)
    restrictions = restriction_map().get('queijo parmesão')
    assert massa_de_lasanha.get_ingredients() == ingredients
    assert massa_de_lasanha.recipe == {queijo: 5}
    assert massa_de_lasanha.get_restrictions() == restrictions
