class Person:
    age = 15
    name = "Rolf"
    favorite_foods = ['Beets', 'Turnips', 'Weisswurst']

    def birth_year(self):
        return (2015 - self.age)

test_person = Person()

print(test_person.birth_year())

arr_people = [Person(), Person(), Person()]

sum = 0
for person in arr_people:
    sum += person.age

print(f"The average age is: {str(sum / len(arr_people))}")
