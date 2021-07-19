import requests
from flask import Flask, render_template, url_for

app = Flask(__name__)

# Asking user to enter an ingredient
ingredient = input('Enter an ingredient: ')
mealType = input('Choose one of the following: Breakfast, Dinner, Lunch, Snack, Teatime ')

# Setting query parameters for the API request (including user ingredient input variable)
parameters = {
    "app_id": 'f0380e88',
    "app_key": 'fcca981a2897d3184653e65cf6656a56',
    "q": ingredient,
    "type": "public",
    "mealType": mealType
}

# Function containing API request and .json method to return JSON object of the result. N.B. received result is a
# list of dictionaries
def recipe_search():
    recipe_request = requests.get("https://api.edamam.com/api/recipes/v2", parameters)
    data = recipe_request.json()
    return data["hits"]

# Creating an empty array to temporarily store users search results
ingredient_recipes_database = []

# Creating a function calling recipe search function and storing results in the list of dictionaries recipe
def run():
   results = recipe_search()
   for result in results:
       recipe = result['recipe']
       print(recipe['label'])
       print(recipe['url'])
       print()


run()

#ingredient_recipe_database = recipe_search()


# Printing first result from the database for user's chosen ingredient
# print(ingredient_recipe_database)
# print(ingredient_recipe_database[0]['recipe']['label'])
# print(ingredient_recipe_database[0]['recipe']['shareAs'])
