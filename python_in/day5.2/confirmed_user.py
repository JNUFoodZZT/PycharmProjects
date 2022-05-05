# unconfirem_user = ['ava','bella','carol']
# confiren_user = []
# while True:
#     id = input('you id is:')
#     if id in unconfirem_user:
#         confiren_user.append(id)
#         print('yes')
#         break
#     else:
#         print('sorry and again')

pets = ['dog','cat','dog','goldfish','Cat','rabbit','cat']
print(pets)

pets1 = []
for pet in pets:
    pet = pet.lower()
    if pet != 'cat':
        pets1.append(pet)
print(pets1)