class Person:
    def __init__(self, name, age, favorite_foods):
        self.name = name
        self.age = age
        self.favorite_foods = favorite_foods

    def __str__(self):
        return f"Hi my name is {self.name} and it's lovely to meet you :D"

    def birth_year(self):
        return (2015 - self.age)

arr_people = [Person("Ed", 23, ["Carrots", "Cucumbers"]), Person("Edd", 24, ['Bell Peppers', 'Red Onions']), Person("Eddy", 25, ['Spinach', 'Mushrooms'])]

for person in arr_people:
    print(f"Say hi to {person.name} everyone! {person.name} is {person.age} years old and loves to eat {person.favorite_foods[0]} and {person.favorite_foods[1]}")

print("")

age_sum = 0
year_sum = 0

for person in arr_people:
    age_sum += person.age
    year_sum += person.birth_year()

print(f"The average age of our avatars is {age_sum/len(arr_people)}")
print(f"The average year of birth across our avatars is {year_sum/len(arr_people)}")

print(arr_people[0])
