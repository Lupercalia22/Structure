from abc import ABC, abstractmethod

class Kettle(ABC):
    def __init__(self, brand, capacity, material):
        self.brand = brand
        self.capacity = capacity
        self.material = material

    @abstractmethod
    def boil_water(self):
        pass

class ElectricKettle(Kettle):
    def __init__(self, brand, capacity, material, power):
        super().__init__(brand, capacity, material)
        self.power = power

    def boil_water(self):
        print("Boiling water with electric kettle...")

class GasKettle(Kettle):
    def __init__(self, brand, capacity, material, flame_size):
        super().__init__(brand, capacity, material)
        self.flame_size = flame_size

    def boil_water(self):
        print("Boiling water with gas kettle...")

#создание объектов
electric_kettle = ElectricKettle(brand="SomeBrand", capacity=1.7, material="Stainless steel", power=1500)
gas_kettle = GasKettle(brand="AnotherBrand", capacity=1.5, material="Aluminium", flame_size=10)

electric_kettle.boil_water()
gas_kettle.boil_water()