# dimes = (200,50)
# print(dimes[0])
# print(dimes[1])
# for dime in dimes:
#     print(dime)
# new_dimes = (400,100)
# for dime in new_dimes:
#     print(dime)


foods = ('chicken','beef','apple','rice','ava')
for food in foods:
    print(food)

new_foods = [food for food in foods]
foods = new_foods
print(new_foods)
print(foods)