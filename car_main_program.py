from car import Car

my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
miles_now = my_new_car.read_odometer()
print(f"Miles now = {my_new_car.read_odometer()}")
my_new_car.odometer_reading = 23
miles_now = my_new_car.read_odometer()
print(f"Miles now = {my_new_car.read_odometer()}")
my_new_car.update_odometer(46)
miles_now = my_new_car.read_odometer()
print(f"Miles now = {my_new_car.read_odometer()}")

my_used_car = Car('ford', 'focus', 2010)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(89786)
print(f"Miles now = {my_used_car.read_odometer()}")
my_used_car.increment_odometer(100)
print(f"Miles now = {my_used_car.read_odometer()}")