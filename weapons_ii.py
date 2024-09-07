class Weapon:

    def __init__(self, attributes = {}):
        self.name = attributes["name"]
        self.description = attributes["description"]
        self.atk_power = attributes["atk_power"]

    def __str__(self):
        return f"{self.name}: {self.description} with an attack power of {self.atk_power}"

    def int_atk_power_boost(self):
        return (self.atk_power * 30)

class Axe(Weapon):
    # In the absence of the instance method int_atk_power_boost this child class will search for the instance method in parent class, find it and then invoke automatically
    def str_placeholder(self):
        return "Here so I don't get fined..."

class Sword(Weapon):
    # Inherit but invoke identical instance method via parent
    def int_atk_power_boost(self):
        return super().int_atk_power_boost()

class Mace(Weapon):
    # Inherit but override
    def int_atk_power_boost(self):
        return (self.atk_power * 100)

class LongBow(Weapon):
    # Inherit, invoke and extend
    def int_atk_power_boost(self):
        return (super().int_atk_power_boost() + 23)

obj_axe = Axe({"name": "Axe", "description": "perfect for close combat", "atk_power": 85})
obj_sword = Sword({"name": "Sword", "description": "razor sharp and deadly against strong foes", "atk_power": 75})
obj_mace = Mace({"name": "Mace", "description": "capable of turning even the strongest skulls into mush", "atk_power": 90})
obj_longbow = LongBow({"name": "Long Bow", "description": "in the hands of a skilled marksman the largest of armies will fall", "atk_power": 99})

arr_weapons = [obj_axe, obj_sword, obj_mace, obj_longbow]

i = 0
for weapon in arr_weapons:
    print(f"{i + 1}. {weapon}")
    i += 1

print("")

for index, weapon in enumerate(arr_weapons, 1):
    print(f"{index}. {weapon.name} when boosted can see it's attack power increase from {weapon.atk_power} to {weapon.int_atk_power_boost()}")
