"""Make a program that can take in contents of your fridge, and recipes for meals you like to make. 
And returns meals you can make with the contents of fridge."""


def meal_list(fridge, meal_ingredients: list) -> bool:
    """Function takes in list of items in fridge and ingredients for meal and returns if fridge has all needed ingredients"""
    count = 0
    for ingredient in meal_ingredients:
        if ingredient in fridge:
            count += 1

    return count == len(meal_ingredients)


def meal_options(fridge, meals: list) -> list:
    """Takes in contents of fridge and list of meals consisting of tuples(meal,ingredients). And returns what meals that can be made"""
    meal_options_ls = []
    
    for meal, ingredients in meals:
        if meal_list(fridge,ingredients): meal_options_ls.append(meal)

    return meal_options_ls
