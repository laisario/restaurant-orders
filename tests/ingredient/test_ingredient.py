from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient('tomate')
    other_ingredient = Ingredient('presunto')
    assert ingredient.name == 'tomate'
    assert other_ingredient.restrictions != set()
    assert repr(ingredient) == "Ingredient('tomate')"
    assert ingredient.__eq__(other=other_ingredient) is False
    assert ingredient.__eq__(other=ingredient) is True
    assert hash(ingredient) != hash(other_ingredient)
    assert hash(ingredient) == hash(ingredient)
