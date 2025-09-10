# book.py
from recipe import Recipe
from datetime import datetime

class Book:
    def __init__(self, name):
        if not isinstance(name, str) or not name:
            print("Error: book name must be a non-empty string")
            exit(1)
        self.name = name
        self.creation_date = datetime.now()
        self.last_update = self.creation_date
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name 'name' and returns the instance"""
        for r_type in self.recipes_list:
            for recipe in self.recipes_list[r_type]:
                if recipe.name == name:
                    print(recipe)
                    return recipe
        print("Recipe not found")
        return None

    def get_recipes_by_types(self, recipe_type):
        """Gets all recipes names for a given recipe_type"""
        if recipe_type not in self.recipes_list:
            print("Invalid recipe type")
            return []
        return [recipe.name for recipe in self.recipes_list[recipe_type]]

    def add_recipe(self, recipe):
        """Adds a recipe to the book and updates last_update"""
        if not isinstance(recipe, Recipe):
            print("Error: You can only add Recipe objects")
            return
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()

