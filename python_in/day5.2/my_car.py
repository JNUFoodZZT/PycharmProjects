from car import Car

my_new_car = Car('audi','a4','2016')
print(my_new_car.getInfo())

my_new_car.odometer_reading = 25
my_new_car.read_odometer()