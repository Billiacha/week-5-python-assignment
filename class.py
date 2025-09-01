# Base class
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery  # in percentage

    def call(self, contact):
        print(f"{self.brand} {self.model} is calling {contact} 📞")

    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"{self.brand} {self.model} charged to {self.battery}% 🔋")


# Derived class (Inheritance)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, battery, cooling_system):
        super().__init__(brand, model, battery)
        self.cooling_system = cooling_system

    def play_game(self, game):
        if self.battery > 20:
            print(f"{self.brand} {self.model} is playing {game} 🎮 with {self.cooling_system} cooling!")
            self.battery -= 20
        else:
            print(f"Battery too low to play {game} ❌")


# Example usage
phone1 = Smartphone("Samsung", "Galaxy S24", 80)
phone1.call("Alice")
phone1.charge(15)

gaming_phone = GamingPhone("Asus", "ROG 7", 60, "Liquid")
gaming_phone.play_game("PUBG")
gaming_phone.charge(30)
