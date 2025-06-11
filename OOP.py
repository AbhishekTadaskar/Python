# Define a class named 'Car'
class Car:
    # Constructor method (__init__)
    def __init__(self, make, model, year):
        # Attributes (instance variables)
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0  # Default value for mileage

    # Method to display car details
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}, Mileage: {self.mileage} miles")

    # Method to update mileage
    def drive(self, miles):
        self.mileage += miles
        print(f"Driven {miles} miles. Total mileage: {self.mileage} miles")

# Create objects (instances) of the Car class
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Tesla", "Model S", 2023)

# Display car information
car1.display_info()
car2.display_info()

# Drive the cars and update mileage
# car1.drive(100)
# car2.drive(250)

# Display updated information
# car1.display_info()
# car2.display_info()
