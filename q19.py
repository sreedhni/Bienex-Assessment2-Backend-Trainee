#19. Write program for building restaurant menu using class in Python.
class Menu:
    def __init__(self):
        self.veg_items = {}
        self.non_veg_items = {}
        self.juices = {}

    def add_veg_item(self, name, price):
        self.veg_items[name] = {"price": price}

    def add_non_veg_item(self, name, price):
        self.non_veg_items[name] = {"price": price}

    def add_juice(self, name, price):
        self.juices[name] = {"price": price}

    def print_menu(self):
        print("Restaurant Menu:")
        print("\nVegetarian Items:")
        for name, details in self.veg_items.items():
            print(f"{name}:  $ {details['price']:.2f}")
        print("\nNon-Vegetarian Items:")
        for name, details in self.non_veg_items.items():
            print(f"{name}:  $ {details['price']:.2f}")
        print("\nJuices:")
        for name, details in self.juices.items():
            print(f"{name}:  $ {details['price']:.2f}")


menu = Menu()
menu.add_veg_item("Dosha", 12.99)
menu.add_veg_item("Chaya", 15)
menu.add_veg_item("Coffee", 20)
menu.add_veg_item("Meals", 60)
menu.add_non_veg_item("Chicken Biriyani", 120)
menu.add_non_veg_item("puffs", 20)
menu.add_non_veg_item("alpham", 120)
menu.add_juice("Orange Juice", 5.99)
menu.add_juice("Apple Juice", 6.49)

menu.print_menu()

#==========================OUTPUT-==============================
# Restaurant Menu:

# Vegetarian Items:
# Dosha:  $ 12.99
# Chaya:  $ 15.00

# Non-Vegetarian Items:
# Chicken Biriyani:  $ 120.00
# alpham:  $ 120.00

# Juices:
# Orange Juice:  $ 5.99
# Apple Juice:  $ 6.49
