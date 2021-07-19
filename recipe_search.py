import requests
from flask import Flask, render_template, url_for

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
ingr_recipes_database = []


# Creating a function calling recipe_search function and creating dictionary on each loop
def run():
    results = recipe_search()

    # Creating dictionary with keys and empty values
    recipe_dict = {'recipe_name': '', 'recipe_webpage': '', 'recipe_image': ''}

    # Looping through results
    for result in results:
        recipe = result['recipe']

        # Adding values on each iteration
        recipe_dict['recipe_name'] = recipe['label']
        recipe_dict['recipe_webpage'] = recipe['url']
        recipe_dict['recipe_image'] = recipe['image']

        # Creating a copy of a dictionary to add unique dictionary to the list on each iteration
        ingr_recipes_database.append(recipe_dict.copy())

        print(recipe['label'])
        print(recipe['url'])
        print(recipe['image'])

        # print()


run()

print(ingr_recipes_database)


# Using Flask to create routes to display our code on the webpage
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', recipes=ingr_recipes_database)

if __name__ == '__main__':
    app.run(debug=True)

