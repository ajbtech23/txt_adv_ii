class Food:
    def __init__(self, attributes = {}):
        self.name = attributes["name"]
        self.carbs = attributes["carbs"]
        self.proteins = attributes["proteins"]
        self.fats = attributes["fats"]

    def __str__(self):
        return f"In your typical {self.name} you can friend {self.carbs} grams of carbs; {self.proteins} grams of proteins; and {self.fats} grams of fat"

    def int_food_total_calories(self):
        return ((self.carbs * 4) + (self.proteins * 4) + (self.fats * 9))

class Recipe:
    def __init__(self, attributes = {}):
        self.name = attributes["name"]
        self.description = attributes["description"]
        self.ingredients = attributes["ingredients"]

    def __str__(self):
        return f"This {self.name} {self.description} and contains the following ingredients: {self.ingredients[0]}, {self.ingredients[1]} and {self.ingredients[2]}"

    def int_recipe_total_calories(self):

        recipe_sum_total_calories = 0
        for ingredient in self.ingredients:
            recipe_sum_total_calories += ingredient.int_food_total_calories()
        return recipe_sum_total_calories
