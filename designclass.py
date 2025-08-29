# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"Device: {self.brand} {self.model}"


# Child class (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        # Call parent constructor
        super().__init__(brand, model)
        self.storage = storage
        self.battery = battery
        self.is_on = False
    
    # Method to power on the phone
    def power_on(self):
        self.is_on = True
        return f"{self.brand} {self.model} is now ON."
    
    # Method to power off the phone
    def power_off(self):
        self.is_on = False
        return f"{self.brand} {self.model} is now OFF."
    
    # Method to check battery
    def check_battery(self):
        return f"Battery level: {self.battery}%"
    
    # Method to take a picture (example of behavior)
    def take_picture(self):
        if self.is_on:
            return f"📸 Taking a picture with {self.brand} {self.model}."
        else:
            return f"{self.brand} {self.model} is OFF. Cannot take picture."


# Another child class (showing polymorphism)
class Tablet(Device):
    def __init__(self, brand, model, screen_size):
        super().__init__(brand, model)
        self.screen_size = screen_size
    
    def device_info(self):
        # Polymorphism: overriding parent method
        return f"Tablet: {self.brand} {self.model}, Screen size: {self.screen_size} inches"


# ======= Testing the classes =======
phone1 = Smartphone("Apple", "iPhone 14", "256GB", 85)
phone2 = Smartphone("Samsung", "Galaxy S23", "128GB", 65)
tablet1 = Tablet("Lenovo", "Tab P11", 11)

print(phone1.device_info())
print(phone1.power_on())
print(phone1.take_picture())
print(phone1.check_battery())

print(phone2.device_info())
print(phone2.power_off())

print(tablet1.device_info())  # Shows polymorphism
# Polymorphism Challenge 🎭

# Base class
class Vehicle:
    def move(self):
        return "Vehicle is moving"

# Child classes overriding the move() method
class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road"

class Plane(Vehicle):
    def move(self):
        return "✈️ Flying in the sky"

class Boat(Vehicle):
    def move(self):
        return "⛵ Sailing on the water"

class Bicycle(Vehicle):
    def move(self):
        return "🚴 Pedaling on the track"


# ======= Testing Polymorphism =======
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for v in vehicles:
    print(v.move())
    