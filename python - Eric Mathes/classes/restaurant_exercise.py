class Restaurant:
    """A simple class for a restaurant"""

    def __init__(self, name, cuisine_type):
        """Initialize attributes"""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"Restaurant name is {self.name}  and it prepares  {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Restaurant {self.name} is opened")

    def set_number_served(self, customers_served):
        """Set the number of customers restaurant has served"""
        self.number_served = customers_served

class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type, flavors):
        super().__init__(name, cuisine_type)
        self.flavors = flavors
    
    def displayFlavors(self):
        for flavor in self.flavors:
            print(flavor)

restaurant = Restaurant("New Jawud","Indian & Pakistani dishes")
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(f"The restaurant has served {restaurant.number_served} customers")
restaurant.set_number_served(10)
print(f"The restaurant has served {restaurant.number_served} customers")

print()
restaurant2 = Restaurant("Brasserie", "African dishes")
restaurant2.describe_restaurant()

print()
restaurant3 = Restaurant("Lafayete", "French dishes")
restaurant3.describe_restaurant()

flavors = ["Vanilla", "chocolate", "mint"]
ice_cream_stand = IceCreamStand("Nats Ice Cream", "Sweets", flavors)
ice_cream_stand.displayFlavors()