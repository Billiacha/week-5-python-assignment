class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")


# Example usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()   # Each one calls its own move() implementation
