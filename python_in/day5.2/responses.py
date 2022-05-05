responses = {}
polling_active = True
while polling_active:
    name = input('your name: ')
    response = input('which gril you would like to marry:')
    responses[name] = response

    conti = input('would you like to continue(yes/no):')
    if conti == 'no':
        break
print('---over---')
for name,girl in responses.items():
    print(f"{name} would like to marry with {girl}!")
