# def greet_user(username):
#     print(f'hello {username.title()} !')
#
# def favorite_book(bookname):
#     print(f"my favorite book is {bookname}!")
#
# def describe_pet(pet_type,pet_name):
#     print(f"\nI have a {pet_type}, her name is {pet_name}.")
#
# for i in range(3):
#     type = input('what is your pet:')
#     name = input('its name is:')
#     describe_pet(type,name)
#     print(f"\n")
#

# def make_shirt(word,size='x'):
#     print(word,size)
# make_shirt('fuck')

# def fullname(first_name,last_name,middle_name=''):
#     full_name = first_name.upper() + ' ' + middle_name.title() + last_name.title()
#     return full_name
# musician = fullname('zheng','tao')
# print(musician)
person = {'first':[],'last':[]}
fir = []
las = []
def build_name(first_name,last_name):
    person['first'].append(first_name)
    person['last'].append(last_name)
    return person
for i in range(3):
    fir.append(input('first name:'))
    las.append(input('last name:'))
    mes = build_name(fir[i],las[i])
    print(f"my name is {mes['first'][i].upper()} {mes['last'][i].title()}")
print(person)