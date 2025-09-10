# test.py
from recipe import Recipe
from book import Book

# Create recipes
pancakes = Recipe(
    "Pancakes", 
    2, 
    15, 
    ["flour", "milk", "eggs"], 
    "Fluffy pancakes for breakfast", 
    "dessert"
)

salad = Recipe(
    "Salad", 
    1, 
    10, 
    ["lettuce", "tomato", "cucumber"], 
    "",  # empty description
    "starter"
)

# Create book
my_cookbook = Book("My Cookbook")

# Add recipes
my_cookbook.add_recipe(pancakes)
my_cookbook.add_recipe(salad)

# Get recipe by name
my_cookbook.get_recipe_by_name("Pancakes")

# Get recipes by type
print("Starters:", my_cookbook.get_recipes_by_types("starter"))
print("Desserts:", my_cookbook.get_recipes_by_types("dessert"))

# Attempt to add invalid recipe
my_cookbook.add_recipe("Not a recipe")  # Should show error
