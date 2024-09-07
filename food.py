class Food:
    def __init__(self, attributes = {}):
        self.name = attributes["name"]
        self.carbs = attributes["carbs"]
        self.protein = attributes["protein"]
        self.fat = attributes["fat"]

    def __str__(self):
        return f"In your typical {self.name} you will find: {self.carbs} grams of carbs; {self.protein} grams of protein; and {self.fat} grams of fat."

    def total_calories(self):
        return ((self.carbs * 4) + (self.protein * 4) + (self.fat * 9))

food_obj_eggs = Food({"name": "Eggs", "carbs": 100, "protein": 20, "fat": 50})
food_obj_milk = Food({"name": "Milk", "carbs": 13, "protein": 25, "fat": 60})
food_obj_flour = Food({"name": "Flour", "carbs": 20, "protein": 2, "fat": 20})

class Recipe:
    def __init__(self, attributes = {}):
        self.name = attributes["name"]
        self.ingredients = attributes["ingredients"]

    def __str__(self):
        return f"This recipe is called {self.name} and serves 8 people..."

    def recipe_total_calories(self):
        sum_calories = 0
        for ingredient in self.ingredients:
            sum_calories += ingredient.total_calories()

        return (f"The total amount of calories in a recipe for making {self.name} is {sum_calories}")

recipe_obj_cake = Recipe({"name": "Cake", "ingredients": [food_obj_eggs, food_obj_milk, food_obj_flour]})
print(recipe_obj_cake)
print(recipe_obj_cake.recipe_total_calories())

food_obj_beef = Food({"name": "beef", "carbs": 100, "protein": 200, "fat": 150})
food_obj_tomato = Food({"name": "Tomato", "carbs": 10, "protein": 5, "fat": 1})
food_obj_onion = Food({"name": "Onion", "carbs": 7, "protein": 7, "fat": 7})

recipe_obj_bolognaise = Recipe({"name": "Bolognaise", "ingredients": [food_obj_beef, food_obj_tomato, food_obj_onion]})
print(recipe_obj_bolognaise)
print(recipe_obj_bolognaise.recipe_total_calories())
