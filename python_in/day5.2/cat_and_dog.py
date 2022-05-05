"""

"""

filename = ['dad.txt','cats.txt','dogs.txt','girls.txt']

def pet(filename):
    with open(filename,'r+') as pets:
        list = pets.readlines()
    print('|--------|')
    for pet in list:
        print(pet.strip())
    print('|------ -|')

for file in filename:
    try:
        pet(file)
    except FileNotFoundError:
        # print('not found')
        pass