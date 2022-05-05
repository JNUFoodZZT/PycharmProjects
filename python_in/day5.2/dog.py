class Dog():
    """ a modify of dogs"""

    def __init__(self,name,age):
        """chushihua """
        self.name = name
        self.age = age

    def sit(self):
        """moni dog dunxia"""
        print(self.name.title()+" is now sitting")

    def roll_over(self):
        """moni dog dagun"""
        print(self.name.title()+ ' rolled over!')


my_dog = Dog('diana','6')
your_dog = Dog('ava','2')
print(f"my dog's name is {my_dog.name.title()}, now she is {my_dog.age} years old!")
my_dog.roll_over()
print(f"your dog's name is {your_dog.name.title()}, now she is {your_dog.age} years old!")