class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def turn_on(self):
        print(f"{self.brand} {self.model} is turned on.")

    def turn_off(self):
        print(f"{self.brand} {self.model} is turned off.")


class CoffeeMachine(Device):
    def __init__(self, brand, model, water_reservoir_capacity):
        super().__init__(brand, model)
        self.water_reservoir_capacity = water_reservoir_capacity

    def brew_coffee(self):
        print(f"Brewing coffee with {self.brand} {self.model}.")

    def refill_water(self):
        print(f"Refilling water in {self.brand} {self.model}.")


class Blender(Device):
    def __init__(self, brand, model, max_speed):
        super().__init__(brand, model)
        self.max_speed = max_speed

    def blend(self):
        print(f"Blending with {self.brand} {self.model}.")

    def set_speed(self, speed):
        print(f"Setting speed to {speed} on {self.brand} {self.model}.")


class MeatGrinder(Device):
    def __init__(self, brand, model, power):
        super().__init__(brand, model)
        self.power = power

    def grind_meat(self):
        print(f"Grinding meat with {self.brand} {self.model}.")

    def clean(self):
        print(f"Cleaning {self.brand} {self.model}.")


coffee_machine = CoffeeMachine("CoffeeBrand", "ModelX", 1000)
coffee_machine.turn_on()
coffee_machine.refill_water()
coffee_machine.brew_coffee()
coffee_machine.turn_off()

blender = Blender("BlenderCo", "BlenderZ", 1500)
blender.turn_on()
blender.set_speed(3)
blender.blend()
blender.turn_off()

meat_grinder = MeatGrinder("GrinderCorp", "MeatMaster", 800)
meat_grinder.turn_on()
meat_grinder.grind_meat()
meat_grinder.clean()
meat_grinder.turn_off()

########################################

class Ship:
    def __init__(self, name, length, max_speed, displacement):
        self.name = name
        self.length = length
        self.max_speed = max_speed
        self.displacement = displacement

    def start_engine(self):
        return f"{self.name}: Engine started."

    def stop_engine(self):
        return f"{self.name}: Engine stopped."

    def navigate(self, destination):
        return f"{self.name} is navigating to {destination}."

class Frigate(Ship):
    def __init__(self, name, length, max_speed, displacement, missile_count):
        super().__init__(name, length, max_speed, displacement)
        self.missile_count = missile_count

    def fire_missiles(self, target):
        return f"{self.name} fires {self.missile_count} missiles at {target}."

class Destroyer(Ship):
    def __init__(self, name, length, max_speed, displacement, gun_count):
        super().__init__(name, length, max_speed, displacement)
        self.gun_count = gun_count

    def fire_guns(self, target):
        return f"{self.name} fires {self.gun_count} guns at {target}."

class Cruiser(Ship):
    def __init__(self, name, length, max_speed, displacement, aircraft_capacity):
        super().__init__(name, length, max_speed, displacement)
        self.aircraft_capacity = aircraft_capacity

    def launch_aircraft(self, aircraft):
        return f"{self.name} launches {aircraft} aircraft."

frigate = Frigate("Frigate-1", 120, 30, 3000, 16)
destroyer = Destroyer("Destroyer-1", 150, 35, 4500, 5)
cruiser = Cruiser("Cruiser-1", 200, 25, 8000, 20)

print(frigate.start_engine())
print(destroyer.fire_guns("Enemy Ship"))
print(cruiser.launch_aircraft(4))
