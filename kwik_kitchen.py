class Food:
    def __init__(self, attributes = {}):
        self.name = attributes["name"]
        self.carbs = attributes["carbs"]
        self.proteins = attributes["proteins"]
        self.fats = attributes["fats"]

    def __str__(self):
        return f"\nIn your standard serving of {self.name} you will find: {self.carbs} grams of carbs; {self.proteins} grams of proteins; and {self.fats} grams of fats."

    def int_food_total_calories(self):
        return ((self.carbs * 4) + (self.proteins * 4) + (self.fats * 9))

class Recipe:
    def __init__(self, attributes = {}):
        self.name = attributes["name"]
        self.ingredients = attributes["ingredients"]

    def __str__(self):
        return f"To make this lovely recipe for {self.name} you will need: {self.ingredients[0].name}; {self.ingredients[1].name}; and {self.ingredients[2].name}..."

    def int_recipe_total_calories(self):
        recipe_sum_total_calories = 0

        for ingredient in self.ingredients:
            recipe_sum_total_calories += ingredient.int_food_total_calories()

        return recipe_sum_total_calories

food_obj_bell_peppers = Food({"name": "Bell Peppers", "carbs": 12, "proteins": 5, "fats": 3})
food_obj_red_onions = Food({"name": "Red Onions", "carbs": 7, "proteins": 5, "fats": 2})
food_obj_beans = Food({"name": "Beans", "carbs": 33, "proteins": 100, "fats": 25})

arr_food_objs = [food_obj_bell_peppers, food_obj_red_onions, food_obj_beans]

i = 0
for food_obj in arr_food_objs:
    print(f"{i + 1} ==> {food_obj}")
    print(f"The total calorie count in a standard serving of {food_obj.name} is {food_obj.int_food_total_calories()}\n")
    i += 1

recipe_obj_bean_salad = Recipe({"name": "Bean Salad", "ingredients": arr_food_objs})
print(recipe_obj_bean_salad)
print(f"The total calorie count for your typical serving of {recipe_obj_bean_salad.name} is {recipe_obj_bean_salad.int_recipe_total_calories()}")

def str_get_chef_cmd():
    return input("Would you like to cook with us today? Press 'Q' to quit or 'GO' so we can 'GO' to the Kwik Kitchen XD\n> ")

def play():

    bool_chef_still_active = True

    while bool_chef_still_active:
        str_chef_cmd = str_get_chef_cmd()
        if str_chef_cmd in ['q', 'Q', 'quit', 'Quit']:
            print("It's been amazing having you in the kitchen today! One day you'll be a Head Chef :D")
            bool_chef_still_active = False
        else:
            print("Thank you for choosing to cook with us today :D it's going to be amazing XD")
            print("In the Kwik Kitchen you will be building recipes which take 3 ingredients - this is the Kwik Kitchen after all!!!")

            arr_new_food_objs = []

            while len(arr_new_food_objs) < 3:
                food_obj_attr_name = input("What is the name of the food you would like to have in your recipe?\n> ")
                food_obj_attr_carbs = int(input("How many grams of carbs are found in this food choice?\n> "))
                food_obj_attr_proteins = int(input("How many grams of proteins are found in this food choice?\n> "))
                food_obj_attr_fats = int(input("How many grams of fats are found in this food choice?\n> "))

                arr_new_food_objs.append(Food({"name": food_obj_attr_name, "carbs": food_obj_attr_carbs, "proteins": food_obj_attr_proteins, "fats": food_obj_attr_fats}))

            print("You will be adding the following ingredients to your recipe:\n")
            for index, new_food_obj in enumerate(arr_new_food_objs, 1):
                print(f"{index} ==> {new_food_obj.name}")

            print("Now it's time to bring all of those ingredients together for your Recipe xoxoxoxo")
            recipe_obj_attr_name = input("What would you like to call your recipe?\n> ")

            new_recipe_obj = Recipe({"name": recipe_obj_attr_name, "ingredients": arr_new_food_objs})

            print("Our proprietary AI and ML technologies can tell you all of the nutritional info about the recipe you've instructed us to make; let's see what we can learn below :D\n")

            print(new_recipe_obj)
            print(f"In your standard serving of {new_recipe_obj.name} you can expect to to find a total of {new_recipe_obj.int_recipe_total_calories()} calories... proceed with care... or don't XD")



play()
