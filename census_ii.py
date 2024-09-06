class Person:
    age = 20
    name = "Joshua"
    favorite_foods = ['Lasagna', 'Pizza', 'Pasta']

    def birth_year(self):
        return (2015 - self.age)

people = [Person(), Person(), Person()]

people[0].name = "Damian"
people[0].age = "23"
people[0].favorite_foods = ['Pounded Yam', 'Egusi with assorted meats', 'Ogbono Soup']

print(f"{people[0].name} is {people[0].age} years old and likes to eat {', '.join(people[0].favorite_foods)}")
