class Person:
    def __init__(self, name, age, favorite_foods):
        self.name = name
        self.age = age
        self.favorite_foods = favorite_foods

    def birth_year(self):
        return (2015 - self.age)

arr_people = [Person("Ed", 23, ["Carrots", "Cucumbers"]), Person("Edd", 24, ['Bell Peppers', 'Red Onions']), Person("Eddy", 25, ['Spinach', 'Mushrooms'])]

for person in arr_people:
    print(f"Say hi to {person.name} everyone! {person.name} is {person.age} years old and loves to eat {person.favorite_foods[0]} and {person.favorite_foods[1]}")

print("")
