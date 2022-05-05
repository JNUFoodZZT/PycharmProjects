# pizza ={
#     'crust' : 'thick',
#     'toppings' : ['mushroom','extra cheese']
# }
#
# print('your ordered a '+ pizza['crust'] + '-crust pizza with the following toppings: ')
# for topping in pizza['toppings']:
#     print('\t' + topping)

# users={
#     'ava':{
#         'cup': 'c',
#         'age': '21'
#     },
#     'bella':{
#         'cup':'b',
#         'age':'23'
#     }
# }
# for name,info in users.items():
#     print(f'her name is {name}\n'+
#           f"cup is {info['cup']}\n"+
#           f"age is {info['age']}\n")


pets = {
    'ava':{
        'kinds':'cat',
        'master':'dianna'
    },
    'carol':{
        'kinds':'wolf',
        'master':'elieen'
    },
    'bella':{
        'kinds':'rabbit',
        'master':'zheng'
    }
}

# for pet in pets.items():
#     print(f"{pet[0]}, it is a {pet[1]['kinds']}, and its master is {pet[1]['master']}")

for name,info in pets.items():
    print(f"{name}, it is a {info['kinds']}, and its master is {info['master']}")
