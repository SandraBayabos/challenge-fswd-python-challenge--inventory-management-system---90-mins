class Product():
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return f'{self.name} - {self.quantity} items available'


class Warehouse_1():
    def __init__(self, location):
        self.location = location
        print(f'Warehouse 1 is located at {location}')


class Warehouse_2():
    def __init__(self, location):
        self.location = location
        print(f'Warehouse 2 is located at {location}')


# class Store():
#     def __init__(self):

####FOR PRODUCTS AVAILABLE####
keyblades = Product("Keyblade", 50)
potions = Product("Phoenix Down", 12)
print(repr(keyblades))
print(repr(potions))

####FOR WAREHOUSE LOCATION & ITEMS AVAILABLE#####
