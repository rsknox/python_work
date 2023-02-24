import Car from car

my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
miles_now = my_new_car.read_odometer()
print(f"Miles now = {my_new_car.read_odometer()}")
my_new_car.odometer_reading = 23
miles_now = my_new_car.read_odometer()
print(f"Miles now = {my_new_car.read_odometer()}")