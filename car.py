class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        # print(f"This car has {self.odometer_reading} miles on it.")
        return self.odometer_reading

    def update_odometer(self, mileage):
        """Set the odometer to the given value."""

        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""

        self.odometer_reading = self.odometer_reading + miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
     def __init__(self, make, model, year):
         """Initialize attributes of the parent class."""
         super().__init__(make, model, year)



