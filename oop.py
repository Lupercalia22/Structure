class Water:
    def __init__(self, amount):
        self.amount = amount

class Stove:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print("Stove is on")

    def turn_off(self):
        self.is_on = False
        print("Stove is off")

class Kettle:
    def __init__(self, capacity):
        self.capacity = capacity
        self.water = None

    def add_water(self, water):
        if not self.water:
            self.water = water
            print("Water added to kettle")
        else:
            print("Kettle is already filled with water")

    def boil_water(self, stove):
        if stove.is_on and self.water:
            print("Water is boiling")
        else:
            print("Cannot boil water. Check if stove is on and kettle has water")

    def pour_water(self):
        if self.water:
            print(f"{self.water.amount} ml of water poured")
            self.water = None
        else:
            print("Kettle is empty")

class Sink:
    def __init__(self):
        self.water_level = 0

    def fill_sink(self, water):
        self.water_level += water.amount
        print("Sink filled with water")


water = Water(500)  
kettle = Kettle(1000)
stove = Stove() 
sink = Sink() 

kettle.add_water(water) 
stove.turn_on() 
kettle.boil_water(stove) 
kettle.pour_water() 
sink.fill_sink(water) 
