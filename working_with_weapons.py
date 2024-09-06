# I wonder how much of what I've picked up in Ruby can be applied to Python
class Weapon:
    def __init__(self, attributes = {}):
        self.name = attributes["name"]
        self.description = attributes["description"]
        self.atk_power = attributes["atk_power"]

    def __str__(self):
        return f"{self.name}: {self.description} with an attack power of {self.atk_power}"

    def int_power_up(self):
        return (self.atk_power * 10)

class BattleAxe(Weapon):
    # Extension with modifications made to val returned from parent class
    def int_power_up(self):
        return (super().int_power_up() + 23)

    def str_placeholder():
        return "Be Easy"

class LongSword(Weapon):
    # Extension with modifications made to val returned from parent class
    def int_power_up(self):
        return (super().int_power_up() + 33)

class Rapier(Weapon):
    # Overiding
    def int_power_up(self):
        return (self.atk_power * 1000)

class BroadSword(Weapon):
    # Invoking the identical method in the parent class forcibly versus allowing to take place passively via absence of method which drives inheritance
    def int_power_up(self):
        return super().int_power_up()


test_battleaxe = BattleAxe({"name": "Mjolnir", "description": "famed weapon of legend", "atk_power": 75})
test_longsword = LongSword({"name": "OathKeeper", "description": "remarkable AOE and long term damage", "atk_power": 80})
test_rapier = Rapier({"name": "Kamusari", "description": "one thrust is all it takes to decimate", "atk_power": 95})
test_broadsword = BroadSword({"name": "Widows Wail", "description": "weapon of mass destruction", "atk_power": 150})

arr_weapons = [test_battleaxe, test_longsword, test_rapier, test_broadsword]

for weapon in arr_weapons:
    print(weapon)

print("")
for weapon in arr_weapons:
    print(f"When powered up the {weapon.name} has an ultimate attack power of {weapon.int_power_up()}")
