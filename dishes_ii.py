class Food:
    def __init__(self, attributes = {}):
        self.name = attributes["name"]
        self.carbs = attributes["carbs"]
        self.proteins = attributes["proteins"]
        self.fats = attributes["carbs"]

    def __str__(self):
        return f"In your typical serving of {self.name} you can find: {self.carbs} grams of carbs; {self.proteins} grams of proteins; and {self.fats} grams of fats."

    def int_food_total_calories(self):
        return ((self.carbs * 4) + (self.proteins * 4) + (self.fats * 9))

class Recipe:
    def __init__(self, attributes = {}):
        self.name = attributes["name"]
        self.ingredients = attributes["ingredients"]

    def __str__(self):
        return f"\nTo make this recipe for {self.name} you will need: {self.ingredients[0].name}; {self.ingredients[1].name}; and {self.ingredients[2].name}."

    def int_recipe_total_calories(self):
        recipe_sum_total_calories = 0

        for ingredient in self.ingredients:
            recipe_sum_total_calories += ingredient.int_food_total_calories()
        return recipe_sum_total_calories

food_obj_beef = Food({"name": "Beef", "carbs": 20, "proteins": 25, "fats": 30})
food_obj_tomato = Food({"name": "Tomato", "carbs": 5, "proteins": 3, "fats": 2})
food_obj_onion = Food({"name": "Onion", "carbs": 2, "proteins": 3, "fats": 5})

arr_food_objs = [food_obj_beef, food_obj_tomato, food_obj_onion]

i = 0
for food_obj in arr_food_objs:
    print(f"\n({i + 1}). ==> {food_obj}")
    print(f"The total calorie composition of your standard portion of {food_obj.name} is {food_obj.int_food_total_calories()}")
    i += 1

recipe_obj_bolognaise = Recipe({"name": "Bolognaise", "ingredients": arr_food_objs})
print(f"\n\nThis perfect recipe for {recipe_obj_bolognaise.name} unfortunately contains {recipe_obj_bolognaise.int_recipe_total_calories()} worth of calories - proceed with caution but delight XD")
