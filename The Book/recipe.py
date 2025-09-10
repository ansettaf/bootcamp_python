#recipe.py
# recipe.py
class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        # Validate inputs
        if not isinstance(name, str) or not name:
            print("Error: name must be a non-empty string")
            exit(1)
        if not isinstance(cooking_lvl, int) or not (1 <= cooking_lvl <= 5):
            print("Error: cooking_lvl must be an integer between 1 and 5")
            exit(1)
        if not isinstance(cooking_time, int) or cooking_time < 0:
            print("Error: cooking_time must be a non-negative integer")
            exit(1)
        if not isinstance(ingredients, list) or not all(isinstance(i, str) for i in ingredients):
            print("Error: ingredients must be a list of strings")
            exit(1)
        if not isinstance(description, str):
            print("Error: description must be a string")
            exit(1)
        if recipe_type not in ["starter", "lunch", "dessert"]:
            print("Error: recipe_type must be 'starter', 'lunch' or 'dessert'")
            exit(1)

        # Assign attributes
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Returns the string to print with the recipe’s info"""
        txt = (
            f"Recipe: {self.name}\n"
            f"Cooking level: {self.cooking_lvl}\n"
            f"Cooking time: {self.cooking_time} minutes\n"
            f"Ingredients: {', '.join(self.ingredients)}\n"
            f"Description: {self.description if self.description else 'No description'}\n"
            f"Type: {self.recipe_type}"
        )
        return txt

