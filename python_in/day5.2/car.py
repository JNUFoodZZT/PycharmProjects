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
