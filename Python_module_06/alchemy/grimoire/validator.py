VALID_ELEMENTS = ["fire", "water", "earth", "air"]


def validate_ingredients(ingredients: str) -> str:

    ingredients_lower = ingredients.lower()
    for element in VALID_ELEMENTS:
        if element in ingredients_lower:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"