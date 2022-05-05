class Car():

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 300

    def getInfo(self):
        long_name = str(self.year) +' ' +self.make +' ' +self.model
        return long_name.title()

    def read_odometer(self):
        print(f"{self.odometer_reading} is yours ")

    def update_odometer(self, miles):
        self.odometer_reading = miles
        print(f"{self.odometer_reading} is yours ")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
        print(f"{self.odometer_reading} is yours ")


class Battery():
    """xiaolei"""

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self,*arg):
        if arg:
            self.battery_size = arg
            print(f"wuhu! this car has a {self.battery_size[0]} kWh battery")
        else:
            print(f"this car has a {self.battery_size} kWh battery")

    def get_range(self,*battery_last):
        if battery_last:
            self.battery_size = battery_last[0]
        range = self.battery_size *3
        print(f"it's range is {range} km")

class ElectricCar(Car):

    def __init__(self,make,model,year):
        """chushihua"""
        super().__init__(make,model,year)
        self.battery = Battery()





my_new_car =Car('audi','a4','2016')
print(my_new_car.getInfo())


# my_new_car.read_odometer()
# my_new_car.update_odometer(1100)
# my_new_car.increment_odometer(100)

my_ele_car = ElectricCar('tesla','model s','2018')
print(my_ele_car.getInfo())
my_ele_car.battery.describe_battery(15)
my_ele_car.battery.get_range(15)