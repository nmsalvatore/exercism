"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from `dish_ingredients`."""
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    """Append "Cocktail" (alcohol)  or "Mocktail" (no alcohol) to `drink_name`, based on `drink_ingredients`."""
    for ingredient in drink_ingredients:
        if ingredient in ALCOHOLS:
            return drink_name + ' Cocktail'

    return drink_name + ' Mocktail'


def categorize_dish(dish_name, dish_ingredients):
    """Categorize `dish_name` based on `dish_ingredients`."""
    categories = {
        'VEGAN': VEGAN,
        'VEGETARIAN': VEGETARIAN,
        'KETO': KETO,
        'PALEO': PALEO,
        'OMNIVORE': OMNIVORE
    }

    for category_name, category in categories.items():
        category = set(category)

        if dish_ingredients.issubset(category):
            return f'{dish_name}: {category_name}'

    return f'{dish_name}: "OTHER"'


def tag_special_ingredients(dish):
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`."""
    return (dish[0], set(dish[1]) & SPECIAL_INGREDIENTS)


def compile_ingredients(dishes):
    """Create a master list of ingredients."""
    master_list = set()

    for dish in dishes:
        master_list = master_list | dish

    return master_list


def separate_appetizers(dishes, appetizers):
    """Determine which `dishes` are designated `appetizers` and remove them."""
    return set(dishes) - set(appetizers)


def singleton_ingredients(dishes, intersection):
    """Determine which `dishes` have a singleton ingredient (an ingredient that only appears once across dishes)."""
    singletons = set()

    for dish in dishes:
        singletons = singletons ^ dish

    return singletons - intersection
