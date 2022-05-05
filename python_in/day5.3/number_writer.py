import json

# numbers = [2,3,4,6,7,9]
# filename = 'number.json'
# with open(filename,'w') as file_obj:
#     json.dump(numbers,file_obj)
#

# filename_1 = 'number.json'
# with open(filename_1) as file_obj:
#     numbers_1 = json.load(file_obj)
# print(numbers_1)

user_name = input('your name is:')
filename = 'username.json'
with open(filename,'w') as file_obj:
    json.dump(user_name,file_obj)
    print(f"we'll remember your name when you come back, {user_name.title()}!")

with open(filename) as file_obj:
    user_name_1 = json.load(file_obj)
    print(f"welcome back, {user_name_1.title()}!")