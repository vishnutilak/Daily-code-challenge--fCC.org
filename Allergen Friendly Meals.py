def get_allergen_friendly_meals(meals, allergens):
    avoid_set = set(allergens)
    safe_meals = []

    for meal_name, meal_allergens in meals:

        is_safe = True
        for allergen in meal_allergens:
            if allergen in avoid_set:
                is_safe = False
                break
        if is_safe:
            safe_meals.append(meal_name)
    return safe_meals
