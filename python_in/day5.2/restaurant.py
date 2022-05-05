# class Restaurant():
#
#     def __init__(self,name,city):
#         self.name = name
#         self.city = city
#         self.number_served = 0
#
#
#     def open_restaurant(self):
#         print(f"{self.name} is opening, come to {self.city} right now!   [{self.number_served}]")
#
#     def set_number_served(self,num):
#         self.number_served = num
#         print(f"[{self.number_served}] people have served")
#     def increment_number_served(self,num):
#         self.number_served += num
#         print(f"[{self.number_served}] people have served")
#
# class IceCreamStand(Restaurant):
#
#     def __init__(self,name,city):
#         super().__init__(name,city)
#         self.number_served = 15
#         self.flavors = ['chocolate','apple','banana','nigger']
#
#     def list(self):
#         for flavor in self.flavors:
#             print(flavor)
#
#
# # res = Restaurant('cook house','wuxi')
# #
# # res.open_restaurant()
# # res.set_number_served(98)
# # res.increment_number_served(24)
#
# ice =IceCreamStand('Ice','zhijiang')
# ice.open_restaurant()
# ice.list()
#
# #
# #
class User():

    def __init__(self,first_name,last_name,*args):
        self.first_name = first_name
        self.last_name = last_name
        self.args = args
        self.times = 0

    def test_args(self):
        print(f"the name is {self.first_name.upper()} {self.last_name.title()}")
        for arg in self.args:
            print(arg)

    def increment_login(self):
        self.times += 1
        print(f"you have login [{self.times}] times")

    def reset(self):
        self.times = 0
        print(f"its [{self.times}] now, reset successfully!")

class Admin(User):

    def __init__(self,first_name='admin',last_name='',*args):
        super().__init__(first_name,last_name,*args)
        self.privileges = Privileges()


class Privileges():

    def __init__(self):
        self.privileges = ['can add post', 'can add ava', 'can add kira']

    def show_admin_privileges(self):
        for privilege in self.privileges:
            print(f"they have the right to {privilege}")



admin = Admin()
admin.privileges.show_admin_privileges()





# elieen = User('ava','bella','carol','diana')
# elieen.test_args()
#
# for i in range(3):
#     elieen.increment_login()
# elieen.reset()
#
# elieen.test_args()
#





# class Car():
#
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 300
#
#     def getInfo(self):
#         long_name = str(self.year) +' ' +self.make +' ' +self.model
#         return long_name.title()
#
#     def read_odometer(self):
#         print(f"{self.odometer_reading} is yours ")
#
#     def update_odometer(self, miles):
#         self.odometer_reading = miles
#         print(f"{self.odometer_reading} is yours ")
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#         print(f"{self.odometer_reading} is yours ")
#
#
# my_new_car =Car('audi','a4','2016')
# print(my_new_car.getInfo())
#
# my_new_car.read_odometer()
# my_new_car.update_odometer(1100)
# my_new_car.increment_odometer(100)
