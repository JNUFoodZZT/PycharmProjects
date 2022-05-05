# alien_color = ['green','red','yellow']
# if alien_color[2] == 'green':
#     print("get 5 points")
# elif alien_color[2] == 'yellow':
#     print('get 10 points')

available_toppings = ['ava','bella','carol','dianna']
requested_toppings = ['ava','bella']

for thing in requested_toppings:
    if thing not in available_toppings:
        t = True
    else:
        t = False
if not t:
    for thing in requested_toppings:
        print(f'added {thing}')
    print('over')
else:
    print('sorry')

