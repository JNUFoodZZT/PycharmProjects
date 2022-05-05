users = ['ava','bella','carol','Dianna','Elieen','admin']
users1 = ['keir','pella','Ava']

# if users1:
#     for user in users1:
#         if user == 'admin':
#             print('Hello admin! ')
#         else:
#             print(f"hello {user}")
# else:
#     print('we need more')

for user in users1:
    if user.lower() in users:
        print(f'sorry {user}')
    else:
        print(f"{user} is ok")

new_users = users[:]
print(new_users)
for i in range(len(new_users)):
    new_users[i] = new_users[i].lower()
print(new_users)